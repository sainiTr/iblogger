from django.urls import path,include
from python import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index,name='python'),
]