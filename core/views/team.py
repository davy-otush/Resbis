from django.views import generic


class TeamView(generic.TemplateView):
    template_name = 'core/team.html'
