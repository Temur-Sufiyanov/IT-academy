# Generated by Django 5.0.7 on 2024-09-04 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0015_alter_review_value_comment'),
        ('users', '0003_profil_tag_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profil'),
        ),
    ]