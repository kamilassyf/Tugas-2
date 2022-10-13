# Tugas 6

## **Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.**

asynchronous programming dan synchronous programming adalah dua jenis model pemrograman. Asynchronous programming dengan synchronous programming memiliki perbedaan. Asynchronous yang merujuk pada kata “async” merupakan program yang bisa dijalankan secara paralel dan membutuhkan parameter atau perintah untuk dijalankan. Asynchronous programming dapat berjalan bersamaan tanpa perlu menunggu proses lain selesai terlebih dahulu. Synchronous programming adalah model pemgrograman yang membutuhkan pengguna untuk menunggu server dan data terproses terlebih dahulu sebelum melanjutkan interaksi dan hanya dapat menjalankan satu operasi (single) dalam satu waktu dengan urutan yang tidak fleksibel

## **Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.**

Paradigma event-driven programming adalah paradigma pemrograman yang alur programnya ditentukan oleh event yang merupakan output dari tindakan user.  Contoh dari event-driven programming adalah ketika user menekan/meng-klik tombol, atau mengeser mouse.  Penerapan event-driven programming pada tugas 6 kali ini adalah implementasi button/tombol ‘create’ untuk menambahkan task. Ketika tombol ‘create’ ditekan, akan muncul event form yang akan mengiriim title dan description ke database oleh AJAX dan akan diperbaharui data todolist dari server secara asynchronous.

## **Jelaskan penerapan asynchronous programming pada AJAX.**

Penerapan asynchronous programming pada AJAX membuat web tidak perlu untuk reload halaman secara keseluruhan ketika terjadi perubahan kecil pada data. Implementasi ajax get dan ajax post juga merupakan penerapan dari asynchronouse programming.ajax get dan post akan melakukan trigger ketika html mengirim method get atau post yang diterima oleh ajax. Kemudian data akan dikirimkan tanpa melewati proses reload browser

## **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

**ajax get**
1. Membuat fungsi show_ajax pada file view.py dalam folder todolist yang akan mereturn JSONResponse data
2. Membuat path /todolist/json pada  file urls.py folder todolist yang akan mengarah pada fungsi show_ajax 
3. Menambahkan AJAX GET melalui fungsi get data pada todolist.html untuk mengambil data


**ajax post**
1. Membuat modal pada todolist.html 
2. Membuat fungsi add_ajax untuk menambahkan task baru ke dalam database
3. Membuat path /todolist/add pada file urls.py folder todolist yang akan mengarah pada fungsi add_ajax 
4. Membuat tombol create untuk menutup modal jika tugas sudah ditambahkan


