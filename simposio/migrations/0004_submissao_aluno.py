# Generated by Django 2.0.13 on 2019-10-29 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simposio', '0003_auto_20190829_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissao',
            name='aluno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='simposio.Aluno'),
            preserve_default=False,
        ),
    ]
