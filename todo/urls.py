
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    ###import all app urls
    path('' , include('app.urls'))
]
