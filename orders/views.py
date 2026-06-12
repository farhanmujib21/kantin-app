from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Pesanan, DetailPesanan
from menu.models import Menu

def is_admin(user):
    return user.is_staff

@login_required
def checkout(request):
    keranjang = request.session.get('keranjang', {})
    if not keranjang:
        messages.error(request, 'Keranjang kosong!')
        return redirect('/')

    total = sum(item['harga'] * item['jumlah'] for item in keranjang.values())
    nomor = (Pesanan.objects.count() or 0) + 1

    pesanan = Pesanan.objects.create(
        pembeli=request.user,
        total_harga=total,
        nomor_antrean=nomor
    )

    for menu_id, item in keranjang.items():
        menu = Menu.objects.get(id=int(menu_id))
        DetailPesanan.objects.create(
            pesanan=pesanan,
            menu=menu,
            jumlah=item['jumlah'],
            sub_total=item['harga'] * item['jumlah']
        )

    request.session['keranjang'] = {}
    messages.success(request, f'Pesanan berhasil! Nomor antrean kamu: #{nomor}')
    return redirect('/pesanan-saya/')

@login_required
def pesanan_saya(request):
    pesanan = Pesanan.objects.filter(pembeli=request.user).order_by('-tanggal_pesan')
    return render(request, 'orders/pesanan_saya.html', {'pesanan': pesanan})

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    pesanan = Pesanan.objects.all().order_by('-tanggal_pesan')
    return render(request, 'orders/admin_dashboard.html', {'pesanan': pesanan})

@login_required
@user_passes_test(is_admin)
def update_status(request, pesanan_id):
    pesanan = Pesanan.objects.get(id=pesanan_id)
    status_map = {'menunggu': 'diproses', 'diproses': 'siap'}
    pesanan.status = status_map.get(pesanan.status, pesanan.status)
    pesanan.save()
    return redirect('/admin-dashboard/')