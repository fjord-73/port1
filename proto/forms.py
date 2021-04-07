from django import forms
from .models import Rank, Message
class HelloForm(forms.ModelForm):
    class Meta:
        model = Rank
        fields = ['name','point','datepoint']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'point': forms.NumberInput(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control'}),
        }

class FindForm(forms.Form):
    find = forms.CharField(label='find', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))

class CheckForm(forms.Form):
    

    str = forms.CharField(label='string', widget=forms.TextInput(attrs={'class':'form-control'}))
    def clean(self):
        cleaned_data = super().clean()
        str = cleaned_data['str']
        if (str.lower().startswith('no')):
            raise forms.ValidationError('真壁瑞希')

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title','content','rank']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control form-control-sm'}),
            'content': forms.Textarea(attrs={'class':'form-control form-control-sm', 'rows':2}),
            'rank': forms.Select(attrs={'class':'form-control form-control-sm'}),

        }