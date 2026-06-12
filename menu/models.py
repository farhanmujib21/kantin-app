from django.db import models

class Menu(models.Model):
    nama_makanan = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=0)
    gambar = models.ImageField(upload_to='menu/', blank=True, null=True)
    is_tersedia = models.BooleanField(default=True)

    def __str__(self):
        return self.nama_makanan