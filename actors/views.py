from django.shortcuts import render, redirect
from django.views import View
from genres.views import montar_headers
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import requests

@method_decorator(login_required(login_url = 'login_api'), name='dispatch')
class ActorView(View):
    def get(self, request, *args, **kwargs):
        headers = montar_headers(request)
        if not headers:
            return redirect('login_api')
        
        url = 'http://127.0.0.1:8080/api/v1/actors/'

        try:
            response = requests.get(url = url, headers = headers)
            response.raise_for_status()
            actors = response.json()
            return render(request, 'actors.html', {'actors':actors})
        except requests.exceptions.HTTPError:
            actors = None
        return render(request, 'actors.html', {'actors':actors})

class ActorDetailView(View):
    def get(self, request, *args, **kwargs):
        headers = montar_headers(request)
        if not headers:
            return redirect('login_api')
        
        pk = self.kwargs.get('pk')
        url = f'http://127.0.0.1:8080/api/v1/actors/{pk}/'

        try:
            response = requests.get(url = url, headers = headers)
            response.raise_for_status()
            actor = response.json()
            return render(request, 'actor_detail.html', {'actor':actor})
        except requests.exceptions.HTTPError as erro:
            actor = None
            print(erro)
        return render(request, 'actor_detail.html', {'actor':actor})

    



    
        

