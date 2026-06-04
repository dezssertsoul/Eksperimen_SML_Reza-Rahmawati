# Eksperimen Supervised Machine Learning - Klasifikasi Trafik Jaringan

Proyek ini merupakan implementasi eksperimen *Supervised Machine Learning* (SML) untuk melakukan klasifikasi pada dataset trafik jaringan (`Midterm_53_group`). Repositori ini disusun dengan standar struktur folder industri serta dilengkapi dengan otomatisasi *pipeline preprocessing* berbasis MLOps menggunakan GitHub Actions.

---

## 📁 Struktur Repositori

Sesuai dengan standardisasi dan rekomendasi struktur folder, repositori ini disusun sebagai berikut:

*   **`.github/workflows/`** : Berisi berkas konfigurasi GitHub Actions (`verify.yml`) untuk memicu otomatisasi *pipeline* secara berkala.
*   **`.workflow/`** : Folder duplikasi konfigurasi sesuai dengan teks instruksi kriteria *assignment*.
*   **`Midterm_53_group_raw/`** : Berisi dataset mentah (*raw data*) asli (`Midterm_53_group.csv`) yang diunduh langsung dari Kaggle (disajikan dalam bentuk *sample data* 100 baris pertama guna optimalisasi repositori).
*   **`preprocessing/`** : Folder utama pemrosesan data, berisi:
    *   `Eksperimen_Reza-Rahmawati.ipynb` (Google Colab Notebook eksperimen)
    *   `automate_Reza-Rahmawati.py` (Skrip otomatisasi mandiri)
    *   `dataset_preprocessing.csv` (Hasil akhir dataset yang telah dibersihkan dan siap latih)

---

## 🛠️ Langkah Preprocessing & Otomatisasi (Kriteria Skilled)

Pemrosesan data dilakukan secara otomatis melalui skrip `automate_Reza-Rahmawati.py` dengan tahapan sebagai berikut:
1.  **Data Loading**: Membaca dataset mentah dengan opsi penanganan *bad lines* untuk mencegah kegagalan parser.
2.  **Data Cleaning**: Menghapus baris data yang duplikat secara logis untuk menjaga integritas model.
3.  **Feature Scaling**: Melakukan standardisasi fitur numerik panjang paket (`Length`) menggunakan `StandardScaler` dari *library* scikit-learn.
4.  **Auto-Export**: Menyimpan data bersih terbaru secara langsung ke dalam format `.csv`.

---

## ⚡ GitHub Actions Workflow Pipeline (Kriteria Advance)

Repositori ini telah mengimplementasikan **CI/CD Pipeline (MLOps)** tingkat lanjut melalui GitHub Actions:
*   **Trigger**: Berjalan otomatis setiap kali ada aktivitas pengiriman kode (`git push`) ke cabang utama (`main`).
*   **Proses Cloud**: Sistem akan membangun lingkungan Python virtual di server Ubuntu, menginstal seluruh *dependencies* (`pandas`, `scikit-learn`), mencari letak skrip otomatisasi secara dinamis, lalu mengeksekusinya.
*   **Output**: Hasil pemrosesan data bersih terbaru (`dataset_preprocessing.csv`) akan di-commit dan di-push kembali ke repositori secara otomatis oleh `GitHub Action Bot`.

---

## 🚀 Cara Menjalankan Skrip Secara Lokal

Jika Anda ingin menjalankan otomatisasi *preprocessing* ini di komputer lokal Anda, ikuti langkah berikut:

1. Clone repositori ini:
```bash
   git clone [https://github.com/dezssertsoul/Eksperimen_SML_Reza-Rahmawati.git](https://github.com/dezssertsoul/Eksperimen_SML_Reza-Rahmawati.git)
