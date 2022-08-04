from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.urls import reverse_lazy
from django.db import models
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from .forms import CommentForm
from .models import books
from django.shortcuts import get_object_or_404
# Create your views here.
class BookListView(generic.ListView):
    model = books
    paginate_by = 2
    template_name = 'books/books_list.html'
    context_object_name='books'

# class BookDetailView(generic.DetailView):
#     model = books
#     template_name = "books/detail_view.html"
@login_required
def book_detail_view(request,pk):
    book=get_object_or_404(books,pk=pk)
    book_comments=book.comments.all()
    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
           new_comment= comment_form.save(commit=False)
           new_comment.book=book
           new_comment.author=request.user
           new_comment.save()
           comment_form = CommentForm()

    else:
        comment_form=CommentForm()
    return render(request,"books/detail_view.html",{'book':book,'comments':book_comments,'comment_form':comment_form})

class BookCreationView(LoginRequiredMixin,generic.CreateView):
    model = books
    fields = ['title','author','content','price','cover']
    template_name = "books/book_new.html"


class BookUpdateView(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    model = books
    fields = ['title','author','content','cover']
    template_name = "books/book_update.html"

    def test_func(self):
      obj=self.get_object()
      return obj.user==self.request.obj
class BookDeleteView(LoginRequiredMixin,generic.DetailView):
    model = books
    template_name = "books/book_delete.html"
    succuss_url=reverse_lazy('Book_List')
