from django.views import generic

from core.models import Policy


class PolicyView(generic.DetailView):
    model = Policy
    template_name = 'core/policy.html'

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs['slug'])
