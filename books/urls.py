from django.urls import path
from .views import BookListView,book_detail_view,BookCreationView,BookUpdateView,BookDeleteView
urlpatterns = [
    path('',BookListView.as_view(),name='Book_List'),
    path('<int:pk>/',book_detail_view,name="book_detail"),
    path('new/', BookCreationView.as_view(), name='Book_new'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='Book_update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='Book_delete'),

]