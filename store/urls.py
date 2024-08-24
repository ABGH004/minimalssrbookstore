from django.urls import path, include
from . import views

books_urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path(
        "<int:pk2>/",
        views.BookDetailView.as_view(),
        name="book_detail",
    ),
    path("new/", views.BookCreateView.as_view(), name="book_new"),
    path(
        "<int:pk2>/edit",
        views.BookUpdateView.as_view(),
        name="book_edit",
    ),
    path(
        "<int:pk2>/delete",
        views.BookDeleteView.as_view(),
        name="book_delete",
    ),
    path(
        "search/",
        views.BookSearchView.as_view(),
        name="book_search_results",
    ),
]
urlpatterns = [
    path("authors/", views.AuthorListView.as_view(), name="author_list"),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author_detail"),
    path("authors/new/", views.AuthorCreateView.as_view(), name="author_new"),
    path(
        "authors/<int:pk>/edit/", views.AuthorUpdateView.as_view(), name="author_edit"
    ),
    path(
        "authors/<int:pk>/delete/",
        views.AuthorDeleteView.as_view(),
        name="author_delete",
    ),
    path(
        "authors/search/",
        views.AuthorSearchView.as_view(),
        name="author_search_results",
    ),
    path("authors/<int:pk>/books/", include(books_urlpatterns)),
]
