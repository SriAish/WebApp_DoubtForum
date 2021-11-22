from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home(request):

    """Renders the home page which has all doubts."""
    doubts = Doubt.objects.all().order_by('-created_on')

    context = {
        "doubts": doubts,
    }

    return render(request, "home.html", context)


def add_doubt(request):
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
            if(form.cleaned_data["link"] == ""):
                doubt.link = None
            doubt.tags.set([form.cleaned_data["tag"]])
            doubt.save()
            return redirect('/')

    context = {
        "form": form
    }

    return render(request, 'addDoubt.html', context)


def tagged_doubts(request, tag):
    doubts = Doubt.objects.filter(
        tags__name__contains=tag
    ).order_by(
        '-created_on'
    )
    context = {
        "query": tag,
        "doubts": doubts
    }
    return render(request, "searchResults.html", context)


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

    comments = Comment.objects.filter(doubt=doubt).order_by('-created_on')
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


def search_doubt(request):
    form = SearchForm()

    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            request.session['search_type'] = form.cleaned_data['search_type']
            request.session['search_query'] = form.cleaned_data['search_query']
            return redirect('searched_doubts')
    context = {
        "form": form
    }

    return render(request, 'search.html', context)


def searched_doubts(request):
    search_type = request.session.get('search_type')
    search_query = request.session.get('search_query')
    if search_type == "Author":
        doubts = Doubt.objects.filter(
            author__contains=search_query
        ).order_by(
            '-created_on'
        )
    elif search_type == "Title":
        doubts = Doubt.objects.filter(
            title__contains=search_query
        ).order_by(
            '-created_on'
        )
    elif search_type == "Subject":
        doubts = Doubt.objects.filter(
            tags__name__contains=search_query
        ).order_by(
            '-created_on'
        )
    else:
        doubts = []

    context = {
        "query": search_query,
        "doubts": doubts
    }
    return render(request, "searchResults.html", context)
