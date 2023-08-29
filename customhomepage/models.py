from django.db import models
from wagtail.models import Page, ParentalKey
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel

from authorpage.models import AuthorPage
from bookarcpage.models import BookArcPage
from series.models import Series


class BookArcPageChooser(models.Model):
    """
    This is a through model for the ManyToMany relationship between
    HomePage and BookArcPage.
    """

    homepage = ParentalKey(
        "HomePage", on_delete=models.CASCADE, related_name="bookarcpages"
    )
    bookarcpage = models.ForeignKey(
        BookArcPage, on_delete=models.CASCADE, related_name="+"
    )

    panels = [
        FieldPanel("bookarcpage"),
    ]

    class Meta:
        unique_together = (("homepage", "bookarcpage"),)


class SeriesChooser(models.Model):
    """
    This is a through model for the ManyToMany relationship between
    HomePage and Series.
    """

    homepage = ParentalKey(
        "HomePage", on_delete=models.CASCADE, related_name="seriespages"
    )
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name="+")

    panels = [
        FieldPanel("series"),
    ]

    class Meta:
        unique_together = (("homepage", "series"),)


class HomePage(Page):
    template = "customhomepage/homepage.html"

    page_ptr = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        parent_link=True,
        related_name="custom_homepage_ptr",
    )

    body = RichTextField(blank=True)
    announcement = RichTextField(blank=True)
    current = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
        FieldPanel("announcement", classname="full"),
        FieldPanel("current", classname="full"),
        MultiFieldPanel(
            [
                InlinePanel(
                    "bookarcpages",
                    label="Book/Arc Selection",
                )
            ],
            heading="Book/Arc Selection",
        ),
        MultiFieldPanel(
            [InlinePanel("seriespages", label="Series")],
            heading="Series",
        ),
    ]

    def get_authors(self):
        return AuthorPage.objects.live()  # Returns all live AuthorPage instances
