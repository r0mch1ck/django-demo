Вот команды с подробными пояснениями в формате Markdown:

## 🐍 Django REST Framework — команды запуска и настройки

| Команда                                  | Пояснение                                             |
|------------------------------------------|-------------------------------------------------------|
| `pip install djangorestframework`        | Установка Django REST Framework                       |
| `python manage.py makemigrations`        | Создание миграций для моделей (подготовка изменений в базе данных) |
| `python manage.py migrate`               | Применение созданных миграций (внесение изменений в базу данных) |
| `python manage.py runserver`             | Запуск встроенного сервера Django для локальной разработки (по умолчанию на `http://127.0.0.1:8000`) |
| `python manage.py drf_create_token <user_name>` | Создание авторизационного токена DRF для указанного пользователя (`<user_name>` нужно заменить на реальное имя пользователя) |

### 📌 Пример использования команды создания токена:

```bash
python manage.py drf_create_token test
```

Выведет токен, например:

```
Generated token cc735f64132c98e88ee533c60d13a794486f7e0d for user test
```

Теперь этот токен можно использовать для авторизации в запросах к API:

```bash
curl -X GET http://localhost:8000/api/example/ \
-H "Authorization: Token cc735f64132c98e88ee533c60d13a794486f7e0d"
```
