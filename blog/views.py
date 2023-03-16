from django.views.generic import TemplateView

# Blog
class Blog(TemplateView):
    template_name = "blog/blog.html"
class BlogGrid(TemplateView):
    template_name = "blog/blog-grid.html"
class BlogModern(TemplateView):
    template_name = "blog/blog-modern.html"
class BlogMasonry(TemplateView):
    template_name = "blog/blog-masonry.html"
class BlogDetails(TemplateView):
    template_name = "blog/blog-details.html"
class BlogAuthor(TemplateView):
    template_name = "blog/blog-author.html"