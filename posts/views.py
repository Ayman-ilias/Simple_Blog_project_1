from django.shortcuts import render, redirect
from .import forms,models

def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
    else:
        post_form = forms.PostForm
    return render(request, 'post.html', {'form': post_form})

def edit_post(request,id):
    p=models.post.objects.get(pk=id)
    post_form = forms.PostForm(instance=p)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST,instance=p)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
    return render(request, 'post.html', {'form': post_form})

def delete_post(request,id):
    p=models.post.objects.get(pk=id)
    p.delete()
    return redirect('home')


