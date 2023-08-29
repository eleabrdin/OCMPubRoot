from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField

from wagtail.search import index


import series.models

from chapterpage.models import ChapterPage


class BookArcPage(Page):
    parent_page_types = ["series.Series"]
    template = "bookarcpage/book_arc_page.html"

    book_title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    book_series = models.ForeignKey(
        "series.Series",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="books",
    )

    announcements = RichTextField(blank=True)
    summary = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("book_title"),
        FieldPanel("description"),
        FieldPanel("book_series"),
        FieldPanel("announcements"),
        FieldPanel("summary"),
    ]

    search_fields = Page.search_fields + [
        index.SearchField("book_title"),
        index.SearchField("description"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["chapters"] = (
            ChapterPage.objects.live().public().order_by("first_published_at")
        )
        return context
