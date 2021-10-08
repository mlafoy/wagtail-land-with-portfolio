from django.db import models

from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock

from wagtail.snippets.models import register_snippet




class TeamBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    name = blocks.TextBlock(required=False)
    title = blocks.TextBlock(required=False)
    link = blocks.URLBlock(required=False)


PORTFOLIO_CHOICES = [
    ('Commerce', 'Commerce'),
    ('Education', 'Education'),
    ('Health', 'Health'),
    ('Entertainment', 'Entertainment'),
]

class PortfolioBlock(blocks.StructBlock):
    title = blocks.TextBlock(required=False)
    body = blocks.TextBlock(required=False)
    thumbnail = ImageChooserBlock()
    thumbnail_secondary = ImageChooserBlock()
    # industry = blocks.TextBlock(required=False)
    website = blocks.URLBlock(required=False)
    linkedin = blocks.URLBlock(required=False)
    twitter = blocks.URLBlock(required=False)
    industry = blocks.ChoiceBlock(required=False, choices=PORTFOLIO_CHOICES)


class HomePage(Page):
    # banner = models.ForeignKey(
    #     'wagtailimages.image',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+'
    # )
    team = StreamField([
        ('teams', TeamBlock()),
    ],
        null=True,
        blank=True
    )
    portfolio = StreamField([
        ('portfolio', PortfolioBlock()),
    ],
        null=True,
        blank=True
    )
    about_us_title = models.CharField(max_length=50, null=True, blank=True)
    about_us_bold = models.TextField(max_length=1000, null=True, blank=True)
    about_us_small = models.TextField(max_length=1000, null=True, blank=True)

    content_panels = Page.content_panels + [
        # ImageChooserPanel('banner'),
        MultiFieldPanel(
            [
                FieldPanel('about_us_title'),
                FieldPanel('about_us_bold'),
                FieldPanel('about_us_small'),
            ],
            heading="Black Section Content",
            # classname="-"
        ),
        StreamFieldPanel("team"),
        StreamFieldPanel("portfolio"),
    ]

    # def get_context(self, request, *args, **kwargs):
    #     context = super().get_context(request, *args, **kwargs)
    #     context["portfolios"] = Portfolio.objects.all()
    #     return context


# @register_snippet
# class Portfolio(models.Model):
#     title = models.CharField(max_length=255)
#     body = models.TextField(max_length=255)
#     thumbnail = models.ForeignKey(
#         'wagtailimages.image',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+'
#     )
#     thumbnail_secondary = models.ForeignKey(
#         'wagtailimages.image',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+'
#     )
#     # industry = blocks.TextBlock(required=False)
#     website = models.URLField(null=True, blank=True)
#     linkedin = models.URLField(null=True, blank=True)
#     twitter = models.URLField(null=True, blank=True)
#     industry = models.CharField(max_length=255, choices=PORTFOLIO_CHOICES)

#     panels = [
#         ImageChooserPanel('thumbnail'),
#         ImageChooserPanel('thumbnail_secondary'),
#         FieldPanel('title'),
#         FieldPanel('body'),
#         FieldPanel('website'),
#         FieldPanel('linkedin'),
#         FieldPanel('twitter'),
#         FieldPanel('industry'),
#     ]