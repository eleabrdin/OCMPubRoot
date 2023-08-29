from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField

from series.models import Series  # Update this import if necessary


class AuthorPage(Page):
    template = "authorpage/author_page.html"

    bio = RichTextField(blank=True)
    name = models.CharField(max_length=255, null=True)
    announcements = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("bio"),
        FieldPanel("name"),
        FieldPanel("announcements"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        context["series"] = (
            Series.objects.live().public().order_by("-first_published_at")
        )
        return context
