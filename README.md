# Wiki Population ETL

ETL pipeline untuk mengambil, transformasi, dan memuat data populasi negara dari Wikipedia ke database PostgreSQL.

## Fitur

- **Extract**: Mengambil data HTML dari halaman Wikipedia.
- **Transform**: Mengubah tabel HTML menjadi DataFrame Pandas yang bersih.
- **Load**: Memasukkan data ke tabel `population` di database PostgreSQL.
- **Testing**: Pengujian otomatis setiap tahapan ETL menggunakan pytest.

## Struktur Folder

```
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
├── config/
│   └── config.yaml
├── main.py
├── Dockerfile
└── README.md
```

## Persiapan & Instalasi

1. **Klon repo**
   ```
   git clone https://github.com/zidanlf/wiki-population-etl.git
   cd wiki-population-etl
   ```

2. **Siapkan file konfigurasi**
   - Edit `config/config.yaml` sesuai kebutuhan (URL scraping & konfigurasi database PostgreSQL).
  
## Jalankan dengan Docker di WSL

Ikuti urutan berikut untuk menjalankan pipeline dan testing dengan Docker yang terintegrasi WSL2:

### 1. Build image dan setup layanan dengan Docker Compose
```
docker compose build
```

### 2. Jalankan semua service (database & ETL)
```
docker compose up -d
```

### 3. Jalankan testing otomatis di container ETL
```
docker compose run etl pytest -v
```

### 4. Jalankan pipeline utama (main.py) di container ETL
```
docker compose run etl python main.py
```

### 5. Masuk ke container database PostgreSQL
```
docker exec -it wiki_etl-db-1 psql -U postgres -d wiki_db
```

### 6. Cek tabel dan data hasil ETL
Di dalam prompt `psql`, jalankan:
```
\d
SELECT * FROM population LIMIT 5;
```

### 7. (Opsional) Matikan semua container setelah selesai
```
docker compose down
```

**Catatan:**
- Pastikan file konfigurasi database di `config/config.yaml` sudah sesuai dengan pengaturan di docker-compose.
- Untuk keluar dari prompt PostgreSQL (`psql`), ketik `\q`.
