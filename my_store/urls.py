from django.contrib import admin
from django.urls import path, include
from store import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    # Все маршруты приложения "Orders"
    path('orders', include('orders.urls', namespace='orders')),
    # Все маршруты приложения "Cart"
    path('cart', include('cart.urls', namespace='cart')),
    # Все маршруты приложения "Store"
    path('', include('store.urls', namespace='store')),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)