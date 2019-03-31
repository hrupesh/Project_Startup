"""ecommerce URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from user_model.views import user_signup, user_login, activate, user_home,password_reset, activate_password, password_reset_new, logout
from products.views import home, search, detail
from cart.views import view, cart_update , checkout
from Loma.views import Loma, loma_register, loma_login
from profilee.views import profile, edit_profile_page, edit_address, address_user, profile_user, profile_settings, profile_contact, your_order
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register_user/', user_signup, name='user_signup'),
    url(r'^login_user/', user_login, name='user_login'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
    url(r'^activate_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate_password, name='activate_password'),
    url(r'^home/(?P<slug>[\w-]+)/$', detail, name='details'),
    url(r'^home/', user_home , name='user_home'),
    url(r'^loma_register/', loma_register , name='loma_register'),
    url(r'^loma_login/', loma_login, name='loma_login'),
    url(r'^loma-home/', Loma , name='loma'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^$', home , name='home'),
    url(r'^search/', search, name='searchproduct'),
    url(r'^cart/(?P<slug>[\w-]+)/$', cart_update, name='cart_update'),
    url(r'^cart/', view, name='view'),
    url(r'^profile/', profile, name='profile'),
    url(r'^password_reset/', password_reset , name='password_reset'),
    url(r'^password_reset_new/', password_reset_new, name='password_reset_new'),
    url(r'^edit_profile/', edit_profile_page, name='edit_profile_page'),
    url(r'^edit_address/', edit_address, name='edit_address'),
    url(r'^profile_user/', profile_user, name='profile_user'),
    url(r'^your_order/', your_order, name='your_order'),
    url(r'^profile_contact/', profile_contact, name='profile_contact'),
    url(r'^address_user/', address_user, name='address_user'),
    url(r'^checkout/', checkout , name='checkout'),
    url(r'^logout/', logout, name='logout'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)