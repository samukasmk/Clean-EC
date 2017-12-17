from django import forms
from ecweb.models import Aluno

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    alunos = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), required=True,
                                            queryset=Aluno.objects.all())


