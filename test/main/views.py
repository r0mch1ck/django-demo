from django.shortcuts import render, redirect
from django.http import JsonResponse, FileResponse, Http404
from django.conf import settings
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


def index(request):
    data = {
        "message": "Hi. It's JSON!",
        "status": "200"
    }
    return redirect('/users/login')


def html_page(request):
    return render(request, 'main/html_page.html')


def image_view(request):
    image_path = os.path.join(settings.BASE_DIR, 'main', 'static', 'main', 'imag_to_test.png')
    try:
        return FileResponse(open(image_path, 'rb'), content_type='image/png')
    except FileNotFoundError:
        raise Http404("Изображение не найдено")



