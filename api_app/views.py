# api_app/views.py
from django.shortcuts import render
import requests  # precisa instalar
from .forms import ApiForm

def api_view(request):
    response_data = None

    if request.method == 'POST':
        form = ApiForm(request.POST)
        if form.is_valid():
            api_url = form.cleaned_data['api_url']
            try:
                response = requests.get(api_url)
                response_data = response.json()  # ou response.text para texto puro
            except requests.exceptions.RequestException as e:
                response_data = str(e)
    else:
        form = ApiForm()

    return render(request, 'api_app/api_form.html', {'form': form, 'response_data': response_data})

