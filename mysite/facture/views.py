#coding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View

from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

#from weasyprint import HTML
from django.conf import settings
from easy_pdf.views import PDFTemplateView

from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context

from .forms import PrestataireForm, ClientForm, FactureForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from bootstrap_datepicker_plus import DatePickerInput

from facture.models import Facture
from django.urls import reverse_lazy

from .models import Prestataire
from .models import Client
from .models import Facture
# from .models import Image




@login_required (redirect_field_name='my_redirect_field')
def prestataire(request):
    return render(request=request,
                  template_name="prestataire_list.html",
                  context={"prestataires": Prestataire.objects.all})

@login_required
def client(request):
    return render(request=request,
                  template_name="client_list.html",
                  context={"clients": Client.objects.all})

@login_required
def facture(request):
    return render(request=request,
                  template_name="facture_list.html",
                  # ordering = [-Facture.ref_fact],
                  # https://simpleisbetterthancomplex.com/article/2017/03/21/class-based-views-vs-function-based-views.html
                  context={"factures": Facture.objects.all})






"""CREATION FICHE FACTURE ET AFFICHAGE SUCCESS"""

class FactureCreate(CreateView):
    model = Facture
    #fields = '__all__'
    form_class = FactureForm

    def get_form(self):
        form = super().get_form()
        form.fields['date_debut'].widget = DatePickerInput().start_of('facture date')
        form.fields['date_echeance'].widget = DatePickerInput().end_of('facture date')
        form.fields['date_prestation'].widget = DatePickerInput().end_of('facture date')
        
        return form
      

class FactureView(DetailView):
    model = Facture



"""EDITER ET EFFACER FACTURE"""

class FactureUpdate(UpdateView):
    model = Facture
    fields = "__all__"



class FactureDelete(DeleteView):
    model = Facture
    success_url = reverse_lazy('facture_list')






"""CREATION FICHE CLIENT ET AFFICHAGE SUCCESS"""

class ClientCreate(CreateView):
    model = Client
    fields = '__all__'

class ClientView(DetailView):
    model = Client


"""EDITER ET EFFACER CLIENT"""

class ClientUpdate(UpdateView):
    model = Client
    fields = '__all__'

class ClientDelete(DeleteView):
    model = Client
    success_url = reverse_lazy('client_list')




"""CREATION FICHE PRESTATAIRE ET AFFICHAGE SUCCESS"""

class PrestataireCreate(CreateView):
    model = Prestataire
    fields = '__all__'

class PrestataireView(DetailView):
    model = Prestataire


"""EDITER ET EFFACER PRESTATAIRE"""

class PrestataireUpdate(UpdateView):
    model = Prestataire
    fields = '__all__'

class PrestataireDelete(DeleteView):
    model = Prestataire
    success_url = reverse_lazy('prestataire_list')



""" CREATION DU MODELE PDF"""

class HelloPDFView(PDFTemplateView):
    template_name = 'facture_detail_PDF.html'
    base_url = 'file://' + settings.STATIC_ROOT
    download_filename = 'hello.pdf'

    def get_context_data(self, **kwargs):
        return super(HelloPDFView, self).get_context_data(
            pagesize='A4',
            title='Hi there!',

            **kwargs
       )
