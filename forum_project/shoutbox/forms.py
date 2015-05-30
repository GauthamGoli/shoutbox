from django import forms
from shoutbox.models import Post

class PostForm(forms.ModelForm):
	print dir(forms)
	message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'5'}))

	class Meta:
		model = Post
		fields = ('message',)