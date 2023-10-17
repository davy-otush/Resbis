from django.views import generic


class PricesView(generic.TemplateView):
    template_name = 'core/prices.html'
