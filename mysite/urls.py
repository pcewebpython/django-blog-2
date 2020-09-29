
from django.contrib import admin
from django.urls import path, include  # <-- Make sure you have both of these imports.


urlpatterns = [
    path('', include('blogging.urls')),  # <-- add this
    path('polling/', include('polling.urls')),  # <-- Add this
    path('blogging/', include('blogging.urls')),  # <-- Add this
    path('admin/', admin.site.urls),
]
