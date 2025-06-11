from django import forms

class DateInput(forms.DateInput):
	input_type = 'date'

class RouteForm(forms.Form):
	date = forms.DateField(widget = DateInput())