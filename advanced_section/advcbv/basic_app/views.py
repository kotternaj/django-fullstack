from django.shortcuts import render
from django.views.generic import View, TemplateView

class IndexView(TemplateView):  #inherit TemplateView
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION!'
        return context 

# class CBView(View):
#     def get(self,request):
#         return HttpResponse('CLASS BASED VIEW!')


# def index(request):
#     return render(request, 'index.html')