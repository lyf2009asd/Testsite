from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
# Create your views here.


def posts_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request,"blogs/create.html", context)


def posts_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "blogs/detail.html", context)

def posts_list(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 10)  # Show 25 contacts per page
    page_request_var = 'bloglist'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list":queryset,
        "title": "list",
        "page_request_var": page_request_var,
    }
    return render(request, "blogs/home.html", context)


def posts_update(request, id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,request.FILES or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Edited")

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "blogs/create.html", context)


def posts_delete(request, id):
    instance = get_object_or_404(Post, id=id)

    messages.success(request, "Successfully Deleted")
    return redirect("posts_list")
