from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    phone_number = models.CharField(
        max_length=15, blank=True, null=True,
        verbose_name="Номер телефона пользователя"
    )

    bio = models.TextField(
        max_length=600, blank=True, null=True,
        verbose_name="Биография пользователя",
        help_text="Краткая информация о пользователе"
    )

    date_of_birth = models.DateField(
        blank=True, null=True,
        verbose_name="Дата рождения пользователя"
    )

    avatar = models.ImageField(
        upload_to='avatars/', blank=True, null=True,
        verbose_name="Аватар пользователя"
    )

    is_email_verified = models.BooleanField(
        default=False,
        verbose_name="Подтвержден ли email пользователя"
    )

    def __str__(self):
        """
        Возвращает человекочитаемое представление пользователя.
        Обычно это username, но можно использовать любые другие поля.
        """
        return self.username

    def get_full_name(self):
        """
        Возвращает полное имя пользователя, комбинируя first_name и last_name.
        """
        full_name = f"{self.first_name} {self.last_name}".strip()
        return full_name or self.username

    def get_short_name(self):
        """
        Возвращает короткое имя пользователя (обычно first_name).
        """
        return self.first_name or self.username

    def save(self, *args, **kwargs):
        """
        Переопределение метода save() для кастомных действий перед сохранением модели.
        Например, здесь можно привести телефон к стандартному виду перед сохранением.
        """
        if self.phone_number:
            self.phone_number = self.phone_number.strip().replace(" ", "")
            if self.phone_number[0] == '8':
                self.phone_number = '+7' + self.phone_number[1:]

        if not self.bio:
            self.bio = 'Привет! Я новый пользователь.'
        super().save(*args, **kwargs)

