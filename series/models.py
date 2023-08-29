from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import RichTextField

from bookarcpage.models import BookArcPage


class Series(Page):
    template = "series/series_page.html"
    description = RichTextField(blank=True)

    author = models.ForeignKey(
        "authorpage.AuthorPage",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="series",
    )

    current_info = RichTextField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("description", classname="full"),
        FieldPanel("current_info", classname="full"),
    ]

    parent_page_types = ["authorpage.AuthorPage"]

    description = models.CharField(max_length=255)

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("current_info", classname="full"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["books"] = (
            BookArcPage.objects.live().public().order_by("-first_published_at")
        )
        return context
