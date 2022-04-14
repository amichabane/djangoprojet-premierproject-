from django.shortcuts import render, redirect
from .models import Notes
from .forms import NotesForm
from django.contrib import messages
from User.models import CustomUser as User


# Create your views here.


def index(request):
    return render(request, 'index.html')


def new_note(request):
    form = NotesForm()
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "update.html", {"form": form})


def note_detail(request, pk):
    note = Notes.objects.get(id=pk)
    form = NotesForm(instance=note)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "update.html", {"note": note, "form": form})


# def delete_note(request, pk):
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


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    user = User.objects.get(id=request.user.id)
    signup = User.objects.get(username=user)
    totalnotes = Notes.objects.filter(username=user).count()
    return render(request, 'dashboard.html', locals())


def viewNotes(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    user = User.objects.get(id=request.user.id)
    signup = User.objects.get(username=user)
    notes = Notes.objects.filter(signup=user)
    return render(request, 'viewNotes.html', locals())


def deleteNotes(request, pid):
    if not request.user.is_authenticated:
        return redirect('signin')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('viewNotes')


def addNotes(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    user = User.objects.get(id=request.user.id)
    signup = User.objects.get(username=user)

    error = ""
    if request.method == "POST":
        form = NotesForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'addNotes.html', locals())


def editNotes(request, pid):
    if not request.user.is_authenticated:
        return redirect('signin')
    notes = Notes.objects.get(id=pid)
    if request.method == "POST":
        title = request.POST['Title']
        content = request.POST['Content']

        notes.Title = title
        notes.Content = content

        try:
            notes.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'editNotes.html', locals())
