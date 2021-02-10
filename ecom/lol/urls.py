#from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="shopHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("product/<int:myid>", views.productview, name="ProductView"),
    path("checkout/", views.checkout, name="CheckOut")
    #path("checkout/placeorder/", views.checkout.placeorder, name="PlaceOrder")

]