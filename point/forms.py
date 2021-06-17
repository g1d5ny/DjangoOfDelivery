from django import forms


class AddPointForm(forms.Form):
    code = forms.CharField(label='Your Point Code')
