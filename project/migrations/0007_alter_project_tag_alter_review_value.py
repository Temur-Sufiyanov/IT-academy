# Generated by Django 5.0.7 on 2024-08-15 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_review_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='proj_tag', to='project.tag'),
        ),
        migrations.AlterField(
            model_name='review',
            name='value',
            field=models.CharField(choices=[('-', 'salbiy'), ('+', 'ijobiy')], max_length=50),
        ),
    ]
