from django.shortcuts import render,redirect
from .forms import UserForm
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import UserModel
# Create your views here.
def userView(request):
    fm=UserForm()
    if request.method=='POST':
        fm=UserForm(data=request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponse('success...')


    return render(request,'index.html',{'form':fm})

@csrf_exempt
def userNamevalidateView(request):
    import json
    data=json.loads(request.body)
    username=data['username']
    if not str(username).isalnum():
        return JsonResponse({'user_name_error':'Username should contain only alphanumeric characters'})
    elif UserModel.objects.filter(name=username).exists():
        return JsonResponse({'user_name_error':'Username already exists'})
    return JsonResponse({'usernamevalid':True})

@csrf_exempt
def pwdvalidate(request):
    import json
    def oneMinChar(s):
        return any(c.isupper() for c in s ) and any(c.isdigit() for c in s)
    data=json.loads(request.body)
    pwd=data['password']
    if len(pwd)<4:
        return JsonResponse({"pwd_security_error":"Password must be at least 4 characters"}) 
    elif not oneMinChar(pwd):
        return JsonResponse({"pwd_security_error":"Password must contain at least one uppercase letter and one digit"})
    else:
        return JsonResponse({"passwordvalid":True})

@csrf_exempt
def match_password(request):
    import json
    data=json.loads(request.body)
    pwd=data['password']
    re_pwd=data['re_password']
    if pwd!=re_pwd:
        return JsonResponse({"match_error":"Passwords do not match"})
    else:
        return JsonResponse({"matchvalid":True})
