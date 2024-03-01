from django import forms


class BuyForm(forms.Form):
    # it is not inheriting from forms.ModelForm
    confirmation = forms.CharField(label='confirmation',
                                   max_length=10)
