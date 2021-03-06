# Generated by Django 3.1.8 on 2021-10-12 22:51

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='homepage',
            name='portfolio',
            field=wagtail.core.fields.StreamField([('portfolio', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(required=False)), ('body', wagtail.core.blocks.TextBlock(required=False)), ('thumbnail', wagtail.images.blocks.ImageChooserBlock()), ('thumbnail_secondary', wagtail.images.blocks.ImageChooserBlock()), ('website', wagtail.core.blocks.URLBlock(required=False)), ('linkedin', wagtail.core.blocks.URLBlock(required=False)), ('twitter', wagtail.core.blocks.URLBlock(required=False)), ('industry', wagtail.snippets.blocks.SnippetChooserBlock(required=True, target_model='home.category'))]))], blank=True, null=True),
        ),
    ]
