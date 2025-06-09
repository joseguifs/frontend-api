from django.shortcuts import render, redirect
from django.views import View
import requests
from Api.service import Auth

# Create your views here.

class LoginView(View):
    def post(self, request):
        auth = Auth()
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            request.session['jwt'] = auth.get_token(username, password) # modificando session_data da tabela django_session
            return redirect('genres')
        except ValueError as erro:
            return render(request, 'login_api.html', {'error': f'{erro}'})
    def get(self, request):
        return render(request, 'login_api.html')
    
class RecuperarSenha(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'recuperar_senha.html')
    
    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        data = {
            "username":username,
            "email":email
        }
        response = requests.post(url = 'http://localhost:8080/api/v1/recovery/', json = data)
        message = response.json()
        return redirect("login_api")
