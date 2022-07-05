import json
from django.http import JsonResponse
from django.shortcuts import redirect, render

from django.db import connection

import datetime
# Create your views here.
def initdatabase():
    with connection.cursor() as cursor:
        cursor.execute("CREATE TABLE IF NOT EXISTS logs ( id int not null primary key auto_increment, time varchar(100), ip varchar(100) )")
def Home(request):
    initdatabase()
    data={}
    current_datetime = datetime.datetime.now()
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    with connection.cursor() as cursor:
        cursor.execute(f"insert into logs (time,ip) values ('{current_datetime}','{ip}')")
    return JsonResponse(data)

def add(request):
    if request.method=="POST":
        time=request.POST['time']
        ip=request.POST['ip']
        with connection.cursor() as cursor:
            cursor.execute(f"insert into logs (time,ip) values ('{time}','{ip}')")
    return render(request,"index.html",{})
def edit(request):
    data={}
    logs=[]
    with connection.cursor() as cursor:
        cursor.execute("select * from logs")
        row=cursor.fetchall()
        for i in row:
            d={
                'id':i[0],
                'time':i[1],
                'ip':i[2], 
            }
            logs.append(d)
        data={
            'logs': logs
        }
    return render(request,"edit.html",data)
def update(request):
    
    if request.method=='POST':
        time=request.POST["time"]
        ip=request.POST["ip"]
        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE logs SET time = {time} , ip = {ip} WHERE id={id}")
            
    data={
    }
    print(request.GET['id'])
    with connection.cursor() as cursor:
            cursor.execute(f"select * from logs where id={request.GET['id']}")
            row= cursor.fetchone()
            data={
                'time': row[1],
                'ip': row[2]
            }   
    return render(request,"update.html",data)
def delete(request):
    data={}
    with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM logs WHERE id={request.GET['id']}")
    return redirect("/")
    