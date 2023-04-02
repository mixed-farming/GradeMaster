from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from .filters import ItemFilter
from .forms import ItemForm, Document
from .models import Item, Document

from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import DocumentForm

# Create your views here.
# Search list screen
class ItemFilterView(LoginRequiredMixin, FilterView):
    model = Item

    # Default sort order to newest
    queryset = Item.objects.all().order_by('-created_at')

    # django-filter settings
    filterset_class = ItemFilter
    strict = False

    # Number of items displayed per page
    paginate_by = 10

    # Save search criteria in session
    def get(self, request, **kwargs):
        if request.GET:
            request.session['query'] = request.GET
        else:
            request.GET = request.GET.copy()
            if 'query' in request.session.keys():
                for key in request.session['query'].keys():
                    request.GET[key] = request.session['query'][key]

        return super().get(request, **kwargs)


# Details screen
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item


# Registration screen
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')


# update screen
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')


# Delete screen
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('index')

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})

def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents': documents})

def download_document(request, id):
    document = get_object_or_404(Document, id=id)
    response = HttpResponse(document.file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
    return response

