from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.http import HttpResponse
from .forms import *


def inserir(request):
    if request.method == "GET":
        form_responsavel = ResponsavelFamiliarForm()
        form_membro_familiar_factory = inlineformset_factory(ResponsavelFamiliar, MembroFamiliar, form=MembroFamiliarForm)
        form_membro_familiar = form_membro_familiar_factory()
        context = {
            'form_responsavel': form_responsavel,
            'form_membro_familiar': form_membro_familiar
        }
        return render(request, 'cadastro/cadastro.html', context)

    if request.method == "POST":
        form_responsavel = ResponsavelFamiliarForm(request.POST)
        form_membro_familiar_factory = inlineformset_factory(ResponsavelFamiliar, MembroFamiliar, form=MembroFamiliarForm)
        form_membro_familiar = form_membro_familiar_factory(request.POST)
        if form_responsavel.is_valid() and form_membro_familiar.is_valid():
            responsavel_familiar = form_responsavel.save()
            form_membro_familiar.instance = responsavel_familiar
            form_membro_familiar.save()
            return HttpResponse('Registrado')