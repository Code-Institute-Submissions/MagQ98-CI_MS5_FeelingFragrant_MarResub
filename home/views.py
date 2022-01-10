from django.shortcuts import render
import logging

# Create your views here.


def index(request):
    """ A view to return the index page """

    logging.getLogger('gunicorn.error')
    logger.error("calling home")
    return render(request, 'home/index.html')
