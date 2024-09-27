from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from .models import Profile
from .forms import Profile_creation



from django.core.files.base import ContentFile
import base64
from django.http import HttpResponseRedirect


# Create your views here.
class IndexView(CreateView):
    form_class = Profile_creation
    template_name = 'first_app/index.html'
    success_url = '/'

    def form_valid(self, form):
        cropped_image = self.request.POST.get('cropped_image')
        if cropped_image:
            format, imgstr = cropped_image.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='profile_pic.' + ext)
            form.instance.image = data
        return super().form_valid(form)


