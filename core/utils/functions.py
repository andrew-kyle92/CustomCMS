# All the functions for the entire project
from cms.models.models import Page


def get_pages():
    pages = Page.objects.all()
    return pages
