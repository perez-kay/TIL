from django.forms import ModelForm, CharField
from profiles.models import Profile

class ProfileUpdateForm(ModelForm):
	first_name = CharField(max_length=32, required=False)
	last_name = CharField(max_length=32, required=False)
	class Meta:
		model = Profile
		fields = ['profile_picture', 'bio', 'banner']