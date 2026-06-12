from django.db import models
from django.contrib.auth.models import User
from menu.models import Menu

class Pesanan(models.Model):
    STATUS_CHOICES = [
        ('menunggu', 'Menunggu'),
        ('diproses', 'Diproses'),
        ('siap', 'Siap Diambil'),
    ]
    pembeli = models.ForeignKey(User, on_delete=models.CASCADE)
    tanggal_pesan = models.DateTimeField(auto_now_add=True)
    total_harga = models.DecimalField(max_digits=10, decimal_places=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='menunggu')
    nomor_antrean = models.IntegerField(default=0)

    def __str__(self):
        return f"Pesanan #{self.nomor_antrean} - {self.pembeli.username}"

class DetailPesanan(models.Model):
    pesanan = models.ForeignKey(Pesanan, on_delete=models.CASCADE, related_name='details')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    jumlah = models.IntegerField(default=1)
    sub_total = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return f"{self.menu.nama_makanan} x{self.jumlah}"