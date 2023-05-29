from django.contrib import admin
from django.urls import path, include

API_VERSION = 'v1'

urlpatterns = [
    path(f'api/{API_VERSION}/', include('app.pizza_context.infrastructure.urls')),


    path('admin/', admin.site.urls),

]
