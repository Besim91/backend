from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from .dummy_data import gadgets
import json
from django.utils.text import slugify
from django.urls import reverse
from django.views import View
from django.views.generic.base import RedirectView


def start_page_view(request):
    return render(request, 'tech_gadgets/test.html', {'gadget_list': gadgets})

class RedirectToGagedsView(RedirectView):
    pattern_name = "gadget_slug_url"
    
    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(gadgets[kwargs.get("gadget_id",0)]["name"])
        new_kwarg = {"gadget_slug": slug}
        return super().get_redirect_url(*args, **new_kwarg)


def single_gadgeds_int_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse("gadget_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponse("not found by me")



# class GadgetsView(View):
#     def get(self,request,gadget_slug):
#         gadget_match = None
#         for gadget in gadgets:
#             if slugify(gadget["name"]) == gadget_slug:
#                 gadget_match = gadget
                
#         if gadget_match:        
#             return JsonResponse(gadget_match)
#         raise Http404()
    
#     def post(self, request,*args, **kwargs):
#         try:
#             data = json.loads(request.body)
#             print(f"received data: {data["test"]}")
#             return JsonResponse({"response": "Das wahr was"})        
#         except:
#             return JsonResponse({"response": "Das wahr wohl nix"})

class GadgetsView(View):
    def get(self, request, gadget_slug=None):  # Parameter optional gemacht
        if gadget_slug is None:
            # Fall: Aufruf ohne Slug (z. B. /gadget/) → Liste aller Gadgets
            return JsonResponse({'gadgets': gadgets})
        
        # Fall: Aufruf mit Slug (z. B. /gadget/iphone-15/) → Einzelnes Gadget
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget
                
        if gadget_match:        
            return JsonResponse(gadget_match)
        raise Http404()
    
    # post-Methode bleibt unverändert
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            print(f"received data: {data['test']}")
            return JsonResponse({"response": "Das wahr was"})        
        except:
            return JsonResponse({"response": "Das wahr wohl nix"})