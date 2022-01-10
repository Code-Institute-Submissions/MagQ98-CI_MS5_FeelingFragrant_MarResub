from django.shortcuts import render
import logging

# Create your views here.


def index(request):
    """ A view to return the index page """

    logger = logging.getLogger(__name__)
    logger.info("calling home")
    return render(request, 'home/index.html')
