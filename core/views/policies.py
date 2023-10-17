from django.views import generic

from core.models import Policy


class PoliciesView(generic.ListView):
    model = Policy
    template_name = 'core/policies.html'
    paginated_by = 10

    def get_queryset(self):
        return self.model.objects.active().order_by("-creation_date")