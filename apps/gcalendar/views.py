from django.http import HttpResponse
from django.template import loader, Context, RequestContext
from django.utils import simplejson

from gcalendar.models import Calendar


def embed_calendar_html(request, slug=None, html=None):
    """
    This should build the iframe that contains the google
    calendar with all relevant options preset. This is going
    to be a composite of all the categories.

    TODO:
      switch settings by user
      change this to return JSON with the iframe as a field
      
    """
    template = 'gcalendar/embed_calendar.html'
    context = dict()
    response = {
        'html': None,
        'error_code': None,
    }
    error = ''

    try:
        context['calendar'] = Calendar.objects.get(slug=slug)
    
        if html:
            render(request, template, context)

        template = loader.get_template(template)
        context = Context(context)

        response = {'html': template.render(context)}

    except Exception as ex:
        response['error_code'] = 500
        response['html'] = ex.message
    
    return HttpResponse(
        simplejson.dumps(response),
        mimetype="application/json"
    )


# def category
