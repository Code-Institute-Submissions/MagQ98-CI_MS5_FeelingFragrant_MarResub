from django.shortcuts import render
def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)

def internal_server_error_view(request, *args, **argv):
    return render(request, '500.html', status=500)