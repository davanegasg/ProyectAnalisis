from django.views.generic import TemplateView

class HomeTemplateView(TemplateView):
    template_name = 'home/index.html'
    
class TestWithValuesTemplateView(TemplateView):
    template_name = 'home/test_with_values.html'
