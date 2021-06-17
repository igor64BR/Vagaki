from django.db import models


class Base(models.Model):
    created = models.DateField('Data de Criação', auto_now_add=True)
    modified = models.DateField('Data de Modificação', auto_now=True)

    class Meta:
        abstract = True


class Offer(Base):
    SALARY_RANGES = (
        ('VL', 'Até R$1000'),
        ('L', 'De R$1000 a R$2000'),
        ('M', 'De R$2000 a R$3000'),
        ('H', 'Acima de R$3000')
    )
    EDUCATION = (
        ('EF', 'Fundamental'),
        ('EM', 'Médio'),
        ('T', 'Técnico'),
        ('S', 'Superior'),
        ('M', 'Mestrado/Pós/MBA'),
        ('D', 'Doutorado')
    )
    name = models.CharField('Vaga', max_length=100)
    salary = models.CharField('Salário', choices=SALARY_RANGES, null=False, blank=False, max_length=2)
    requirements = models.CharField('Requisitos', max_length=100)
    min_education = models.CharField('Escolaridade Mínima', max_length=2, choices=EDUCATION, blank=False, null=False)

    # class Meta:
    #     db_table = 'offer'


    def __str__(self):
        return self.name


class Candidate(Base):
    SALARY_RANGES = (
        ('VL', 'Até R$1000'),
        ('L', 'De R$1000 a R$2000'),
        ('M', 'De R$2000 a R$3000'),
        ('H', 'Acima de R$3000')
    )
    EDUCATION = (
        ('EF', 'Fundamental'),
        ('EM', 'Médio'),
        ('T', 'Técnico'),
        ('S', 'Superior'),
        ('M', 'Mestrado/Pós/MBA'),
        ('D', 'Doutorado')
    )
    name = models.CharField('Nome', max_length=100, blank=False, null=False)
    surname = models.CharField('Sobrenome', max_length=100, blank=False, null=False)
    email = models.EmailField('Email', max_length=100, blank=False, null=False)
    phone = models.IntegerField('Número de Telefone - Apenas Números')
    sal_claim = models.CharField('Pretensão Salarial', choices=SALARY_RANGES, max_length=2, blank=False, null=False)
    education = models.CharField('Última Escolaridade', choices=EDUCATION, max_length=2, blank=False, null=False)


    def __str__(self):
        return self.name
