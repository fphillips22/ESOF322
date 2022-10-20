from django.urls import reverse_lazy
from .models import Data
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


# Create your views here.

class DataListView(ListView):
    model = Data
    template_name = "add url stuff"
    context_object_name = "add list stuff here"


class DataCreateView(CreateView):
    model = Data
    template_name = "add url stuff"
    fields = ["title", "description"]
    success_url = reverse_lazy("add crap here")


class DataUpdateView(UpdateView):
    model = Data
    # template_name = ""
    fields = ["title", "description"]


class DataDeleteView(DeleteView):
    model = Data
    template_name = "more url thing"
    success_url = reverse_lazy("list thingy")