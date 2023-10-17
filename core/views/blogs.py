from django.views import generic

from core.models import Blog


class BlogsView(generic.ListView):
    model = Blog
    template_name = 'core/blogs.html'
    paginated_by = 10

    def get_queryset(self):
        return self.model.objects.active().order_by("-created")