from django import forms
class BMIForm(forms.Form):
    weight=forms.FloatField(label='weight in kg',min_value=0,required=True)
    height=forms.FloatField(label="height in m's",min_value=0,required=True)
    