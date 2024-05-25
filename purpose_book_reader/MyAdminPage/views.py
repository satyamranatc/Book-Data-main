from django.shortcuts import render
from books.models import Book


# Create your views here.
def AdminPage(request):
    return render(request, 'AdminPage.html')

def SubmitBook(request):
    if(request.method == 'POST'):
        Name = request.POST.get('BookName')
        BookCover = request.FILES.get('BookCover')
        BookPdf = request.FILES.get('BookPdf')
        print(Name, BookCover, BookPdf)
        Book.objects.create(name=Name, cover_image=BookCover, pdf=BookPdf)
    return render(request, 'AdminPage.html')