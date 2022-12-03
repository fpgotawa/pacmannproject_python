# %%
# Import numpy library untuk membantu membuat urutan nomor item pada tabel
import numpy as np

# Import pandas library untuk membuat tabel transaksi
import pandas as pd

# Buat class
class Transaction:
    # Inisiasi class, buat dictionary kosong untuk menampung item transaksi
    def __init__(self):
        self.ordered_item = dict()

    # Fungsi 1, menambahkan item baru dengan mengisi nama, jumlah, dan harga per item    
    def add_item(self, nama_item, jumlah_item, harga_per_item):
        self.ordered_item[nama_item] = [jumlah_item, harga_per_item]
        print(f"Item yang dibeli adalah: {self.ordered_item}")

    # Fungsi 2, mengubah nama item
    def update_item_name(self, nama_item, update_nama_item):
        self.ordered_item[update_nama_item] = self.ordered_item[nama_item]
        del self.ordered_item[nama_item]
        print("Nama item berhasil diubah.")
        print(f"Item yang dibeli adalah: {self.ordered_item}")

    # Fungsi 3, mengubah jumlah item
    def update_item_qty(self, nama_item, update_jumlah_item):
        self.ordered_item[nama_item][0] = update_jumlah_item
        print("Jumlah item berhasil diubah.")
        print(f"Item yang dibeli adalah: {self.ordered_item}")

    # Fungsi 4, mengubah harga per item
    def update_item_price(self, nama_item, update_harga_item):
        self.ordered_item[nama_item][1] = update_harga_item
        print("Harga item berhasil diubah.")
        print(f"Item yang dibeli adalah: {self.ordered_item}")

    # Fungsi 5, menghapus satu item tertentu
    def delete_item(self, nama_item):
        del self.ordered_item[nama_item]
        print(f"{nama_item} berhasil dihapus.")

    # Fungsi 6, menghapus semua item yang sudah diinput
    def reset_transaction(self):
        self.ordered_item = dict()
        print("Semua item berhasil dihapus.")

    # Fungsi 7, melakukan pengecekan input apakah sudah sesuai dan menampilkan tabel item yang akan dibeli
    def check_order(self):
        self.table_order = pd.DataFrame.from_dict(self.ordered_item, orient="index", columns=["Jumlah Item", "Harga/Item"])
        self.table_order.index.names = ["Nama Item"]
        self.table_order.reset_index(inplace=True)
        self.table_order.index = np.arange(1, len(self.table_order) + 1)
        self.table_order.index.names = ["No"] 

        # Melakukan pengecekan apakah tipe data yang diinput sudah sesuai 
        try:
            for key, value in self.ordered_item.items():
                key = str(key)
                value[0] = int(value[0])
                value[1] = float(value[1])
      
            self.table_order["Total Harga"] = self.table_order["Jumlah Item"] * self.table_order["Harga/Item"]
            print("Pemesanan sudah benar.")
            print(self.table_order)
        except:
            print("Terdapat kesalahan input data. Silakan dicek kembali.")
            print(self.table_order)

    # Fungsi 8, menampilkan total harga yang harus dibayarkan setelah diskon
    def total_price(self):
        try:
            total_harga = self.table_order["Total Harga"].sum()

            # Harga di atas 500000 diskon 10%
            if total_harga > 500000:
                persen_diskon = 0.10
                diskon = total_harga * persen_diskon
                harga_diskon = total_harga - diskon

                print(f"Selamat anda mendapat potongan harga sebesar {persen_diskon*100}% atau sebesar Rp{diskon}!")
                print(f"Total belanja anda adalah sebesar Rp{harga_diskon}.")

            # Harga di atas 300000 diskon 8%
            elif total_harga > 300000:
                persen_diskon = 0.08
                diskon = total_harga * persen_diskon
                harga_diskon = total_harga - diskon

                print(f"Selamat anda mendapat potongan harga sebesar {persen_diskon*100}% atau sebesar Rp{diskon}!")
                print(f"Total belanja anda adalah sebesar Rp{harga_diskon}.")

            # Harga di atas 200000 diskon 5%
            elif total_harga > 200000:
                persen_diskon = 0.05
                diskon = total_harga * persen_diskon
                harga_diskon = total_harga - diskon

                print(f"Selamat anda mendapat potongan harga sebesar {persen_diskon*100}% atau sebesar Rp{diskon}!")
                print(f"Total belanja anda adalah sebesar Rp{harga_diskon}.")

            # Harga di bawah 200000 tidak mendapat diskon
            else:
                print(f"Total belanja anda adalah sebesar Rp{total_harga}.")
        except:
            print("Anda belum melakukan pengecekan item. Silakan gunakan check_order() untuk melakukan pengecekan sebelum menghitung total.")

