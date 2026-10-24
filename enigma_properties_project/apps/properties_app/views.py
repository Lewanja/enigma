from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from enigma_properties_project.apps.properties_app.forms import AddPropertyForm
from enigma_properties_project.apps.properties_app.models import Property
from django.http import HttpResponse, Http404

# Create your views here.
from django.views.generic import CreateView


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')

def list_properties(request):
    existing_property = Property.objects.all()
    return render(request, 'view_property/list_property.html', {'property': existing_property})


def view_properties(request, property_id):
    try:
        property_name = Property.objects.get(property_id=property_id)
    except Property.DoesNotExist:
        raise Http404("Property does not exist")

    return render(request, 'view_property/view_property.html', {"property_name": property_name})

def about(request):
    abt = "we are buyers and sellers of land and houses, we also sell property on behalf of our clients."
    return render(request, "about.html", {"abt":abt})



class AddProperty(LoginRequiredMixin, CreateView):
    model = Property
    template_name = 'upload_property/upload_property_form.html'
    fields = '__all__'
    success_url = reverse_lazy('index')

    def test_func(self):
        # Check if the user is a superuser
        return self.request.user.is_superuser

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, "You need to have superuser permission to access this page")
            return redirect('/')
        else:
            messages.error(self.request, "You need to login to access this page")
            return redirect('/')

    def form_valid(self, form):
        messages.success(self.request, "POST added successfully")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error in your submission")
        return super().form_invalid(form)
