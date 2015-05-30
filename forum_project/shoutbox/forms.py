from django import forms
from shoutbox.models import Post

class PostForm(forms.ModelForm):
	message = forms.CharField(max_length=200)

	class Meta:
		model = Post
		fields = ('message',)