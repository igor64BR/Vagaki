from django.db import models


class Base(models.Model):
    created = models.DateField('Data de Criação', auto_now_add=True)
    modified = models.DateField('Data de Modificação', auto_now=True)

    class Meta:
        abstract = True


class Offer(Base):
    SALARY_RANGES = (
        ('Até 1000', 'Até R$1000'),
        ('1000 - 2000', 'De R$1000 a R$2000'),
        ('2000 - 3000', 'De R$2000 a R$3000'),
        ('Acima de 3000', 'Acima de R$3000')
    )
    EDUCATION = (
        ('Fundamental', 'Fundamental'),
        ('Médio', 'Médio'),
        ('Técnico', 'Técnico'),
        ('Superior', 'Superior'),
        ('Mestrado/Pós/MBA', 'Mestrado/Pós/MBA'),
        ('Doutorado', 'Doutorado')
    )

    name = models.CharField('Vaga', max_length=100)
    salary = models.CharField('Faixa Salarial', choices=SALARY_RANGES, null=False, blank=False, max_length=13)
    requirements = models.CharField('Requisitos', max_length=100)
    min_education = models.CharField('Escolaridade Mínima', max_length=16, choices=EDUCATION, blank=False, null=False)

    def __str__(self):
        return self.name


class Candidate(Base):
    SALARY_RANGES = (
        ('Até 1000', 'Até R$1000'),
        ('1000 - 2000', 'De R$1000 a R$2000'),
        ('2000 - 3000', 'De R$2000 a R$3000'),
        ('Acima de 3000', 'Acima de R$3000')
    )
    EDUCATION = (
        ('Fundamental', 'Fundamental'),
        ('Médio', 'Médio'),
        ('Técnico', 'Técnico'),
        ('Superior', 'Superior'),
        ('Mestrado/Pós/MBA', 'Mestrado/Pós/MBA'),
        ('Doutorado', 'Doutorado')
    )
    OFFERS = tuple([(str(offer.name), str(offer.name)) for offer in Offer.objects.all()])

    name = models.CharField('Nome', max_length=100, blank=False, null=False)
    surname = models.CharField('Sobrenome', max_length=100, blank=False, null=False)
    email = models.EmailField('Email', max_length=100, blank=False, null=False)
    phone = models.IntegerField('Número de Telefone - Apenas Números')
    sal_claim = models.CharField('Pretensão Salarial', choices=SALARY_RANGES, max_length=13, blank=False, null=False)
    experiences = models.CharField('Experiências', max_length=500)
    formation = models.CharField('Área(s) de Atuação', max_length=100)
    education = models.CharField('Última Escolaridade', choices=EDUCATION, max_length=16, blank=False, null=False)
    application = models.CharField('Vaga Selecionada', choices=OFFERS, max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name
