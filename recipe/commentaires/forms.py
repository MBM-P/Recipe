from django import forms
from commentaires.models import Commentaire

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contenu'].label = ""
        self.fields['contenu'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Entrez votre commentaire ici',
        })
