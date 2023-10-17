from django.views import generic
from core.models import requests
from core.forms import RequestsForm

class RequestsView(generic.FormView):
    template_name = 'core/requests.html'
    form_class = RequestsForm
    success_url = '/'