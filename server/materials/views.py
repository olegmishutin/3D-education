from django.shortcuts import render
from django.http import FileResponse
from .models import App, HandBook


def materials(request):
    apps = App.objects.all()
    handBooks = HandBook.objects.all()
    return render(request, 'materials.html', {'apps': apps, 'handBooks': handBooks})


def downloadBook(request, pk):
    book = HandBook.objects.get(pk=pk)
    return FileResponse(open(book.file.path, 'rb'), as_attachment=True)
