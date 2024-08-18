from django import forms

class ApiForm(forms.Form):
    api_url = forms.URLField(label='API URL', required=True)
    # Create a form with the field URL