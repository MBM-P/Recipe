from django import forms
from notes.models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['valeur']
        widgets = {
            'valeur': forms.NumberInput(attrs={ 'min': 0, 'max': 5, 'step': 1,'style': 'width: 55px;',}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['valeur'].label = "Note (sur 5)"
        self.fields['valeur'].widget.attrs.update({
            'class': 'form-control',
        })
