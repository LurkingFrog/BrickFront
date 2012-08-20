from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext


def welcome(request):
    """
    This is the entry page
    """
    template = 'base.html'
    context = dict()

    return render(request, template, context)

