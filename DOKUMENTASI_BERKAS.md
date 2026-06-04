# 📁 Dokumentasi Berkas & Struktur Repositori (Kriteria 1)

Dokumen ini menjelaskan pembagian berkas secara terpisah untuk memenuhi standardisasi industri dan rubrik penilaian PIJAK.

### 1. Folder `.github/workflows/` & `.workflow/`
*   **`verify.yml`**
    Berkas konfigurasi otomatisasi MLOps (YAML) yang bertugas menyalakan server Ubuntu virtual, memasang *library* Python, dan memicu robot untuk memperbarui dataset bersih secara berkala.

### 2. Folder `Midterm_53_group_raw/`
*   **`Midterm_53_group.csv`**
    Dataset trafik jaringan mentah asli (*raw data*). Disimpan dalam bentuk sampel 100 baris pertama guna menghindari batasan ukuran unggah browser.

### 3. Folder `preprocessing/`
*   **`Eksperimen_Reza-Rahmawati.ipynb`**
    *Notebook* Google Colab utama tempat coretan analisis data, EDA, dan pembersihan data awal dilakukan.
*   **`automate_Reza-Rahmawati.py`**
    Skrip Python mandiri (*clean code*) hasil konversi untuk menjalankan fungsi pembersihan data secara otomatis.
*   **`dataset_preprocessing.csv`**
    File output data bersih terbaru yang siap digunakan untuk umpan pelatihan model machine learning.

### ⚡ Mekanisme Otomatisasi (GitHub Actions - 4 Poin Advance)
Setiap kali ada pengiriman kode (`git push`) ke cabang utama (`main`), robot GitHub akan otomatis mengeksekusi file `automate_Reza-Rahmawati.py` di server cloud, mencuci datanya, lalu memperbarui isi file `dataset_preprocessing.csv` secara mandiri.
