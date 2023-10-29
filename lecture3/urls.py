from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    # I included the hello file which I newly created also import it above
    path('hello/', include("hello.urls")),
    path('newyear/', include("newyear.urls")),
    path('tasks/', include('tasks.urls')),
]
