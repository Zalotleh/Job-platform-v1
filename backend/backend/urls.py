
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('job.urls')),
    path('api/', include('account.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view())

]

handler500 = 'utils.error_views.handler500'
handler404 = 'utils.error_views.handler404'

