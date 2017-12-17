from django.contrib import admin
from ecweb.models import Aluno, Professor, Turma, YoutubeVideo, Aula, PresencaDeAula, Prova, NotaDeProva

class AlunoAdmin(admin.ModelAdmin):
    pass


class ProfessorAdmin(admin.ModelAdmin):
    pass


class TurmaAdmin(admin.ModelAdmin):
    pass


class YoutubeVideoAdmin(admin.ModelAdmin):
    pass


class AulaAdmin(admin.ModelAdmin):
    pass


class PresencaDeAulaAdmin(admin.ModelAdmin):
    pass


class ProvaAdmin(admin.ModelAdmin):
    pass


class NotaDeProvaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(YoutubeVideo, YoutubeVideoAdmin)
admin.site.register(Aula, AulaAdmin)
admin.site.register(PresencaDeAula, PresencaDeAulaAdmin)
admin.site.register(Prova, ProvaAdmin)
admin.site.register(NotaDeProva, NotaDeProvaAdmin)