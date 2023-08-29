from django.db import models

from wagtail.models import Page


class HomePage(Page):
    page_ptr = models.OneToOneField(
        Page,
        on_delete=models.CASCADE,
        parent_link=True,
        related_name="home_homepage_ptr",
    )
