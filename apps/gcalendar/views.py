# Create your views here.

def display(request):
    """
    This shows the base calendar.

    TODO: Add in per user views
    """
    template = 'gcalendar/gcalendar.html'
    context = dict()

    return render(request, template, context)
