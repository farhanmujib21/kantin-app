from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views as core_views
from menu import views as menu_views
from orders import views as order_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', core_views.login_view, name='login'),
    path('register/', core_views.register_view, name='register'),
    path('logout/', core_views.logout_view, name='logout'),
    path('', menu_views.katalog, name='katalog'),
    path('tambah-keranjang/<int:menu_id>/', menu_views.tambah_keranjang, name='tambah_keranjang'),
    path('keranjang/', menu_views.keranjang, name='keranjang'),
    path('hapus-keranjang/<int:menu_id>/', menu_views.hapus_keranjang, name='hapus_keranjang'),
    path('checkout/', order_views.checkout, name='checkout'),
    path('pesanan-saya/', order_views.pesanan_saya, name='pesanan_saya'),
    path('admin-dashboard/', order_views.admin_dashboard, name='admin_dashboard'),
    path('update-status/<int:pesanan_id>/', order_views.update_status, name='update_status'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)