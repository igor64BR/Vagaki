# Generated by Django 3.2.4 on 2021-06-18 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_offer_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='application',
            field=models.CharField(choices=[('Administrador', 'Administrador')], default='Admin', max_length=100, verbose_name='Vaga Selecionada'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='education',
            field=models.CharField(choices=[('Fundamental', 'Fundamental'), ('Médio', 'Médio'), ('Técnico', 'Técnico'), ('Superior', 'Superior'), ('Mestrado/Pós/MBA', 'Mestrado/Pós/MBA'), ('Doutorado', 'Doutorado')], max_length=16, verbose_name='Última Escolaridade'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='sal_claim',
            field=models.CharField(choices=[('Até 1000', 'Até R$1000'), ('1000 - 2000', 'De R$1000 a R$2000'), ('2000 - 3000', 'De R$2000 a R$3000'), ('Acima de 3000', 'Acima de R$3000')], max_length=13, verbose_name='Pretensão Salarial'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='min_education',
            field=models.CharField(choices=[('Fundamental', 'Fundamental'), ('Médio', 'Médio'), ('Técnico', 'Técnico'), ('Superior', 'Superior'), ('Mestrado/Pós/MBA', 'Mestrado/Pós/MBA'), ('Doutorado', 'Doutorado')], max_length=16, verbose_name='Escolaridade Mínima'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='salary',
            field=models.CharField(choices=[('Até 1000', 'Até R$1000'), ('1000 - 2000', 'De R$1000 a R$2000'), ('2000 - 3000', 'De R$2000 a R$3000'), ('Acima de 3000', 'Acima de R$3000')], max_length=13, verbose_name='Faixa Salarial'),
        ),
    ]
