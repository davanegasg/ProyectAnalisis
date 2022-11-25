from django.conf import settings

def apps_processors(request):
    ctx = {}

    ctx['url_base'] = settings.BASE_URL

    return ctx