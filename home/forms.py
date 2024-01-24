from django import forms

class CalculatorForm(forms.Form):
    num1 = forms.FloatField()
    num2 = forms.FloatField()
    opt = forms.ChoiceField(choices=[('+', '+'), ('-', '-'), ('*', '*'), ('/', '/')])
