from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.core import serializers
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from cbvapp.models import person
from django.urls import reverse_lazy
from cbvapp.forms import userform, profileform
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
class myCBV(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['d'] = "data 1"
        context['i'] = 20
        return context

class personList(ListView):
    model = person
    context_object_name = "person"

class persondetail(DetailView):
    model = person

class personview(CreateView):
    model = person
    fields = ('name','email','age','profile_pic')

class personupdate(UpdateView):
    model = person
    fields = ('name','email','age','profile_pic')
    success_url = reverse_lazy('cbvapp:list')

class persondelete(DeleteView):
    model = person
    success_url = reverse_lazy('cbvapp:list')
    template_name ='cbvapp/delete.html'

def registration(request):
    form = userform()
    profile = profileform()
    if request.method == "POST":
        if "signup" in request.POST:
            form = userform(request.POST)
            profile = profileform(request.POST,request.FILES)
            if form.is_valid() and profile.is_valid():
                user = form.save()
                # user.set_password(user.password)
                user.is_staff = True
                user.save()

                profile = profile.save(commit=False)
                profile.user = user
                profile.save()
                return HttpResponseRedirect('/cbvapp/signin/')

    return render(request,'signup.html',{'user':userform,'profile':profileform})

def userlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/cbvapp/')
        else:
            return HttpResponse("Sorry You are not registred")
    return render(request,'login.html')

def checkuser(request):
    username = request.GET.get('username')
    check = User.objects.filter(username__iexact=username).exists()
    result = {}
    result['c']=check

    return JsonResponse(result)

def searchuser(request):
    username = request.GET.get('username')
    result = User.objects.filter(username__icontains=username)
    js= serializers.serialize("json", result)
    return HttpResponse(js,content_type='application/json')
