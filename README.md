# Kantin App 🍔

Kantin App adalah aplikasi berbasis web yang dibangun menggunakan framework **Django** untuk mempermudah proses pemesanan makanan dan minuman di lingkungan kantin (seperti Kantin USK). Aplikasi ini menyediakan pengalaman berbelanja makanan secara daring (*online*) untuk para pembeli, dan memudahkan pihak pengelola kantin (Admin) untuk memantau serta memperbarui pesanan secara seketika (*real-time*).

## ✨ Fitur Utama pada Aplikasi

Berikut adalah penjelasan detail mengenai fitur-fitur yang tersedia dalam aplikasi ini:

### 1. Sistem Autentikasi dan Role-based Access Control (RBAC)
Aplikasi memiliki sistem keamanan login dan registrasi akun. Pengguna dibedakan berdasarkan perannya (role):
- **Pembeli (User biasa)**: Dapat melihat katalog menu, menggunakan keranjang belanja, dan melacak pesanan miliknya.
- **Admin Kantin (Staff/Admin)**: Memiliki akses eksklusif ke Dashboard Admin untuk mengelola semua pesanan masuk dan mengubah status pemrosesan.

### 2. Katalog Menu Interaktif
Pembeli dapat melihat daftar makanan dan minuman yang tersedia secara dinamis, lengkap dengan nama menu, harga, dan gambar. Menu yang sedang habis/tidak tersedia (berdasarkan status `is_tersedia`) akan otomatis disembunyikan dari katalog.

### 3. Keranjang Belanja Berbasis Sesi (Session-based Cart)
Pembeli dapat menambahkan beberapa menu sekaligus ke dalam keranjang. Fitur ini menggunakan fitur *Session* pada Django, sehingga keranjang bersifat *temporary* sebelum checkout tanpa membebani database utama. Pengguna dapat menambah kuantitas atau menghapus item dari keranjang dengan mudah.

### 4. Checkout dan Penerbitan Nomor Antrean
Saat pembeli melakukan proses *Checkout*, aplikasi otomatis menghitung subtotal dan menerbitkan **Nomor Antrean** unik. Nomor antrean ini mempermudah pembeli saat mengambil makanannya ketika pesanan sudah disiapkan oleh kantin.

### 5. Manajemen Status Pesanan (Admin Dashboard)
Admin kantin diberikan antarmuka *Dashboard* khusus untuk memonitor semua pesanan yang masuk. Admin dapat mengubah status pesanan melalui alur:
`Menunggu` ➡️ `Diproses` ➡️ `Siap Diambil`

### 6. Riwayat & Pelacakan Pesanan (Pesanan Saya)
Setiap akun pembeli memiliki halaman "Pesanan Saya" untuk melihat daftar pesanan yang pernah dibuat, total harga, dan secara langsung melacak apakah pesanan mereka masih menunggu, sedang dimasak (diproses), atau sudah siap diambil.

---

## 🛠️ Komponen dan Teknologi yang Digunakan

Aplikasi Kantin ini dibangun menggunakan gabungan beberapa teknologi dan komponen pendukung:

### Backend Components
- **Python & Django Framework**: Sebagai tulang punggung (*core framework*) untuk mengatur *routing*, *views*, dan *business logic* dari keseluruhan aplikasi.
- **Django ORM & SQLite**: Komponen *Object-Relational Mapping* dari Django digunakan untuk berinteraksi dengan database bawaan SQLite secara aman (mencegah SQL Injection). Model yang digunakan terbagi menjadi tabel `User` (bawaan Django), `Menu`, `Pesanan`, dan `DetailPesanan`.
- **Django Sessions**: Komponen *middleware* bawaan Django yang menangani fitur Keranjang Belanja tanpa harus menyimpannya secara permanen di database sebelum pengguna melakukan checkout.
- **Django Authentication**: Komponen keamanan untuk enkripsi password (hashing), manajemen proses login/logout, serta kontrol akses (pembatasan *view* menggunakan pengamanan seperti dekorator `@login_required` dan `@user_passes_test`).

### Frontend Components
- **HTML5 & Django Templates**: Mesin *templating* dari Django untuk merender data dari database menjadi antarmuka web dinamis (`{% block %}`, `{% if %}`, `{% for %}`).
- **Bootstrap 5 (via CDN)**: Framework CSS yang menjadi komponen utama untuk merancang antarmuka pengguna (UI) secara cepat, rapi, dan *responsive*. Komponen Bootstrap yang dimanfaatkan antara lain: *Grid system*, *Navbar*, *Cards* (untuk item menu), *Badges* (untuk penanda status warna-warni), *Alerts* (untuk pesan notifikasi sukses/error), dan komponen *Buttons*.
- **FontAwesome 6**: Digunakan untuk menampilkan komponen ikon-ikon vektor pada aplikasi (seperti ikon alat makan, ikon keranjang, dan ikon *dashboard*) guna mempercantik tampilan visual antarmuka pengguna.
- **Custom CSS**: Memberikan gaya desain tambahan pada komponen seperti *background* *navbar* dengan warna gradien (*gradient orange*) dan efek visual bayangan (*shadow*) pada *card* komponen.

---

## 📂 Struktur Proyek

Proyek ini menerapkan arsitektur modular dari Django dan terbagi menjadi 3 aplikasi (apps) utama:

1. **`core`**: Komponen aplikasi untuk mengatur autentikasi pengguna (alur Login, Register, Logout).
2. **`menu`**: Komponen aplikasi untuk mengelola *database* katalog makanan (model `Menu`), serta *views* untuk pemrosesan keranjang belanja.
3. **`orders`**: Komponen aplikasi yang mengatur proses pembuatan riwayat `Pesanan`, `DetailPesanan`, serta menyediakan antarmuka *Dashboard* bagi Admin untuk memperbarui status pemesanan pelanggan.

---

## 🚀 Cara Menjalankan Proyek Secara Lokal

Ikuti langkah-langkah di bawah ini untuk menjalankan aplikasi di komputer Anda:

### 1. Prasyarat
Pastikan Anda sudah menginstal **Python** di komputer Anda.

### 2. Instalasi & Persiapan

Buka terminal/Command Prompt, lalu arahkan ke folder proyek ini.

```bash
# (Opsional) Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Instal Django
pip install django
```

### 3. Migrasi Database

Jalankan perintah migrasi untuk memastikan semua tabel dan komponen database (*User*, *Menu*, *Pesanan*) siap digunakan:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Membuat Akun Admin (Superuser)

Untuk mengakses halaman pengelolaan data (`/admin/`) dan fitur Dashboard Admin Kantin, buatlah akun *superuser*:

```bash
python manage.py createsuperuser
```
*(Ikuti instruksi di terminal untuk mengisi username, email, dan password).*

### 5. Menjalankan Server

Setelah semuanya siap, jalankan server pengembangan Django:

```bash
python manage.py runserver
```

Aplikasi sekarang dapat diakses melalui browser di alamat: **`http://127.0.0.1:8000/`**

---

## 👥 Anggota Kelompok

Proyek ini dikembangkan oleh:

| Nama | NPM |
| :--- | :--- |
| Firman Dwi Prabudi | 2008107010086 |
| Teuku Hafiz Izham | 2308107010056 |
| Farhan Mujiburrahman | 2308107010078 |
