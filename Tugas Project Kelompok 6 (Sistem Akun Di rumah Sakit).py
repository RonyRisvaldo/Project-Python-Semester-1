class Pasien:
    def __init__(self, id_pasien, nama, usia, gejala, jenis_kelamin, alamat, no_telepon):
        self.id_pasien = id_pasien
        self.nama = nama
        self.usia = usia
        self.gejala = gejala
        self.jenis_kelamin = jenis_kelamin
        self.alamat = alamat
        self.no_telepon = no_telepon
        self.dilayani = False
        self.riwayat_pengobatan = []

class Dokter:
    def __init__(self, id_dokter, nama, spesialis, no_telepon):
        self.id_dokter = id_dokter
        self.nama = nama
        self.spesialis = spesialis
        self.no_telepon = no_telepon

class Akun:
    def __init__(self, username, password, peran):
        self.username = username
        self.password = password
        self.peran = peran

class RumahSakit:
    def __init__(self):
        self.pasien_list = []
        self.dokter_list = []
        self.akun_list = []

    def tambah_pasien(self, nama, usia, gejala, jenis_kelamin, alamat, no_telepon, username, password):
        id_pasien = len(self.pasien_list) + 1
        pasien_baru = Pasien(id_pasien, nama, usia, gejala, jenis_kelamin, alamat, no_telepon)
        self.pasien_list.append(pasien_baru)

        akun_pasien = Akun(username, password, "user")
        self.akun_list.append(akun_pasien)

    def tambah_dokter(self, nama, spesialis, no_telepon, username, password):
        id_dokter = len(self.dokter_list) + 1
        dokter_baru = Dokter(id_dokter, nama, spesialis, no_telepon)
        self.dokter_list.append(dokter_baru)

        akun_dokter = Akun(username, password, "dokter")
        self.akun_list.append(akun_dokter)

    def lihat_daftar_pasien(self):
        if not self.pasien_list:
            print("\nBelum ada pasien yang terdaftar.")
        else:
            garis = "=" * 100
            print("\n" + garis)
            print(f"{'Daftar Pasien':^100}")
            print(garis)
            print(f"{'ID':<5} {'Nama':<15} {'Usia':<5} {'Gejala':<20} {'Jenis Kelamin':<15} {'Alamat':<20} {'No Telepon':<15} {'Status':<15}")
            print(garis)
            for pasien in self.pasien_list:
                status = "Dilayani" if pasien.dilayani else "Belum Dilayani"
                print(f"{pasien.id_pasien:<5} {pasien.nama:<15} {pasien.usia:<5} {pasien.gejala:<20} {pasien.jenis_kelamin:<15} {pasien.alamat:<20} {pasien.no_telepon:<15} {status:<15}")
            print(garis)

    def lihat_daftar_dokter(self):
        if not self.dokter_list:
            print("\nBelum ada dokter yang terdaftar.")
        else:
            garis = "=" * 80
            print("\n" + garis)
            print(f"{'Daftar Dokter':^80}")
            print(garis)
            print(f"{'ID':<5} {'Nama':<20} {'Spesialis':<25} {'No Telepon':<20}")
            print(garis)
            for dokter in self.dokter_list:
                print(f"{dokter.id_dokter:<5} {dokter.nama:<20} {dokter.spesialis:<25} {dokter.no_telepon:<20}")
            print(garis)

    def login(self, username, password):
        for akun in self.akun_list:
            if akun.username == username and akun.password == password:
                print(f"\nLogin berhasil! Selamat datang, {username}.")
                return akun
        print("\nUsername atau password salah. Coba lagi.")
        return None

    def ganti_password(self, username):
        akun = next((a for a in self.akun_list if a.username == username), None)
        if akun:
            password_lama = input("Masukkan password lama: ")
            if akun.password == password_lama:
                password_baru = input("Masukkan password baru: ")
                akun.password = password_baru
                print("Password berhasil diubah.")
            else:
                print("Password lama tidak sesuai.")
        else:
            print("Akun tidak ditemukan.")

    def menu(self):
        while True:
            print("\n=================================")
            print("      Rumah Sakit ST Bhinneka")
            print("=================================")
            username = input("Masukkan Username: ")
            password = input("Masukkan Password: ")
            akun = self.login(username, password)
            if akun:
                if akun.peran == "admin":
                    self.menu_admin()
                elif akun.peran == "user":
                    self.menu_user(username)
                elif akun.peran == "dokter":
                    self.menu_dokter(username)

    def menu_admin(self):
        while True:
            print("\n=================================")
            print("         Menu Admin")
            print("=================================")
            print("1. Tambah Pasien")
            print("2. Lihat Daftar Pasien")
            print("3. Tambah Dokter")
            print("4. Lihat Daftar Dokter")
            print("5. Keluar")
            print("=================================")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                nama = input("Nama Pasien: ")
                usia = int(input("Usia: "))
                gejala = input("Gejala: ")
                jenis_kelamin = input("Jenis Kelamin: ")
                alamat = input("Alamat: ")
                no_telepon = input("No Telepon: ")
                username = nama.split()[0].lower()
                password = "1234"
                self.tambah_pasien(nama, usia, gejala, jenis_kelamin, alamat, no_telepon, username, password)
            elif pilihan == "2":
                self.lihat_daftar_pasien()
            elif pilihan == "3":
                nama = input("Nama Dokter: ")
                spesialis = input("Spesialis: ")
                no_telepon = input("No Telepon: ")
                username = nama.split()[0].lower()  # Hanya nama depan yang diambil untuk username
                password = "1234"
                self.tambah_dokter(nama, spesialis, no_telepon, username, password)
            elif pilihan == "4":
                self.lihat_daftar_dokter()
            elif pilihan == "5":
                print("Keluar dari menu admin.")
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")

    def menu_user(self, username):
        while True:
            print("\n=================================")
            print("         Menu User")
            print("=================================")
            print("1. Lihat Data Pribadi")
            print("2. Ganti Password")
            print("3. Keluar")
            print("=================================")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.lihat_data_pribadi(username)
            elif pilihan == "2":
                self.ganti_password(username)
            elif pilihan == "3":
                print("Keluar dari menu user.")
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")

    def menu_dokter(self, username):
        while True:
            print("\n=================================")
            print("         Menu Dokter")
            print("=================================")
            print("1. Lihat Data Pasien")
            print("2. Layani Pasien")
            print("3. Ganti Password")
            print("4. Keluar")
            print("=================================")
            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.lihat_daftar_pasien()
            elif pilihan == "2":
                self.layani_pasien()
            elif pilihan == "3":
                self.ganti_password(username)
            elif pilihan == "4":
                print("Keluar dari menu dokter.")
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")

    def lihat_data_pribadi(self, username):
        for akun in self.akun_list:
            if akun.username == username and akun.peran == "user":
                id_pasien = next((pasien.id_pasien for pasien in self.pasien_list if pasien.nama.split()[0].lower() == username), None)
                if id_pasien:
                    pasien = self.pasien_list[id_pasien - 1]
                    print(f"\nData Pribadi Pasien:\nID: {pasien.id_pasien}\nNama: {pasien.nama}\nUsia: {pasien.usia}\nGejala: {pasien.gejala}\nJenis Kelamin: {pasien.jenis_kelamin}\nAlamat: {pasien.alamat}\nNo Telepon: {pasien.no_telepon}")
                    return
        print("Data pasien tidak ditemukan.")

    def layani_pasien(self):
        self.lihat_daftar_pasien()
        try:
            id_pasien = int(input("Masukkan ID Pasien yang akan dilayani: "))
            pasien = next((p for p in self.pasien_list if p.id_pasien == id_pasien), None)
            if pasien:
                if not pasien.dilayani:
                    pasien.dilayani = True
                    print(f"Pasien {pasien.nama} telah dilayani.")
                else:
                    print(f"Pasien {pasien.nama} sudah pernah dilayani.")
            else:
                print("ID Pasien tidak ditemukan.")
        except ValueError:
            print("Input tidak valid. Masukkan angka ID pasien.")

# Inisialisasi sistem rumah sakit
rumah_sakit = RumahSakit()

# Tambahkan akun admin default
rumah_sakit.akun_list.append(Akun("admin", "admin123", "admin"))

# Tambahkan pasien-pasien awal
data_pasien = [
    ("Andi", 25, "Demam", "Laki-laki", "Jl. Mawar 1", "081234567890"),
    ("Budi", 30, "Batuk", "Laki-laki", "Jl. Melati 2", "081234567891"),
    ("Citra", 22, "Sakit Kepala", "Perempuan", "Jl. Anggrek 3", "081234567892"),
    ("Dewi", 28, "Mual", "Perempuan", "Jl. Kenanga 4", "081234567893"),
    ("Eko", 35, "Nyeri Dada", "Laki-laki", "Jl. Kamboja 5", "081234567894"),
    ("Fitri", 27, "Sesak Napas", "Perempuan", "Jl. Teratai 6", "081234567895"),
    ("Gita", 20, "Flu", "Perempuan", "Jl. Tulip 7", "081234567896"),
    ("Hadi", 40, "Pusing", "Laki-laki", "Jl. Lavender 8", "081234567897"),
    ("Intan", 18, "Batuk Berdarah", "Perempuan", "Jl. Dahlia 9", "081234567898"),
    ("Joko", 50, "Demam Tinggi", "Laki-laki", "Jl. Mawar 10", "081234567899")
]

for nama, usia, gejala, jenis_kelamin, alamat, no_telepon in data_pasien:
    rumah_sakit.pasien_list.append(Pasien(len(rumah_sakit.pasien_list) + 1, nama, usia, gejala, jenis_kelamin, alamat, no_telepon))
    rumah_sakit.akun_list.append(Akun(nama.split()[0].lower(), "1234", "user"))

# Tambahkan dokter-dokter awal dengan username berdasarkan nama depan
data_dokter = [
    ("Dr. Siti Aisyah", "Spesialis Anak", "081234567800"),
    ("Dr. Yogi Wijaya", "Spesialis Penyakit Dalam", "081234567801"),
    ("Dr. Budi Santoso", "Spesialis Bedah", "081234567802"),
    ("Dr. Fitri Amelia", "Spesialis Kulit dan Kelamin", "081234567803")
]

for nama, spesialis, no_telepon in data_dokter:
    username = nama.split()[1].lower()  # Ambil nama depan saja
    rumah_sakit.dokter_list.append(Dokter(len(rumah_sakit.dokter_list) + 1, nama, spesialis, no_telepon))
    rumah_sakit.akun_list.append(Akun(username, "1234", "dokter"))

# Menjalankan menu utama
rumah_sakit.menu()
