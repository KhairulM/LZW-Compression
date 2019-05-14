# LZW - Compression
## Note 
File yang terkompress akan bertipe .txt, sehingga untuk melakukan decompressing, input file .txt dengan nama yang sama dengan file yang di-compress

## Latar Belakang
Pengembangan aplikasi yang berkelanjutan (*sustainable*) menjadi sebuah kejaran yang semakin dicari pada akhir-akhir ini. Penggunaan sumberdaya diatur sedemikian rupa agar dapat terbentuk aplikasi yang sehemat mungkin, termasuk penggunaan energi. Terdapat berbagai metode untuk meningkatkan efisiensi sebuah aplikasi, salah satunya adalah mengurangi penggunaan *storage*. Metode yang aktif dikembangkan dan merupakan salah satu yang paling umum untuk diimplementasikan adalah kompresi.

Algoritma kompresi LZW (Lempel–Ziv–Welch) adalah sebuah metode kompresi *lossless* yang dibuat oleh Abraham Lempel, Jacob Ziv, and Terry Welch pada tahun 1970-1980-an. Konsep algoritma kompresi ini adalah mengurangi ukuran file (byte) dengan menggunakan *table-based lookup algorithm*. Algoritma ini merupakan pengembangan dari algoritma kompresi LZV yang biasa digunakan untuk file dengan format GIF, TIFF. Kompresi LZW juga dapat digunakan untuk kompresi file teks.

## Spesifikasi
Lakukan fork pada repository ini untuk mengerjakan, dan lakukan merge request untuk mengumpulkan.

Buatlah dalam bahasa pemrograman **_Python_** atau **_Rust_**, sebuah aplikasi yang dapat melakukan kompresi LZW dengan rincian sebagai berikut:

1. Dapat membaca file jenis apapun dengan format `python main [compress|decompress] input.gif` untuk **Python**, dan `cargo run main [compress|decompress] input.gif` untuk **Rust**.
2. Dapat melakukan kompresi dan dekompresi sesuai parameter yang diberikan pada eksekusi program. Kompresi dilakukan dengan memanggil fungsi bernama `doCompress` dan dekompresi dilakukan dengan memanggil fungsi bernama `doDecompress`. Hasil file (termasuk nama) setelah dilakukan kompresi dan dekompresi harus tetap sama.
3. Mengeluarkan file output dengan nama bebas.
4. Diutamakan optimal untuk file GIF, TIFF, dan TXT.
5. **_Dilarang menggunakan *library* sekali jadi seperti algoritma kompresi langsung, algoritma harus dibuat sendiri dari awal._**
6. Gunakanlah sesedikit mungkin library.

## Bonus
Terdapat bonus pengerjaan jika bahasa yang digunakan adalah bahasa **Rust**

## Penilaian

- Kebenaran fungsionalitas program
- Kerapihan kode, *repository* dan README.

Nilai maksimum yang bisa didapatkan adalah **1600 (2600 dengan bonus)** poin. <br>

## Referensi Pengerjaan
1. https://users.cs.cf.ac.uk/Dave.Marshall/Multimedia/node214.html
2. https://www.dspguide.com/ch27/5.htm
3. https://www.geeksforgeeks.org/lzw-lempel-ziv-welch-compression-technique/
4. https://www.rust-lang.org/learn/get-started
5. https://www.tutorialspoint.com/rust
