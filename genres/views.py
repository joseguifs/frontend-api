from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
import requests
from Api.service import Auth

def montar_headers(request):
    token = request.session.get('jwt')
    if not token:
        return False
    return {'Authorization': f'Bearer {token}'}

class GenreView(View):
    def get(self, request, *args, **kwargs):
        headers = montar_headers(request)
        if not headers:
            return redirect('login_api')
        auth = Auth()
        try:
            genres = auth.get_genres(headers)
            return render(request, 'genres.html', {'genres':genres})
        except ValueError as erro:
            return render(request, 'login_api.html', {'erro':erro})

class GenreDetailView(View):
    def get(self, request, *args,**kwargs):
        headers = montar_headers(request)
        if not headers:
            return redirect('login_api')
        auth = Auth()
        pk = self.kwargs.get('pk') #  Django automaticamente passa o valor de pk como argumento para a view
        try:
            genre = auth.get_genre_detail(pk, headers)
            return render(request,'genre_detail.html', {'genre':genre})
        except ValueError:
            genre = None
        return render(request, 'genre_detail.html', {'genre':genre})

class GenreCreateView(View):
    def get(self, request, *args, **kwargs):
        headers = montar_headers(request)
        if not headers:
            redirect('login_api')
        return render(request, 'genre_create.html')
        
    def post(self, request):
        headers = montar_headers(request)
        if not headers:
            return redirect('login_api')
        
        auth = Auth()
        genre_name = request.POST.get('name')
        
        payload = {
            "name":genre_name
        }
        
        try:
            auth.post_genre(payload, headers)
            return redirect('genres')
        except ValueError as message:
            return render(request, 'genre_create.html', {'error':message})
        
# resolver erro pra fazer post de genre pois quando esta salvando no bd, name está sendo 0