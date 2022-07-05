import json
from django.http import JsonResponse
from django.shortcuts import render
from django.db import connection

import datetime
# Create your views here.
def Home(request):
    data={}
    current_datetime = datetime.datetime.now()
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    with connection.cursor() as cursor:
        cursor.execute(f"insert into logs (time,url) values ('{current_datetime}','{ip}')")
        # row=cursor.fetchall()
    return JsonResponse(data)

def add(request):
    if request.method=="POST":
        time=request.POST['time']
        ip=request.POST['ip']
        with connection.cursor() as cursor:
            cursor.execute(f"insert into logs (time,url) values ('{time}','{ip}')")
    return render(request,"index.html",{})

def edit(request):
    data={}
    with connection.cursor() as cursor:
        cursor.execute("select * from logs")
        row=cursor.fetchall()
    return JsonResponse(data)
def delete(request):
    pass
    