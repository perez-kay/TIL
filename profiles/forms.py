from django.forms import ModelForm, CharField, TextInput, Textarea
from profiles.models import Profile

class ProfileUpdateForm(ModelForm):
	first_name = CharField(max_length=32, required=False,widget=
				TextInput(attrs={
				'class': 'form-control',
				'style': 'max-width: 300px;'
			}))
	last_name = CharField(max_length=32, required=False,widget=
				TextInput(attrs={
				'class': 'form-control',
				'style': 'max-width: 300px;'
			}))
	class Meta:
		model = Profile
		fields = ['profile_picture', 'bio', 'banner']
		widgets = {
			'bio': Textarea(attrs={
				'class': 'form-control',
				'rows': '3',
				'style': 'max-width: 500px;'
			})
		}

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['first_name'].initial = self.instance.user.first_name
		self.fields['last_name'].initial = self.instance.user.last_name