### Link menuju aplikasi Heroku 

Halaman utama   : https://tugas-2-syifa.herokuapp.com/

Halaman katalog : https://tugas-2-syifa.herokuapp.com/katalog/ 


### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
![This is an image](https://github.com/kamilassyf/Tugas-2/blob/main/diagram.png)


### Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

virtual environment dibutuhkan untuk menjaga isi dari environment agar program tidak terpengaruh oleh hal lain. 
virtual environment akan mengisolasi dependecies yang dbutuhkan

jika tidak menggunakan virtual environment ketika membuat aplikasi web berbasis Django akan mempengaruhi fungsionalitas program. 
jika tidak menggunakan venv, apabila terdapat update tertentu akan mempengaruhi program sehingga akan terdapat perbedaan atau bahkan akan membuat program tidak bisa dijalankan

### Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
1. pada fungsi views.py saya membuat fungsi show_katalog yang menerima parameter request yang kemudian diteruskan ke fungsi render yang telah di import sebelumnya. 
Pada fungsi tersebut akan mengambil data pada CatalogItems dan menambahkan variabel seperti npm dan id mahasiswa (npm) yang disimpan ke dalam 
variabel context yang selanjutnya fungsi akan mereturn dengan parameter request, file htlm katalog, dan context 

2. pada file urls.py akan melakukan routing terhadap fungsi show_katalog. Pada file urls.py pada folder project_django, 
saya menbahkan 'katalog/' dan include('katalog.urls') agar bisa diakses.

3. untuk memetakan data yang didapat ke dalam HTML, saya melakukan loaddata file json dan mengedit 
file katalog.html sehingga berisikan for looping sehingga data yang ada dapat ditampilkan.

4. Pada tahap deployment ke Heroku, langkah pertama adalah membuat app baru lalu 
saya menambahkan Api Key dan App Name kesecret repository pada github. Kemudian akan dapat terhubung secara langsung

