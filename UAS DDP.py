# Hendri Zaidan Safitra
# 2409116013

from prettytable import PrettyTable
from datetime import datetime
import pwinput
import os
import json
import sys
import re
os.system("cls")

json_path = "D:/VSC Codingan/UAS/New folder/databasetoko.json"

with open(json_path, "r") as jsondatabasetoko:
    data = json.loads(jsondatabasetoko.read())

def update_database():
    with open(json_path, "w") as jsondatabasetoko:
        json.dump(data, jsondatabasetoko, indent=4)

def Akun():
    os.system("cls")
    print("╭▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╮")
    print("             Silakan Pilih Login Menu ")
    print("          1. Login (Jika Sudah Punya akun)")
    print("          2. Daftar Akun (Jika Belum Punya akun)")
    print("╰▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬╯")

    while True:
        try:
            mode = input("Silakan Pilih masukan sesuai menu Login/Daftar Akun : ").strip()
            if mode == "1":
                Login()
            elif mode == "2":
                daftar()
            else:
                print("Menu tidak tersedia!")
            continue
        except KeyboardInterrupt:
            print("\n" + "=" * 10 + "Program akan keluar" + "=" * 10)
            sys.exit()

def Login():
    os.system("cls")
    print("    ╔════════════════════════════════════════╗")
    print("       Selamat Datang Di Toko Tiket Bioskop ")
    print("                     ༼ つ ◕_◕ ༽つ           ")
    print("    ╚════════════════════════════════════════╝")

    print("Masukkan Username dan Pin anda!")
    
    members = data.get("Members", {})
    blocked_accounts = data.get("Block_akun", {})
    
    login_username = {member["Username"]: member for member in members}
    percobaan_login = 3

    try:
        for i in range(percobaan_login):
            username = input("Username: ").strip()

            if not username:
                print("Username tidak boleh kosong. Silakan coba lagi.")
                os.system("pause")
                Akun()
                return

            if username in blocked_accounts:
                print("Akun Anda telah diblokir. Silakan hubungi admin untuk meminta bantuan.")
                os.system("pause")
                Akun()
                return

            member_info = login_username.get(username)
            if member_info:
                input_pin = pwinput.pwinput(prompt="PIN: ")
                if input_pin == member_info["Pin"]:
                    membertoko(username)  
                    return
                else:
                    print("PIN salah!")
            else:
                print("Username anda tidak valid ( ꩜ ᯅ ꩜;)⁭ ⁭")
                os.system("pause")
                Akun()
                return
            

        print(f"Anda telah menggunakan semua kesempatan login untuk {username}. Akun akan diblokir.")
        blocked_accounts[username] = True
        data["Block_akun"] = blocked_accounts
        update_database()
        os.system("pause")

        print("Silakan Ulang kembali Program ᕙ(⇀‸↼‶)ᕗ.")
        Akun()
        
    except EOFError:
        print("\nInput tidak valid. Silakan coba lagi.")
    except ValueError:
        print("DATA ANDA TIDAK VALID YA (˶˃ ᵕ ˂˶)!")
    except KeyboardInterrupt:
        print("\n" + "=" * 10 + "Program akan keluar" + "=" * 10)
        sys.exit()

def membertoko(username):
    os.system("cls")
    
    member_info = None
    for member in data["Members"]:
        if member["Username"] == username:
            member_info = member
            break

    if member_info is None:
        print("User tidak ditemukan.")
        return

    nama = member_info['Username']
    member_type = member_info['Member']

    print(" ╔═════════════════════════════════════════════════════════════════════════════════════════╗")
    print(f"                  Selamat Datang di Toko Tiket Bioskop, {nama} ༼ つ ◕_◕ ༽つ")
    print(" ╚═════════════════════════════════════════════════════════════════════════════════════════╝")
    
    if member_type == "VIP":
        print(f" ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ Menu Fitur VIP Member ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("   1. Daftar Jadwal Film ")
        print("   2. Top Up saldo ")
        print("   3. Pemesanan Tiket ")
        print("   4. Cek Saldo")
        print("   5. Top Up Diamonds ")
        print("   6. Daftar Tiket Pesanan")
        print("   7. Log Out ")
    else:  
        print(f" ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ Menu Fitur Member Biasa ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
        print("   1. Update Member ")
        print("   2. Top Up saldo ")
        print("   3. Pemesanan Tiket ")
        print("   4. Cek Saldo")
        print("   5. Top Up Diamonds ")
        print("   6. Daftar Tiket Pesanan")
        print("   7. Log Out ")

    print(" ╚═════════════════════════════════════════════════════════════════════════════════════════╝")

    while True:
        opsi = input("Pilih opsi (1-7): ").strip()
        
        if opsi == '1':
            if member_type == "VIP":
                daftar_film_vip(username)
            else:
                update_member(username)
        elif opsi == '2':
            topup_saldo(username)
        elif opsi == '3':
            pemesanan_tiket(username)
        elif opsi == '4':
            cek_saldo(username)
        elif opsi == '5':
            TopUp_Diamonds(username)
        elif opsi == '6':
            daftar_tiket(username)
        elif opsi == '7':
            mode_login = input ("Apakah anda ingin Keluar atau Kembali ke mode login? (Keluar/mulai) : ").capitalize()
            if mode_login == "Keluar":
                print("Terimakasih telah berkunjung di Toko Tiket Bioskop!!!")
                sys.exit()
            elif mode_login == "Mulai":
                Akun()
                break  
            else:
                print("Pilihan tidak valid!")
                continue
        else:
            print("Pilihan tidak valid!")
        

def real_time():
    realtime = datetime.now().time()

    if datetime.strptime("00:00", "%H:%M").time() <= realtime <= datetime.strptime("12:59", "%H:%M").time():
        return 'Pagi'
    elif datetime.strptime("13:00", "%H:%M").time() <= realtime <= datetime.strptime("18:59", "%H:%M").time():
        return 'Siang'
    else:
        return 'Malam'
    
def daftar_film_vip(username): 
    jadwal_film = real_time()

    table = PrettyTable()
    table.field_names = ["Judul", "Jam Tayang", "Kategori", "Harga"]

    for studio, jadwal in data["Studios"].items():
        if jadwal_film in jadwal:
            movies = jadwal[jadwal_film]
            for movie in movies:
                table.add_row([movie["Judul"], movie["Jam_Tayang"], movie["Kategori"], movie["Harga"]])
    print("\n" + "=" * 20 + f" Daftar Film" + "=" * 20)
    print(table)
    return

def daftar_film(username):
    jadwal_film = real_time()

    table = PrettyTable()
    table.field_names = ["Judul", "Jam Tayang", "Kategori", "Harga"]

    for studio, jadwal in data["Studios"].items():
        if jadwal_film in jadwal:
            movies = jadwal[jadwal_film]
            for movie in movies:
                if movie["Kategori"] == "Biasa":
                    table.add_row([movie["Judul"], movie["Jam_Tayang"], movie["Kategori"], movie["Harga"]])
    print("\n" + "=" * 20 + f" Daftar Film" + "=" * 20)
    print(table)
    

def topup_saldo(username):
    os.system("cls")
    print("◇─◇──◇─────◇──◇─◇ Isi Saldo ◇─◇──◇─────◇──◇─◇")
    
    try:
        topup_amount = float(input("Masukkan jumlah saldo yang ingin Anda isi: "))
        
        if topup_amount < 20000:
            print("Jumlah saldo harus lebih dari Rp. 20.000.")
            os.system("pause")
            membertoko(username)
            return    
        
        elif topup_amount > 6000000:
            print("Jumlah saldo melebihi batas Rp. 6.000.000.")
            os.system("pause")
            membertoko(username)
            return  

        confirm = input(f"Konfirmasi pengisian Rp.{topup_amount:,.2f} saldo? (y/n): ")
        
        if confirm.lower() == "y":
            for member in data["Members"]:
                if member["Username"] == username:
                    member["Saldo"] += topup_amount
                    update_database()  
                    
                    print(f"Isi saldo berhasil. Saldo Anda sekarang: Rp.{member['Saldo']:,.2f}")
                    os.system("pause")
                    membertoko(username)
                    break
        else:
            print("Pengisian saldo dibatalkan (˶˃ ᵕ ˂˶).")
            os.system("pause")
            membertoko(username)

    except ValueError:
        print("Masukan harus berupa angka (˶˃ ᵕ ˂˶).")
        os.system("pause")
        membertoko(username)

def daftar_diamonds():
    print("\n" + "=" * 10 + f" Daftar Harga Diamonds" + "=" * 10)
    
    table_coin = PrettyTable()
    table_coin.field_names = ["Jumlah Diamonds", "Harga (IDR)"]
    
    for jumlah, harga in data["Topup"].items():
        table_coin.add_row([jumlah, harga])
    
    print(table_coin)

def TopUp_Diamonds(username):
    os.system("cls")
    print("◇─◇──◇─────◇──◇─◇ Isi Saldo Diamond ◇─◇──◇─────◇──◇─◇")
    daftar_diamonds()  
    
    try:
        Topup_Diamonds = input("Masukkan nominal diamond yang ingin dibeli: ")

        if Topup_Diamonds not in data["Topup"]:
            print("Top up diamonds tidak valid. Silakan pilih dari daftar.")
            os.system("pause")
            membertoko(username)
            return
        
        total_harga = data["Topup"][Topup_Diamonds]
        
        confirm = input(f"Konfirmasi pembelian {Topup_Diamonds} diamond seharga Rp.{total_harga:,.2f}? (y/n): ")
        
        if confirm.lower() == "y":
            for member in data["Members"]:
                if member["Username"] == username:
                    if member["Saldo"] < total_harga:  
                        print("Saldo tidak mencukupi untuk membeli diamond ini, silakan top up terlebih dahulu.")
                        os.system("pause")
                        membertoko(username)
                        return
                    
                    member["Saldo"] -= total_harga
                    member["Diamond"] += float(Topup_Diamonds)
                    update_database()  

                    print(f"{Topup_Diamonds} diamond berhasil ditambahkan! Total diamond Anda: {member['Diamond']:,.2f}")
                    print(f"Sisa saldo Anda: Rp. {member['Saldo']:,.2f}")
                    os.system("pause")
                    membertoko(username)
                    return
        
        else:
            print("Pembelian dibatalkan.")
            os.system("pause")
            membertoko(username)

    except ValueError as e:
        print(f"Inputan Salah: {e}")
        os.system("pause")
        membertoko(username)

def cek_saldo(username):
    os.system("cls")
    while True:
        print("\n" + "=" * 10 + " Menu Cek Saldo " + "=" * 10)
        print("1. Melihat Saldo IDR")
        print("2. Melihat Jumlah Diamond")
        print("3. Kembali")

        opsi = input("Pilih opsi (1-3): ").strip()

        member_info = next((member for member in data["Members"] if member["Username"] == username), None)

        if opsi == '1':
            if member_info:
                print("====== Cek Saldo ======")
                print(f"Saldo E-Money Anda: Rp. {member_info['Saldo']:,.2f}")
            else:
                print("Username tidak ditemukan")
            continue 

        elif opsi == '2':
            if member_info:
                print("====== Cek Diamond ======")
                print(f"Jumlah Diamond Anda: {member_info['Diamond']}")
            else:
                print("Username tidak ditemukan!")
            continue 

        elif opsi == '3':
            membertoko(username)  
            break
        else:
            print("Pilihan tidak valid ༼ つ ◕_◕ ༽つ!")

def daftar_member():
    print("\n" + "=" * 10 + f" Daftar Membership ༼ つ ◕_◕ ༽つ " + "=" * 10)
    
    table_member = PrettyTable()
    table_member.field_names = ["Member", "Harga (IDR)"]
    
    for jumlah, harga in data["Membership"].items():
        table_member.add_row([jumlah, harga])
    
    print(table_member)

def update_member(username):
    os.system("cls")
    daftar_member()

    try:
        member_info = next((member for member in data["Members"] if member["Username"] == username), None)

        if member_info is None:
            print("Pengguna tidak ditemukan.")
            os.system("pause")
            return
        
        if member_info["Member"] == "Biasa":
            if member_info["Saldo"] >= 500000:  
                confirm = input(f"Konfirmasi Upgrade {username} dari Member Biasa ke Member VIP (y/n)? ")

                if confirm.lower() == "y":
                    member_info["Saldo"] -= 500000 
                    member_info["Member"] = "VIP" 

                    print(f"{username} telah berhasil diupgrade menjadi VIP ༼ つ ◕_◕ ༽つ!")
                    update_database()  
                    os.system("pause")
                    Akun()  
                else:
                    print("Upgrade dibatalkan.")
                    os.system("pause")
                    Akun()  
            else:
                print("Saldo tidak mencukupi untuk upgrade ke VIP. Silakan top up saldo terlebih dahulu (˶˃ ᵕ ˂˶).")
                os.system("pause")
                Akun()  
        else:
            print(f"{username} sudah merupakan Member VIP.")
            return

    except KeyboardInterrupt:
        print("\n" + "=" * 10 + "Program akan keluar" + "=" * 10)
        sys.exit()

def daftar():
    os.system("cls")
    while True:
        try:
            print(" ◀▬▬▬▬▬▬▬▬▬▬▬▬▬▬ Sign Up Akun ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▶")
            username = input("Masukkan username anda: ").strip()

            if not Validasi(username):
                print("Username tidak valid.")
                continue

            if username in [member["Username"] for member in data["Members"]]:
                print("Username telah terdaftar. Silakan cari username yang lain!")
                continue
            
            Kode_pin = input("Masukkan PIN anda (6 digit): ").strip()
            if Kode_pin.isdigit() and len(Kode_pin) == 6:
                data["Members"].append({  
                    "Username": username,
                    "Member": "Biasa",
                    "Pin": Kode_pin,
                    "Saldo": 0,
                    "Diamond": 0,
                })
                
                os.system('cls')
                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                print(f"           Selamat Datang di Toko Tiket Bioskop, {username} ༼ つ ◕_◕ ༽つ ")
                print("╔═══════════════════════════════════════════════════════════════════════════════════╗")
                print(f"               Saldo Anda: Rp.{0:,}, HARAP MELAKUKAN PENGISIAN!")
                print("╚═══════════════════════════════════════════════════════════════════════════════════╝")
                print("╔═══════════════════════════════════════════════════════════════════════════════════╗")
                print(f"               PIN Anda adalah: {Kode_pin}, Jangan sampai lupa ya")
                print("╚═══════════════════════════════════════════════════════════════════════════════════╝")

                update_database()  
                
                while True:
                    mode_login = input("Apakah anda ingin Keluar atau Kembali ke mode login? (Keluar/Mulai): ").capitalize()
                    if mode_login == "Keluar":
                        print("Terimakasih telah berkunjung di Toko Tiket Bioskop!")
                        sys.exit()
                    elif mode_login == "Mulai":
                        Akun()  
                        break  
                    else:
                        print("Pilihan tidak valid!")
            else:
                print("PIN harus berupa angka dengan panjang 6 digit. Silakan coba lagi.")
        except ValueError:
            print("Inputan Harus Berupa Angka!")
            os.system("pause")

def Validasi(username):
    return bool(re.search(r'[a-zA-Z]', username))

def pemesanan_tiket(username):
    os.system("cls")
    member_info = None
    
    for member in data["Members"]:
        if member["Username"] == username:
            member_info = member
            break
            
    if member_info is None:
        print("Pengguna tidak ditemukan.")
        os.system("pause")
        return
    
    member_type = member_info['Member']
    print(" ╔═════════════════════════════════════════════════════════════════════════════════════════╗")
    print(f"           Selamat Datang Booking Tiket di Toko Tiket Bioskop ༼ つ ◕_◕ ༽つ")
    print(" ╚═════════════════════════════════════════════════════════════════════════════════════════╝")
    
    film_ada = False
    
    if member_type == "VIP":
        daftar_film_vip(username)
        try:
            film = input("Masukkan Film yang ingin dipesan: ").strip().lower()
            
            for studio, jadwal in data["Studios"].items():
                for waktu, movies in jadwal.items():
                    for movie in movies:
                        if movie["Judul"].lower() == film:
                            film_ada = True
                            harga = movie["Harga"]
                            selected_showtime = input("Masukkan jam tayang (HH:MM): ")
                            showtime = datetime.strptime(selected_showtime, "%H:%M").time()  
                            current_time = datetime.now().time()
                            current_time_tiket = datetime.now().strftime("%d-%m-%Y %H:%M:%S")  
                            
                            if showtime <= current_time:
                                print("Tidak dapat memesan tiket setelah jam tayang.")
                                os.system("pause")
                                membertoko(username)
                                return
                            
                            confirm = input("Apakah ada Voucher Tiket ? (y/n)? ")
                            
                            if confirm.lower() == 'y':
                                voucher_code = input("Masukkan Kode Voucher Tiket: ")
                                voucher_valid = False
                                
                                for voucher in data.get("voucher", []):
                                    if voucher_code == voucher["kode"]:
                                        voucher_valid = True
                                        if voucher["status"] == 'Digunakan':
                                            print("Kode voucher sudah digunakan. Silakan masukkan kode voucher lain.")
                                            os.system("pause")
                                            membertoko(username)
                                            return
                                        
                                        diskon = (voucher["diskon"] / 100) * harga
                                        total_harga = harga - diskon
                                        print(f"Anda telah menggunakan Voucher tiket dengan diskon {voucher['diskon']}%. Total harga tiket: Rp.{total_harga}.")

                                        if member_info["Diamond"] >= total_harga:

                                            if 'Daftar_tiket' not in data:
                                                data['Daftar_tiket'] = {}
                                            
                                            ticket_id = len(data["Daftar_tiket"]) + 1  

                                            data["Daftar_tiket"][ticket_id] = {
                                                'Judul': film,
                                                'Username': username,
                                                'Jam_tayang': selected_showtime,
                                                'status': 'Terpesan',
                                                'Total_Harga': total_harga,
                                            }

                                            member_info["Diamond"] -= total_harga
                                            voucher["status"] = 'Digunakan'
                                            voucher["penggunaan_terakhir"] = current_time_tiket
                                            voucher["jumlah_penggunaan"] -= 1 
                                            
                                            print(f"Tiket untuk '{film}' berhasil dipesan! Diamond Anda sekarang: Rp.{member_info['Diamond']}.")
                                        else:
                                            print("Diamond tidak mencukupi untuk membeli tiket ini. Silakan top up saldo terlebih dahulu.")
                                        os.system("pause")
                                        update_database()
                                        membertoko(username)
                                        return

                                if not voucher_valid:
                                    print("Kode voucher tidak valid.")
                                    os.system("pause")
                                    membertoko(username)
                                    return

                            if member_info["Diamond"] >= harga:
                                if 'Daftar_tiket' not in data:
                                    data['Daftar_tiket'] = {}
                                
                                ticket_id = len(data["Daftar_tiket"]) + 1  

                                data["Daftar_tiket"][ticket_id] = {
                                    'Judul': film,
                                    'Username': username,
                                    'Jam_tayang': selected_showtime,
                                    'status': 'Terpesan',
                                    'Total_Harga': harga,
                                }
                                
                                member_info["Diamond"] -= harga
                                print(f"Tiket untuk '{film}' berhasil dipesan! Harga: Rp.{harga}. Diamond Anda sekarang: Rp.{member_info['Diamond']}.")
                                update_database()
                                os.system("pause")
                                return
                            else:
                                print("Diamond tidak mencukupi untuk membeli tiket ini. Silakan top up saldo terlebih dahulu.")
                                os.system("pause")
                                return
                    
                    if film_ada:
                        break  
                
                if not film_ada:
                    print(f"Film '{film}' tidak ditemukan. Silakan coba lagi.")
                    os.system("pause")
                    membertoko(username)
                    return
        
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            os.system("pause")
            
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
            os.system("pause")

    else:
        daftar_film(username)
        try:
            film = input("Masukkan Film yang ingin dipesan: ").strip().lower()  
            
            for studio, jadwal in data["Studios"].items():
                for waktu, movies in jadwal.items():
                    for movie in movies:
                        if movie["Judul"].lower() == film:  
                            film_ada = True
                            harga = movie["Harga"]
                            selected_showtime = input("Masukkan jam tayang (HH:MM): ")

                            showtime = datetime.strptime(selected_showtime, "%H:%M").time()
                            current_time = datetime.now().time()
                                
                            if showtime <= current_time:
                                print("Tidak dapat memesan tiket setelah jam tayang.")
                                os.system("pause")
                                return
                                
                            if member_info["Diamond"] >= harga:
                                if 'Daftar_tiket' not in data:
                                    data['Daftar_tiket'] = {}
                                    
                                ticket_id = len(data["Daftar_tiket"]) + 1 
                                data["Daftar_tiket"][ticket_id] = {
                                    'Judul': movie["Judul"],
                                    'Username': username,
                                    'Jam_tayang': selected_showtime,
                                    'status': 'Terpesan',
                                    'Total_Harga': harga,
                                    }
                                    
                                member_info["Diamond"] -= harga 
                                print(f"Tiket untuk '{movie['Judul']}' berhasil dipesan! Harga: Rp.{harga}. Diamond Anda sekarang: Rp.{member_info['Diamond']}.")
                                    
                                update_database()  
                                os.system("pause")
                                membertoko(username)  
                                return
                            else:
                                print("Diamond tidak mencukupi untuk membeli tiket ini. Silakan top up saldo terlebih dahulu (˶˃ ᵕ ˂˶).")
                            break 
                    if film_ada:
                        break
                
                if film_ada:
                    break
        
            if not film_ada:
                print(f"Film '{film}' tidak ditemukan. Silakan coba lagi.")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
    
    os.system("pause")

def daftar_tiket(username):
    os.system("cls") 
    
    table = PrettyTable()
    table.field_names = ["Judul", "Username", "Jam Tayang", "Status", "Total Harga"]
    
    tiket_ditemukan = False 

    for tiket, info in data.get("Daftar_tiket", {}).items():
        if info['Username'] == username:  
            table.add_row([info['Judul'], info['Username'], info['Jam_tayang'], info['status'], info['Total_Harga']])
            tiket_ditemukan = True 
    
    print("\n=== Daftar Tiket Anda ===")
    
    if tiket_ditemukan:
        print(table)  
    else:
        print("Tidak ada reservasi yang terdaftar.") 
    
    os.system("pause")
    membertoko(username)

Akun()