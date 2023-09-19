from django.shortcuts import render
from django.views.generic import CreateView

from zayavki.models import Zayavka


class ZayavkaViews(CreateView):
    template_name = 'contacts.html'
    model = Zayavka
    fields = ('name', 'email', 'question')
    success_url = '/'


def contacts_views(request):
    return render(request, 'contacts.html')