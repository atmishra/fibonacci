from django import forms


class InputForm(forms.Form):
    n = forms.IntegerField(min_value=1, max_value=10000, required=True,
                           label='Enter the value of n')
