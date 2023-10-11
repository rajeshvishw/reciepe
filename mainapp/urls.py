from django.contrib import admin
from django.urls import path,include
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("register/", views.registerView, name="register"),
    path("login/", views.loginView, name="login"),
    path("form/",views.formView,name="form"),
    path("submit/",views.reciepepostView,name="savedata"),
    path("search/",views.searchView,name="search_value"),
    path("pricerenageView",views.pricerenageView, name= "pricerenageView"),
    path("logout/",views.logout,name="logout")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)