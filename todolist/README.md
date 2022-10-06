 ## TUGAS 4 PBP
 
 ### 🔗 Link deploy
https://tugas-2-syifa.herokuapp.com/todolist/login/

https://tugas-2-syifa.herokuapp.com/todolist/register/

https://tugas-2-syifa.herokuapp.com/todolist/create_task/

https://tugas-2-syifa.herokuapp.com/todolist/logout/




 #### **Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?**

Cross-Site Request Forgery (CSRF) yang tertulis dengan tag {% csrf_token %} diimplementasikan untuk menghindari dari serangan. tag tersebut mengenerate token pada server ketika render page terjadi. Jika request yang diberikan tidak berisi token, maka tidak akan dieksekusi. 

Jika tidak menggunakan potongan kode tersebut, akan terjadi eror dimana akan terdapat beberapa route link yang bisa diakses orang lain. 



 #### **Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.**

Ya, kita bisa membuat elemen <form> secara manual dengan memanfaatkan method POST dan csrf token. Nantinya data yang diterima akan disimpan dan dapat diakses dengan method get() dengan parameter nama tag yang sudah dibuat. Misalnya jika membuat tag <input>, maka kita bisa menggunakan request.POST.get('username') untuk mengaksesnya.


#### **Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**

pertama, user melakukan submisi data yang akan dibawa oleh request dan isimpan ke dalam suatu variabel. data tersebut dapat diakses dengan menggunakan method requesst.POST.get(nama pada table). Kemudian data tersebut dapat diambil dari database untuk ditampilkan menggunakan nama models yang telah dibuat pada file todolist/models.py. Data dapat diakses menggunakan "Models".objects.filter(user=request.user) penggunaan filter ditujukan agar dapat sesuai dengan user sehingga yang masuk kedalam context agar dapat terrender ke dalam html. 

Kemudian objectsnya akan dilakukan looping dengan for loop agar dapat menampilkan data yang ingin ditampilkan. Untuk menampilkan data yang diinginkan dapat mengakses nama atribut yang diinginkan. Misalkan ingin mengakses title, maka dapat menulis


. . . . 
        
        <td>{{task.title}}</td>

. . . .



#### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
 
1. Membuat aplikasi baru bernama todolist pada proyek tugas Django sebelumnya (tugas-2)

2. Memasukan path todolist ke dalam urlpattern pada file urls.py pada folder project-django

3. Membuat model Task yang terdapat atribut user, date, title, description pada file models.py pada folder todolist. Setelah itu melakukan migration data 

4. Membuat fungsi register, login_user, dan logout_user pada file view.py di folder todolist

5. Membuat folder 'templates' lalu membuat file 'todolist.html' yang akan menampilkan daftar todo, button untuk tambah task, hapus, dan logout 

6. Membuat halaman baru yaitu todolist/create_task untuk membuat form yang meminta user untuk mengisi task dan deskripsi untuk todo yang ingin ditambahkan pada data

7. Menambahkan 'path' pada 'urls.py' pada folder app 'todolist'

8. Melakukan 'add', 'commit', dan 'push' ke repositoy github. karena repository sudah terhubung maka app dapat langsung diakses melalui Heroku

9. 2 akun dan 3 dummy data di situs web Heroku

![This is an image](https://github.com/kamilassyf/Tugas-2/blob/64f5973201d315d611671b9f60975477a62c8c94/todolist/todo.png)

![This is an image](https://github.com/kamilassyf/Tugas-2/blob/main/todolist/todotodo.png)

## Tugas 5

#### **Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**

**Inline CSS:** 
Inline CSS merupakan kode yang ditulis secara langsung pada atribut elemen HTML. Penulisannya pada atribut style dari elemen HTML yang diinginkan. 

kelebihan:
        
1. Efisien apabila ingin langsung melihat perubahan pada kode dengan cepat
2. Proses laod website akan berjalan lebih cepat
3. Penulisan styling akan lebih spesifik pada satu elemen 

kekurangan:
1. struktur file akan terlihat berantakan karena banyaknya penerapan style yang ada
2. tidak efektif jika dterapkan pada banyak tag HTML karena akan terjadi styling berulang - ulang


**Internal CSS:**
Internal CSS merupakan kode yang ditulis dalam tag `<style>` pada file yang sama. Untuk menggunakan styling CSS dengan internal CSS, kita bisa dengan menggunakan ID, class, atau hanya elemen

kelebihan:
1. Tidak perlu membuat file baru karena styling dilakukan pada file yang sama. 
2. Perubahan hanya terjadi pada satu page saja sehingga memungkinkan untuk membuat page yang berbeda satu sama lainnya


kekurangan:
1. Tidak efisian jika ingin membuat styling CSS yang sama pada lebih dari satu file


**External CSS:**
External CSS merupakan kode yang ditulis pada file yang berbeda. file tersebut berekstensi `.css`. Untuk menghubungkan kedua file perlu menambahkan `<link>` kemudian mereferensikan ke path file berada pada tag `<head>`.



kelebihan:
1. Struktur file HTML akan terlihat lebih rapi dan mudah dipahami
2. Efisiensi jika ingin diterapkan untuk lebih dari satu halaman website
3. Durasi loading website akan lebih cepat


kekurangan:
1. Membutuhkan waktu lebih untuk mengakses styling CSS karena terdapat pada file yang berbeda




#### **Jelaskan tag HTML5 yang kamu ketahui.**
`<body>` : mendefinisikan badan dari document

`<button>` : membuat button yang bisa diketik

`<div>` : membagi menjadi beberapa divisi atau section pada document

`<form>` : mendefinisikan form HTML untuk input user

`<head>` : mendefinisikan bagian head dari document yang biasanya berisi title/judul

`<html>` : mendefinisikan root dari file document HTML

`<img>` : mempresentasikan foto/gambar

`<input>` :  mendefinisikan control untuk input

`<label>` :mendefinisikan label untuk `<input>` control

`<title>` : mendifinikan title/judul dari file document





#### **Jelaskan tipe-tipe CSS selector yang kamu ketahui.**

Terdapat 5 tipe CSS selector, yaitu:

1. CSS element selectors: CSS element selectors menyeleksi element HTML berdasarkan nama elementnya

2. CSS id selectors: CSS id selector akan memilih element yang spesifik dengan menggunakan id atribut dari element HTML

3. CSS class selectors: CSS class selectors akan memilih element HTML dengan atribut class yang spesifik

4. CSS Universal selectors: CSS universal selectors akan memilih elemen HTML pada page

5. CSS Grouping selectors: CSS grouping selectors akan memilih seluruh elemen HTML dengan definisi style yang sama. 



#### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

1. membuat styling dengan menggunakan CSS. Saya menggunakan styling dengan Internal CSS. Saya membuat tag `<style>`  yang isinya terdapat beberapa styling kemudian saya memanggil styling tersebut pada elemen  yang diinginkan dengan  `class= "styling"`

2. Membuat cards pada halaman utama todo list untuk menampilkan task. Kemudian saya menambahkan for-loop untuk menampilkan task dengan format yang sama

3. Membuat keempat halaman menjadi responsive dengan cara mengatur viewport yang terdapat pada `base.html` yang telah diextends oleh file HTML lainnya. Kemudian menambahkan `{% extends 'base.html'%}` pada setiap file html

4. Menambahkan efek hover pada cards dengan cara membuat class `card:hover` pada todolist.html 