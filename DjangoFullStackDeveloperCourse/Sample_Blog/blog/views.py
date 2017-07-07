from django.shortcuts import render,get_object_or_404,redirect
###################################^^^^^^^^^^^^^^^^^^^^^^^^^^###
from django.utils import timezone

from django.views.generic import (TemplateView,CreateView,UpdateView,DeleteView,ListView,DetailView)

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

from blog import models as blogModels
from blog import forms as blogForms
# Create your views here.
# class
class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self):
        context = super(AboutView,self).get_context_data()
        context['title'] = 'About | '
        context['HeaderHeading'] = 'About'
        context['HeaderSubHeading'] = 'just another shit'

        return context
class PostListView(ListView):
    template_name = 'index.html'
    model =blogModels.Posts
    context_object_name = 'post_list'

    def get_context_data(self,**kwargs):
        context = super(PostListView,self).get_context_data(**kwargs)
        context['HeaderHeading'] = 'Diary'
        context['HeaderSubHeading'] = 'just another blog'
        return context

    def get_queryset(self):
        return blogModels.Posts.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')

class PostDetailView(DeleteView):
    template_name = 'post.html'
    context_object_name = 'post_detail'
    model = blogModels.Posts


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    form_class = blogForms.PostForm
    template_name = 'createPost.html'
    model = blogModels.Posts

class UpdatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    form_class = blogForms.PostForm
    # template_name = ''
    model = blogModels.Posts

class PostDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    form_class = blogForms.PostForm
    # template_name = ''
    model = blogModels.Posts
    success_url = reverse_lazy('homePage')

class DrafListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    model = blogModels.Posts
    template_name = 'drafts.html'
    context_object_name = 'drafts_list'

    def get_queryset(self):
        return blogModels.Posts.objects.filter(published_date__isnull = True).order_by('-published_date')

############################################
############################################
############################################
############################################

""" Function Based Views """

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(blogModels.Posts,pk=pk)
    if request.method == 'POST':
        form = blogForms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = blogForms.CommentForm()
    return render(request,'comment_form.html',{'form':form})

@login_required
def comment_approve(req,pk):
    comment = get_object_or_404(blogModels.Comments,pk=pk)
    comment.approve_comment()

    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(req,pk):
    comment = get_object_or_404(blogModels.Comments,pk=pk)
    post_pk = comment.post.pk
    comment.delete()

    return redirect('post_detail',pk = post_pk)


@login_required
def post_publish(req,pk):
    post = get_object_or_404(blogModels.Posts,pk=pk)
    post.publish()

    return redirect('post_detail',pk=post.pk)
