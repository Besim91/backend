from django.urls import path
from .views import start_page_view, single_gadgeds_view, single_gadgeds_slug_view, \
        single_gadgeds_post_view


urlpatterns = [
    path('', start_page_view),
    path('gadget/<int:gadget_id>/', single_gadgeds_view),
    path('gadget/<slug:gadget_slug>/', single_gadgeds_slug_view, name="gadget_slug_url"),
    path('gadget/send_gadget/', single_gadgeds_post_view)
]
