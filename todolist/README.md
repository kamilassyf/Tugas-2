 ## TUGAS 4 PBP
 
 ### Link deploy


 #### **Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?**

Cross-Site Request Forgery (CSRF) yang tertulis dengan tag {% csrf_token %} diimplementasikan untuk menghindari dari serangan. tag tersebut mengenerate token pada server ketika render page terjadi. Jika request yang diberikan tidak berisi token, maka tidak akan dieksekusi. 

Jika tidak menggunakan potongan kode tersebut, akan terjadi eror dimana akan terdapat beberapa route link yang bisa diakses orang lain. 



 #### **Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.**

Ya, kita bisa membuat elemen <form> secara manual dengan memanfaatkan method POST dan csrf token. Nantinya data yang diterima akan disimpan dan dapat diakses dengan method get() dengan parameter nama tag yang sudah dibuat. Misalnya jika membuat tag <input>, maka kita bisa menggunakan request.POST.get('username') untuk mengaksesnya.


#### **Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**

pertama, user melakukan submisi data yang akan dibawa oleh request dan isimpan ke dalam suatu variabel. data tersebut dapat diakses dengan menggunakan method requesst.POST.get(nama pada table). Kemudian data tersebut dapat diambil dari database untuk ditampilkan menggunakan nama models yang telah dibuat pada file todolist/models.py. Data dapat diakses menggunakan "Models".objects.filter(user=request.user). penggunaan filter ditujukan agar dapat sesuai dengan user sehingga yang masuk kedalam context agar dapat terrender ke dalam html. 
Kemudian objectsnya akan dilakukan looping dengan for loop agar dapat menampilkan data yang ingin ditampilkan. Untuk menampilkan data yang diinginkan dapat mengakses nama atribut yang diinginkan. Misalkan ingin mengakses title, maka dapat menulis

....
        <td>{{task.title}}</td>
....



#### **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**

