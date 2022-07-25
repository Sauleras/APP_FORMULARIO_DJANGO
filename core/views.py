from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from core.forms import RegisterForms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

class Index(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        contexto = {
            "classcontent" : "content"
        }
        return render(request, self.template_name, contexto)

class Cadastro(TemplateView):
    template_name = "cadastro.html"

    def get(self, request, *args, **kwargs):
        contexto = {
            "classcontent" : "content"
        }
        return render(request, self.template_name, contexto)

    def post(self, request):
        form = RegisterForms(request.POST or None, request.FILES or None)

        if form.is_valid():
            print("############################# FORM " + str(form))

            username = form.cleaned_data['username'] #request.POST['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name'] 
            email = form.cleaned_data['email']
            pass1 = form.cleaned_data['password']            

            myuser = User.objects.create_user(username, email, pass1) 
            myuser.first_name = first_name
            myuser.last_name = last_name

            myuser.save()

            messages.success(request, "Usuário cadastrado com sucesso.")
            
            return redirect('logar')

        else:
            
            messages.error(request, "Erro ao validar dados") 
            
        return render(request, self.template_name)

class Logar(TemplateView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        contexto = {
            "classcontent" : "content"
        }
        return render(request, self.template_name, contexto)

    def post(self, request):

        if request.method == 'POST':

            username = request.POST['username']
            pass1 = request.POST['password']          

            user_obj = authenticate(username=username, password=pass1)
            
            if user_obj is not None:
                login(request, user_obj)
                return redirect('index')
            
            else:

                messages.error(request, 'Credenciais invalidas')
            
        return render(request, self.template_name)

def sair(request):
    logout(request)
    messages.success(request, "Deslogado com sucesso!")
    return HttpResponseRedirect('/logar')