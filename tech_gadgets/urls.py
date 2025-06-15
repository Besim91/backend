from django.urls import path
from .views import start_page_view, single_gadgeds_int_view, single_gadgeds_view


urlpatterns = [
    path('', start_page_view),
    path('gadget/', single_gadgeds_view),
    path('gadget/<int:gadget_id>/', single_gadgeds_int_view),
    path('gadget/<slug:gadget_slug>/', single_gadgeds_view, name="gadget_slug_url")
]
