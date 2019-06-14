"""rest_framework_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
# from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

urlpatterns1 = [
    url(r'testapp/', include('testapp.urls', namespace="testapp_namespace")),
]
urlpatterns = urlpatterns1 + [
    url(r'^admin/', admin.site.urls),
    # url(r'^docs/', include_docs_urls(title='My API title')),
    url(r'^report_builder/', include('report_builder.urls')),
    url(r'swagger/', get_swagger_view(title="文档", patterns=urlpatterns1)),
    url(r'^wsapp/chat/', include('chat.urls', namespace="chat")),
    # path("testapp/", include("testapp.urls", namespace="testapp_namespace")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
