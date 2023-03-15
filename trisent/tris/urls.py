from django.urls import path
from .views import index, register, login, thrift, travel, search_results, contact
from . import views
urlpatterns=[
    path('',views.index,name="index"),
    # path('',views.counteer,name="counteer"),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('thrift',views.thrift,name="thrift"),
    path('travel',views.travel,name="travel"),
    path('search/',search_results,name="search"),
    path('homedecor',views.homedecor,name="homedecor"),
    path('CultureNew',views.CultureNew,name="CultureNew"),
    #path to send form to backend
    path('Contact',views.Contact,name="Contact"),
    path('food',views.foods,name="food")
]