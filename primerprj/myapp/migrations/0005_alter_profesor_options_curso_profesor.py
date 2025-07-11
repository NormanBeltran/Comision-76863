# Generated by Django 5.2 on 2025-07-09 00:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_alter_curso_turno"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profesor",
            options={"verbose_name": "Docente", "verbose_name_plural": "Docentes"},
        ),
        migrations.AddField(
            model_name="curso",
            name="profesor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="myapp.profesor",
            ),
        ),
    ]
