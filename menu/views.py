from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Menu

@login_required
def katalog(request):
    menus = Menu.objects.filter(is_tersedia=True)
    return render(request, 'menu/katalog.html', {'menus': menus})

@login_required
def tambah_keranjang(request, menu_id):
    keranjang = request.session.get('keranjang', {})
    menu = get_object_or_404(Menu, id=menu_id)
    key = str(menu_id)
    if key in keranjang:
        keranjang[key]['jumlah'] += 1
    else:
        keranjang[key] = {
            'nama': menu.nama_makanan,
            'harga': int(menu.harga),
            'jumlah': 1
        }
    request.session['keranjang'] = keranjang
    messages.success(request, f'{menu.nama_makanan} ditambahkan ke keranjang!')
    return redirect('/')

@login_required
def keranjang(request):
    keranjang = request.session.get('keranjang', {})
    total = sum(item['harga'] * item['jumlah'] for item in keranjang.values())
    return render(request, 'menu/keranjang.html', {'keranjang': keranjang, 'total': total})

@login_required
def hapus_keranjang(request, menu_id):
    keranjang = request.session.get('keranjang', {})
    keranjang.pop(str(menu_id), None)
    request.session['keranjang'] = keranjang
    return redirect('/keranjang/')