# Generated by Django 4.2.2 on 2023-06-26 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookarcpage', '0004_rename_sumary_bookarcpage_summary'),
        ('customhomepage', '0002_homepage_announcement_homepage_current'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookArcPageChooser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookarcpage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chooser_bookarcpages', to='bookarcpage.bookarcpage')),
                ('homepage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chooser_homepages', to='customhomepage.homepage')),
            ],
            options={
                'unique_together': {('homepage', 'bookarcpage')},
            },
        ),
    ]