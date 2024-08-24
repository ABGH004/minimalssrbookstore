from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Author, Book

# Create your views here.


class AuthorListView(ListView):
    model = Author
    template_name = "author_list.html"
    context_object_name = "author_list"


class AuthorDetailView(DetailView):
    model = Author
    template_name = "author_detail.html"


class AuthorCreateView(CreateView):
    model = Author
    template_name = "author_new.html"
    fields = ["first_name", "last_name", "age", "identity_code"]


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = "author_edit.html"
    fields = ["first_name", "last_name", "age", "identity_code"]


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = "author_delete.html"
    success_url = reverse_lazy("author_list")


class AuthorSearchView(ListView):
    model = Author
    context_object_name = "author_list"
    template_name = "author_search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("result")
        return Author.objects.filter(
            Q(first_name__icontains=query)
            | Q(last_name__icontains=query)
            | Q(identity_code__icontains=query)
        )


class BookListView(ListView):
    model = Book

    template_name = "book_list.html"
    context_object_name = "book_list"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data["author_pk"] = self.kwargs["pk"]
        return data

    def get_queryset(self) -> QuerySet[Any]:
        return Book.objects.filter(author_id=self.kwargs["pk"])


class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        data = super().get_context_data(**kwargs)
        data["author_pk"] = self.kwargs["pk"]
        return data

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return Book.objects.get(author_id=self.kwargs["pk"], id=self.kwargs["pk2"])


class BookCreateView(CreateView):
    model = Book
    template_name = "book_new.html"
    fields = ["title", "release_date"]

    def form_valid(self, form):
        form.instance.author_id = self.kwargs["pk"]
        return super().form_valid(form)


class BookUpdateView(UpdateView):
    model = Book
    template_name = "book_edit.html"
    fields = ["title", "release_date"]

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return Book.objects.get(author_id=self.kwargs["pk"], id=self.kwargs["pk2"])


class BookDeleteView(DeleteView):
    model = Book
    template_name = "book_delete.html"
    # success_url = reverse_lazy("book_list")

    def get_success_url(self) -> str:
        return reverse_lazy(
            "book_list",
            kwargs={"pk": self.kwargs["pk"]},
        )

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        return Book.objects.get(author_id=self.kwargs["pk"], id=self.kwargs["pk2"])


class BookSearchView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "book_search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("result")
        return Book.objects.filter(Q(title__icontains=query))
