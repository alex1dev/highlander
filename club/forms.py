from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
import datetime 


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'password')

edata = ""
ddata = ""

class SelEntForm(forms.Form):
	entrance_date = forms.DateField(help_text="Enter an entrance date, please.")
	
	def clean_entrance_date(self):
		global edata; 
		edata = self.cleaned_data['entrance_date']
	
		if edata < datetime.date.today():
			raise ValidationError(_('Please enter a valid Date '))

		if edata > datetime.date.today() + datetime.timedelta(weeks=4):
			raise ValidationError(_('Please enter a valid Date'))

		return edata

class SelDepForm(forms.Form):
	departure_date = forms.DateField(help_text="Enter a departure date, please.")

	def clean_departure_date(self):
		global ddata;
		global edata;
		ddata = self.cleaned_data['departure_date']

		if ddata < edata:
			raise ValidationError(_('Please enter a valid Date'))

		if ddata > edata + datetime.timedelta(weeks=6):
			raise ValidationError(_('Please enter a valid Date'))

		return ddata