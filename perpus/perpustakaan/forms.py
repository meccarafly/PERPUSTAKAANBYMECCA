from django import forms
from django.forms import ModelForm, fields, widgets
from django import forms
from perpustakaan.models import Buku


class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = '__all__'

        widgets = {
            'judul' : forms.TextInput({'class':'form-control'},),
            'penulis' : forms.TextInput({'class':'form-control'},),
            'penerbit' : forms.TextInput({'class':'form-control'},),
            'jumlah' : forms.NumberInput({'class':'form-control'},),
            'nopustaka' : forms.NumberInput({'class':'form-control'},),

        }