from django.shortcuts import redirect, render
from .models import Document
from .forms import DocumentForm
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy

class CreateFile(CreateView):
    model = Document
    form_class = DocumentForm
    template_name = "list.html"
    success_url = reverse_lazy('my-view')


class UpdateFile(UpdateView):
    model = Document
    form_class = DocumentForm
    template_name = "list.html"
    success_url = reverse_lazy('my-view')

class HomeView(ListView):
    model = Document
    template_name = "home.html"

# def my_view(request):
#     print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
#     message = 'Upload as many files as you want!'
#     # Handle file upload
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             newdoc = Document(docfile=request.FILES['docfile'])
#             newdoc.save()

#             # Redirect to the document list after POST
#             return redirect('my-view')
#         else:
#             message = 'The form is not valid. Fix the following error:'
#     else:
#         form = DocumentForm()  # An empty, unbound form

#     # Load documents for the list page
#     documents = Document.objects.all()

#     # Render list page with the documents and the form
#     context = {'documents': documents, 'form': form, 'message': message}
#     return render(request, 'list.html', context)
