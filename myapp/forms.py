from django import forms
from .models import Client, Property

class ClientUpdateForm(forms.ModelForm):
	class Meta:
		model = Client
		# fields = ('firstname','lastname','mobile','email','agent', 'follow_up_date' ,'remarks')
		fields = ('firstname','lastname','mobile', 'address','email', 'city', 'state', 'occupation' ,'agent', 'follow_up_date' ,'remarks','contacted')

class PropertyUpdateForm(forms.ModelForm):
	class Meta:
		model = Property
		fields = ('banner','property_name','property_type','area','price', 'no_of_bedrooms' ,'no_of_bathrooms','city', 'state')

