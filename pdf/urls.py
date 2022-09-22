from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf.urls.static import static
from django.conf import settings
#from .views import GeneratePdf
urlpatterns = [
    path("",views.dashboard,name='dashboard'),
    path("<int:id>/",views.resume,name='resume'),
    path('<int:id>/download/', views.download),
    path('list/',views.list,name='list')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)