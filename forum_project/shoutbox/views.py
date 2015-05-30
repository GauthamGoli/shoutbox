from django.shortcuts import render
from django.http import HttpResponseRedirect
from shoutbox.models import Post
from shoutbox.forms import PostForm

def index(request):
	context_dict={}
	form = PostForm()
	post_list = Post.objects.order_by('-datetime')
	context_dict.update({'posts':post_list,'form':form})

	return render(request,'shoutbox/index.html',context_dict)

def submit(request):
	if request.method == 'POST':
		form = PostForm(request.POST)
		#context_dict={'form':form}
		if form.is_valid():
			form.save(commit=True)
			return HttpResponseRedirect('/shoutbox/')
		else:
			print form.errors
