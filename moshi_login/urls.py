"""moshi_login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from . import views

schema_view_swagger = get_swagger_view(title='Moshi Login')
from customuser import views as custom_user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', schema_view_swagger),
    url(r'^api/v1/token/$', views.TokenAccessView.as_view(), name='token_obtain_pair'),
    url(r'^api/v1/token/refresh/$', views.RefreshTokenView.as_view(), name='token_refresh'),
    url(r'^api/v1/token/verify/$', views.VerifyTokenView.as_view(), name='token_verify'),
    path('api/v1/secured', views.SecuredView.as_view()),
    path('api/v1/user/register', custom_user_views.RegisterUser.as_view()),
    path('api/v1/user/details', custom_user_views.UserDetailsView.as_view())
]
