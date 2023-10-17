from django.views import generic

from core.models import Service


class ServicesView(generic.ListView):
    model = Service
    template_name = 'core/services.html'
    paginated_by = 10

    def get_queryset(self):
        return self.model.objects.active().order_by("-created")