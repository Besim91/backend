from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
from .dummy_data import gadgets
import json
from django.utils.text import slugify
from django.urls import reverse
from django.views import View


def start_page_view(request):
    return HttpResponse("Das hat gut geklappt!")


def single_gadgeds_int_view(request, gadget_id):
    if len(gadgets) > gadget_id:
        new_slug = slugify(gadgets[gadget_id]["name"])
        new_url = reverse("gadget_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponse("not found")



class GadgetsView(View):
    def get(self,request,gadget_slug):
        gadget_match = None
        for gadget in gadgets:
            if slugify(gadget["name"]) == gadget_slug:
                gadget_match = gadget
                
        if gadget_match:        
            return JsonResponse(gadget_match)
        raise Http404()
    
    def post(self, request,*args, **kwargs):
        try:
            data = json.loads(request.body)
            print(f"received data: {data["test"]}")
            return JsonResponse({"response": "Das wahr was"})        
        except:
            return JsonResponse({"response": "Das wahr wohl nix"})
