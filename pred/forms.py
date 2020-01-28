from django import forms

class restrev(forms.Form):
	review = forms.CharField(label="Review", max_length=200)