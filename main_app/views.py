from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Cat, Toy
from .forms import FeedingForm


# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

class CatList(LoginRequiredMixin, ListView):
  model = Cat

  def get_queryset(self):
     return Cat.objects.filter(user=self.request.user)

class CatDetail(LoginRequiredMixin, DetailView):
  model = Cat

  def get_context_data(self, **kwargs):
     context = super().get_context_data(**kwargs)
     toys_cat_doesnt_have = Toy.objects.exclude(id__in = self.object.toys.all().values_list('id'))
     context['feeding_form'] = FeedingForm()
     context['toys'] = toys_cat_doesnt_have
     return context


class CatCreate(LoginRequiredMixin, CreateView):
  model = Cat
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
     form.instance.user = self.request.user
     return super().form_valid(form)

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['breed', 'description', 'age']

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = reverse_lazy('cat-index')

@login_required
def add_feeding(request, pk):
  form = FeedingForm(request.POST)
  if form.is_valid():
      new_feeding = form.save(commit=False)
      new_feeding.cat_id = pk
      new_feeding.save()
    
  return redirect('cat-detail',pk=pk)


class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy 

class ToyDetail(LoginRequiredMixin, DetailView):
   model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
   model = Toy
   fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
   model = Toy
   success_url = reverse_lazy('toy-index')

@login_required
def associate_toy(request, cat_id, toy_id):
   Cat.objects.get(id=cat_id).toys.add(toy_id)
   return redirect('cat-detail', pk=cat_id)

@login_required
def remove_toy(request, cat_id, toy_id):
  cat = Cat.objects.get(id=cat_id)
  cat.toys.remove(toy_id)
  return redirect('cat-detail', pk=cat_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
 


