from django.shortcuts import redirect
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

class RegisterView(CreateView):
    template_name = "registration/register.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        return redirect('login')
    
def index(request):
    return HttpResponse("hola")
