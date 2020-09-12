import uuid
from django.utils import timezone
from .creds import db
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
def index(request):
    return render(request,'main/generate.html')
def addUser(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        email = request.POST.get('email')
        api_key = str(uuid.uuid4())
        status = db.user.insert_one({
            'id' : str(uuid.uuid4()),
            'name' : name,
            'rollno' : rollno,
            'email' : email,
            'api_key' : api_key,
            'datetime' : timezone.now(),
            'updatedtime' : ''
        })
        if status:
            messages.success(request,'User Added')
        user_db = db[rollno]
        user_db.insert_one({
            'api_key' : api_key,
            'id' : str(uuid.uuid4()),
            'name' : name,
            'rollno' : rollno,
            'email' : email,
            'api_key' : api_key,
            'datetime' : timezone.now(),
            'updatedtime' : ''
        })
    return HttpResponseRedirect('/')
def deleteUser(request,user):
    get_user_db = db[user]
    get_user_db.drop()
    action_status = db.user.delete_one({'rollno' : user})
    if action_status:
        return HttpResponseRedirect('/details/')
    return '<h1>Error Encountered</h1>'
def updateUser(request,user):
    if request.method == 'POST':
        name = request.POST.get('name')
        rollno = request.POST.get('rollno')
        email = request.POST.get('email')
        api_key = request.POST.get('api_key')
        action_status = db.user.update_one(
                {
                    'id' : user
                },
                {
                    '$set': 
                    {
                        'name' : name,
                        'rollno' : rollno,
                        'email' : email,
                        'api_key' : api_key,
                        'updatedtime' : timezone.now()
                    }
                })
        if action_status:
            return HttpResponseRedirect('/details/')
        return '<h1>Error Encountered</h1>'
    messages.error(request,'Cannot Update')
    return HttpResponseRedirect('/details/')
def details(request):
    action_status = db.user.find()
    return render(request,'main/view.html',{'users' : action_status})
def detailedUser(request,user):
    action_status = db.user.find_one({'rollno' : user})
    if action_status:
        collection = action_status['rollno']
        selected_db = db[collection]
        user_details = selected_db.find()
        return render(request,'main/detaileduser.html',{'userDetails':user_details})
    return HttpResponseRedirect('/details/')

