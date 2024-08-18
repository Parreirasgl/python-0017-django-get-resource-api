# api_app/views.py
from django.shortcuts import render 
import requests  # Import the module requests in order to make HTTP requests
from .forms import ApiForm

def api_view(request):
    response_data = None  # If response_data weren't initialized, this conditional containing response_data in the templante might not work 

    if request.method == 'POST':
        form = ApiForm(request.POST)  # Create an object of the Class ApiForm with data from the request
        if form.is_valid():
            api_url = form.cleaned_data['api_url']  # Get content of the form (URL of the API)
            try:
                response = requests.get(api_url)  # Makes the GET request using the URL
                response_data = response.json()  # Converts the response to JSON (one can response.text to convert to text)
            except requests.exceptions.RequestException as e:  # Catches any request-related exceptions
                response_data = str(e)  # Stores the exception message in response_data
    else:
        form = ApiForm()  # Creates an empty instance of ApiForm for rendering the form initially

    return render(request, 'api_app/api_form.html', {'form': form, 'response_data': response_data})  # Passes the form and response_data to the template

