from django.db import models

TIPOS_DE_PROVA = (
    ('leitura', 'Leitura'),
    ('escrita', 'Escrita'),
)

TIPOS_DE_TURMA = (
    ('begginer', 'Begginer'),
    ('advanced', 'Advanced'),
)

class Aluno(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Turma(models.Model):
    codigo = models.IntegerField()
    nivel = models.CharField(max_length=100, choices=TIPOS_DE_TURMA)
    alunos = models.ManyToManyField(Aluno)
    professores = models.ManyToManyField(Professor)

    def __str__(self):
        return str(self.codigo)

class YoutubeVideo(models.Model):
    url = models.CharField(max_length=500)
    descricao = models.TextField()

    def __str__(self):
        return self.url

class Aula(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    dia = models.DateField()
    objetivo = models.TextField()
    videos = models.ManyToManyField(YoutubeVideo)

    def __str__(self):
        return str(self.dia)


class PresencaDeAula(models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    aluno = models.ManyToManyField(Aluno)

    def __str__(self):
        return "{}: {}".format(self.aluno.nome, self.aula.nome)

class Prova(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    dia = models.DateField()

    def __str__(self):
        return "{}: {}".format(self.turma.codigo, self.dia)

class NotaDeProva(models.Model):
    prova = models.ForeignKey(Prova, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100, choices=TIPOS_DE_PROVA)
    nota = models.FloatField()
    aluno = models.ManyToManyField(Aluno)

    def __str__(self):
        return "{}: {} - {}".format(self.prova.dia, self.aluno.nome, self.nota)