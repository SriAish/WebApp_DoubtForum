from django.shortcuts import render,redirect
from .models import * 
from .forms import * 
# Create your views here.
 
def home(request):
    doubts = Doubt.objects.all().order_by('-created_on')
    tags = Tag.objects.all()
    form = DoubtForm()
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
    context = {
        "doubts": doubts,
        "tags": tags,
        "form": form
    }
    return render(request, "home.html", context)
 
def blog_category(request, tag):
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

def blog_detail(request, pk):
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

    return render(request, "home.html", context)