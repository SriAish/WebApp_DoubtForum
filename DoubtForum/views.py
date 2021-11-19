from django.shortcuts import render,redirect
from .models import * 
from .forms import * 
from django.contrib import messages
# Create your views here.
 
def home(request):
    doubts = Doubt.objects.all().order_by('-created_on')
    
    context = {
        "doubts": doubts,
    }

    return render(request, "home.html", context)
 
def add_doubt(request):
    form = DoubtForm()
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = DoubtForm(request.POST)
        if form.is_valid():
            doubt = Doubt.objects.create(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                link=form.cleaned_data["link"],
                title=form.cleaned_data["title"],
            )
            doubt.tags.set([form.cleaned_data["tag"]])
            doubt.save()
            return redirect('/')

    context ={
        "form": form,
        "tags": tags
    }

    return render(request,'addDoubt.html',context)


def tagged_doubts(request, tag):
    form = DoubtForm()
    doubts = Doubt.objects.filter(
        tags__name__contains=tag
    ).order_by(
        '-created_on'
    )
    context = {
        "tag": tag,
        "doubts": doubts,
        "form": form
    }
    return render(request, "home.html", context)

def doubt_complete(request, pk):
    doubt = Doubt.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                doubt=doubt
            )
            comment.save()

    comments = Comment.objects.filter(doubt=doubt)
    context = {
        "doubt": doubt,
        "comments": comments,
        "form": form,
    }

    return render(request, "doubtComplete.html", context)

def tag_list(request):
    tags = Tag.objects.all()
    context = {
        "tags": tags,
    }

    return render(request, "tagList.html", context)