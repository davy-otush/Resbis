from django.views import generic
from core.models import contact
from core.forms import ContactForm

class ContactView(generic.FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = '/'