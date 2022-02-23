from django.contrib import admin
from .models import Item_Pembelian, Pembelian

class DaftarItemPembelian(admin.TabularInline):
	model = Item_Pembelian
	extra = 0

class DaftarPembelian(admin.ModelAdmin):
	list_display = ['kd_transaksi','nama', 'email', 'telepon', 'instansi', 'total_buku', 'tgl_transaksi', 'update', 'token', 'bayar']
	list_filter = ['bayar']
	exclude = ['nama', 'email', 'telepon']
	inlines = [DaftarItemPembelian]
	class Meta:
		Model = Pembelian

admin.site.register(Pembelian, DaftarPembelian)