from django import forms
from.models import Datasample
from django.contrib.auth.forms import AuthenticationForm
class ConectForm(forms.Form):
    subject = forms.CharField(label='件名', max_length=10)
    name = forms.CharField(label='name')
    mail = forms.EmailField(label='mail', help_text="※ご確認のうえ、正しく入力してください")
    text = forms.CharField(label='text',widget=forms.Textarea)

class SearchForm(forms.Form):
    search = forms.CharField(label='検索', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
class Add(forms.ModelForm):

    class Meta:
        model = Datasample
        fields = ('name',
                  'gender',
                  'birthday')
        
        labels = {
            'name':'comment',
            'gender':'check',
            'birthday':'day',
        }
class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        