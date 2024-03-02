from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    print(response)
    return HttpResponse('hello world!')


def test(response):
    return HttpResponse('<h1>Test page</h1>')
