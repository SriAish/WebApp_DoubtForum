from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .models import *
from .forms import *

def home(request):
    """
    Display all instances of :model:`DoubtForum.Doubt`.

    **Context**

    ``doubts``
        Objects in doubts are an instance of :model:`DoubtForum.Doubt`.

    **Template:**

    :template:`templates/home.html`
    """
    doubts = Doubt.objects.all().order_by('-created_on')

    context = {
        "doubts": doubts,
    }

    return render(request, "home.html", context)


@login_required(login_url='/login')
def add_doubt(request):
    """
    Display an individual :form:`DoubtForum.DoubtForm`.
    Creates a new :model:`DoubtForum.Doubt` on POST.

    **Context**

    ``form``
        An instance of :form:`DoubtForum.DoubtForm`.

    **Template:**

    :template:`templates/addDoubt.html`
    """
    form = DoubtForm()

    if request.method == 'POST':
        form = DoubtForm(request.POST)
        if form.is_valid():
            doubt = Doubt.objects.create(
                    author=request.user,
                    body=form.cleaned_data["body"],
                    link=form.cleaned_data["link"],
                    title=form.cleaned_data["title"],
                    subject=form.cleaned_data["tag"]
                )
            if(form.cleaned_data["link"] == ""):
                doubt.link = None
            doubt.save()
            return redirect('/')

    context = {
        "form": form
    }

    return render(request, 'addDoubt.html', context)


def tagged_doubts(request, tag):
    """
    Display all instances od :model:`DoubtForum.Doubt` with :model:`DoubtForum.Doubt.subject` = tag.

    **Context**

    ``doubts``
        Objects in doubts are an instance of :model:`DoubtForum.Doubt`.

    **Template:**

    :template:`templates/searchResults.html`
    """
    doubts = Doubt.objects.filter(
        subject__name__contains=tag
    ).order_by(
        '-created_on'
    )
    context = {
        "query": tag,
        "doubts": doubts
    }
    return render(request, "searchResults.html", context)


def doubt_complete(request, pk):
    """
    Display an individual :model:`DoubtForum.Doubt`.
    Display all :model:`DoubtForum.Comment` relate to the individual :model:`DoubtForum.Doubt`.
    Display an individual :form:`DoubtForum.CommentForm`.
    Creates a new :form:`DoubtForum.Comment` on POST.

    **Context**

    ``doubt``
        An instance of :model:`DoubtForum.Doubt`.

    ``comments``
        Objects in comments are an instance of :model:`DoubtForum.Doubt`.

    ``form``
        An instance of :form:`DoubtForum.CommentForm`.

    **Template:**

    :template:`templates/doubtComplete.html`
    """
    doubt = Doubt.objects.get(pk=pk)

    form = CommentForm()
    comments = Comment.objects.filter(doubt=doubt).order_by('-created_on')
    context = {
        "doubt": doubt,
        "comments": comments,
        "form": form,
    }
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=request.user,
                body=form.cleaned_data["body"],
                doubt=doubt
            )
            comment.save()
            return render(request, "doubtComplete.html", context)

    return render(request, "doubtComplete.html", context)


def subject_list(request):
    """
    Display all instances of :model:`DoubtForum.Subject`.

    **Context**

    ``doubts``
        Objects in doubts are an instance of :model:`DoubtForum.Subject`.

    **Template:**

    :template:`templates/subjectList.html`
    """
    tags = Subject.objects.all()
    context = {
        "tags": tags,
    }

    return render(request, "subjectList.html", context)


def search_doubt(request):
    """
    Display an individual :form:`DoubtForum.SearchForm`.
    Redirects to :views:`DoubtForum.searched_doubts` on GET.

    **Context**

    ``form``
        An instance of :form:`DoubtForum.SearchForm`.

    **Template:**

    :template:`templates/search.html`
    """
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
    """
    Display all instances of :model:`DoubtForum.Doubt` based on the search query.

    **Context**

    ``doubts``
        Objects in doubts are an instance of :model:`DoubtForum.Doubt`.

    **Template:**

    :template:`templates/searchResults.html`
    """
    search_type = request.session.get('search_type')
    search_query = request.session.get('search_query')
    if search_type == "Author":
        doubts = Doubt.objects.filter(
            author__username__contains=search_query
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
            subject__name__contains=search_query
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


def doubt_sessions(request):
    """
    Display all instances of :model:`DoubtForum.DoubtSession`.

    **Context**

    ``doubts``
        Objects in doubts are an instance of :model:`DoubtForum.DoubtSession`.

    **Template:**

    :template:`templates/schedule.html`
    """
    sessions = DoubtSession.objects.all().order_by('-scheduled_for')
    context = {
        "sessions": sessions,
    }

    return render(request, "schedule.html", context)


@login_required(login_url='/login')
def user_doubts(request):
    doubts = Doubt.objects.filter(
            author=request.user
        ).order_by(
            '-created_on'
        )

    context = {
        "query": request.user.username,
        "doubts": doubts
    }
    return render(request, "searchResults.html", context)


class sign_up_view(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
