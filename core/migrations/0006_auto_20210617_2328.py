# Generated by Django 3.2.4 on 2021-06-18 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210617_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='experiences',
            field=models.CharField(default='--', max_length=500, verbose_name='Experiências'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='formation',
            field=models.CharField(default='--', max_length=100, verbose_name='Área(s) de Atuação'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='application',
            field=models.CharField(choices=[('Administrador', 'Administrador'), ('Python programmer', 'Python programmer'), ('PE Teacher', 'PE Teacher')], max_length=100, verbose_name='Vaga Selecionada'),
        ),
    ]