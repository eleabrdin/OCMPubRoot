from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


from wagtail.search import index


class ChapterPage(Page):
    parent_page_types = ["bookarcpage.BookArcPage"]
    template = "chapterpage/chapter_page.html"

    book_arc_page = models.ForeignKey(
        "bookarcpage.BookArcPage",
        on_delete=models.SET_NULL,
        related_name="chapters",
        null=True,
        blank=True,
    )

    chapter_title = models.CharField(max_length=250)
    chapter_content = RichTextField(blank=True)

    previous_chapter = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )

    next_chapter = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("book_arc_page"),
        FieldPanel("chapter_title"),
        FieldPanel("previous_chapter"),
        FieldPanel("next_chapter"),
        FieldPanel("chapter_content"),
    ]
