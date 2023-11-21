from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addmsg/', views.addmsg, name='add_msg'),
    path('login/', views.login, name='login'),
    path('msgs/<int:msg_id>/', views.show_msg, name='msg'),
    path('category/<int:cat_id>/', views.show_category, name='category'),

    # path('contact/', views.about, name='contact'),
    # path('msgs/<int:msg_id>/', views.messages, name='msg_id'),
    # path('msgs/<slug:msg_slug>/', views.messages_by_slug, name='msgs'),
    # path('reg/', views.registration, name='reg'),
    # path('archive/<year4:year>/', views.archive, name='archive'),
]