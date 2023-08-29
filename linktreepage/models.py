from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from wagtail.fields import RichTextField

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


@register_snippet
class Link(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    link_tree_page = ParentalKey(
        "LinkTreePage", on_delete=models.CASCADE, related_name="links"
    )

    panels = [
        FieldPanel("title"),
        FieldPanel("url"),
    ]


class LinkTreePage(Page):
    template = "linktreepage/linktree_page.html"
    linktree_title = models.CharField(max_length=255)
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("linktree_title", classname="full title"),
        FieldPanel("description", classname="full"),
        InlinePanel("links", label="Links"),
    ]
