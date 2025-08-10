from django.urls import path
from .views import single_gadgeds_int_view, GadgetsView, RedirectToGagedsView, start_page_view


urlpatterns = [
    path('start/', start_page_view),
    path('', RedirectToGagedsView.as_view()),
    path('<int:gadget_id>', RedirectToGagedsView.as_view()),
    path('gadget/', GadgetsView.as_view()),
    path('gadget/<int:gadget_id>/', single_gadgeds_int_view),
    path('gadget/<slug:gadget_slug>/', GadgetsView.as_view(), name="gadget_slug_url"),
]
