from django.shortcuts import render_to_response


def index(request):
    return render_to_response("pages/html/index.html",
                              {},
                              context_instance=RequestContext(request))


def about(request):
    return render_to_response("pages/html/about.html",
                              {},
                              context_instance=RequestContext(request))


def terms(request):
    return render_to_response("pages/html/terms.html",
                              {},
                              context_instance=RequestContext(request))