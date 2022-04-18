from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Notes
from .forms import NotesForm
from django.contrib import messages
from User.models import User as User


# Create your views here.


def index(request):
    return render(request, 'index.html')


def note_detail(request, pk):
    note = Notes.objects.get(id=pk)
    form = NotesForm(instance=note)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "update.html", {"note": note, "form": form})


def delete_note(request, pk):
    note = Notes.objects.get(id=pk)
    form = NotesForm(instance=note)
    if request.method == 'POST':
        note.delete()
        messages.info(request, "The note has been deleted")
    return render(request, "delete.html", {"note": note, "form": form})


def search_page(request):
    if request.method == 'POST':
        search_text = request.POST['search']
        notes = Notes.objects.filter(title__icontains=search_text) | Notes.objects.filter(
            description__icontains=search_text)
        # if notes is None:
        #     messages.info(request, "Note not found")
        return render(request, "search.html", {"notes": notes})

@login_required
def dashboard(request):
    user = User.objects.get(id=request.user.id)
    signup = User.objects.get(email=user)
    totalnotes = Notes.objects.count()
    return render(request, 'dashboard.html', locals())

@login_required
def viewNotes(request):
    user = User.objects.get(id=request.user.id)
    signup = User.objects.get(email=user)
    notes = Notes.objects.filter(user=signup)
    return render(request, 'viewNotes.html', locals())


# def deleteNotes(request, pid):
#     if not request.user.is_authenticated:
#         return redirect('signin')
#     notes = Notes.objects.get(id=pid)
#     notes.delete()
#     return redirect('viewNotes')


@login_required
def addNotes(request):
    error = ""
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save
    return render(request, 'addNotes.html', locals())

@login_required
def editNotes(request, pid):
    notes = Notes.objects.get(id=pid)
    if request.method == "POST":
        title = request.POST['Title']
        content = request.POST['Content']

        notes.Title = title
        notes.Content = content

    return render(request, 'editNotes.html', locals())
