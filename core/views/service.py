from django.views import generic

from core.models import Service


class ServiceView(generic.DetailView):
    model = Service
    template_name = 'core/service.html'

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs['slug'])
