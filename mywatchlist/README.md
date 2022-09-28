 ## Tugas 3 PBP
 
 
 ### Jelaskan perbedaan antara JSON, XML, dan HTML!
 
 **JSON (JavaSript Object Notation)** merupakan penulisan data yang memilki struktur data yang sederhana dan mudah dipahami
 untuk dpahami. Json menggunakan REST APi dan hanya mendukung encoding UTF-8 dan UTF-16. Datanya berbentuk
 map data structure dimana keys dan valuenya berpasangan. 
 
 
**XML (Extensible Markup Language)** merupakan format pertukaran data yang digunakan untuk menyimpan dan membawa data dari satu
 aplikasi lain melalui internet. Tag pada XML adalah untuk mengontrol data. XML tidak memperhatikan tampilan karena didesain untuk mudah dipahami 
 mesin namun tetap bisa dibaca manusia. XML merupakan data yang berstruktur tree (hirarki), karena didesain untuk mudah dipahami mesin namun tetap 
 bisa dibaca manusia. XML mendukung banyak format encoding dan tidak mudah untuk dipahami seperti JSON 


**HTML (HyperText Markup Language)** merupakan penyyimpanan data yang mudah dipahami user. HTML biasanya digunakan sebagai penggambaran struktur sebuah website
 HTML menggunakan tag untuk memformat tampilan dengan memperhatikan tampilan. HTML merupakan markup laguange dan
 tidak memiliki sintaks penyimpanan dan pertukaran data seperti JSON dan XML
 
 ### Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

**Data delivery** memudahkan pemindahan data antara user dan server dengan cepat dan aman. Ketika pengimplementasian sebuah platform, pasti akan membutuhkan data untuk ditampilkan disihilah peran data delivery diatas bekerja. Data delivery dapat mengirimmkan data ke berbagai platform dengan mudah sehingga dapat diakses dengan struktur web yang berbeda. 

 ### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
 **1.** Membuat django-app bernama aplikasi baru bernama mywatchlist pada proyek Django Tugas 2 dengan perintah python manage.py startapp mywacthlist yang nantinya akan mengenerate secara automatis rangkaian file py awal.

 **2.** Mendaftarkan aplikasi mywatchlist ke dalam proyek Django dengan menambahkan aplikasi mywatchlst ke dalam file settings.py dalam folder project_django

 **3.** Membuat models pada mywatchlist/models.py yang berisikan Class WatchList dan atribut yang dibutuhkan untuk setiap tipe data 'watched', 'title', 'rating', 'release_date', dan review

 **4.** Membuat folder fixtures yang berisikan file json (initial_watchlist_data.json) yang didalamnya berisikan daftar film

**5.** Melakukan migrasi untuk menerapkan model yang telah dibuat ke dalam database Django lokal dan memasukan data pada json ke dalam database Django lokal 

**6.** Membuat fungsi show_watchlist, fungsi show_xml, show_json yang menerima parameter request serta fungsi show_xml_by_id  dan fungsi show_json_by_id yang menerima parameter request dan id

**7.** Melakukan import data yang dibutuhkan pada setiap file yang membutuhkan

**8.** Membuat folder 'templates' yang berisikan file html (watchlist.html) kemudian mengimplementasikan kode yang sesuai

**9.** Menambahkan path aplikasi mywatchilst ke 'urls.py' yang ada di project_django dan mywatchlist.


**10.** Melakukan add, commit, dan push terhadap perubahan yang dilakukan dan melakukan deployment ke aplikasi Heroku




 ### Screenshoot tiga URL di poin 6 menggunakan Postman
 
 #### **postmann html**
 
 ![This is an image](https://github.com/kamilassyf/Tugas-2/blob/main/mywatchlist/postmann_html.png)
 
 #### **Postmann json**
 
 ![This is an image](https://github.com/kamilassyf/Tugas-2/blob/main/mywatchlist/postmann_json.png)
 
 #### **postmann xml**
 ![This is an image](https://github.com/kamilassyf/Tugas-2/blob/main/mywatchlist/postmann_xml.png)