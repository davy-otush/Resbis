from django.views import generic

from core.models import Blog


class BlogView(generic.DetailView):
    model = Blog
    template_name = 'core/blog.html'

    def get_object(self):
        return self.model.objects.get(slug=self.kwargs['slug'])
