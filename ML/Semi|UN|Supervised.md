### DENETİMLİ, DENETİMSİZ VE YARI DENETİMLİ ALGORİTMALAR 

----

<p align="center">
  <b> DENETİMLİ (SUPERVISED) ÖĞRENME</b><br>
</p>


* Denetimli öğrenme, girdi değişkenlerinin (x) ve bir çıktı değişkeninin (Y) olduğu ve girdiden çıktıya eşleme işlevini öğrenmek için bir algoritma kullandığınız yerdir.

<p align="center">
  <b> Y = f (X) </b><br>
</p>

* Hedef, haritalama fonksiyonunu o kadar iyi tahmin etmektir ki, yeni giriş verileriniz (x) olduğunda, bu verinin çıkış değişkenlerini (Y) tahmin edebilirsiniz. Buna **denetimli öğrenme** denir, çünkü **eğitim veri setinden bir algoritma öğrenme süreci, öğrenme sürecini denetleyen bir öğretmen** olarak düşünülebilir. Doğru cevapları biliyoruz, algoritma tekrarlı olarak eğitim verileri üzerinde tahminler yapıyor ve öğretmen tarafından düzeltiliyor. **Algoritma kabul edilebilir bir performans seviyesine ulaştığında öğrenme durur.**

* Denetlenen öğrenme sorunları daha sonra regresyon ve sınıflandırma problemleri olarak gruplandırılabilir:
    
    * **Sınıflandırma** : Sınıflandırma problemi, çıktı değişkeninin “kırmızı” veya “mavi” veya “hastalık” ve “hastalık yok” gibi bir kategori olduğu durumdur.
    * **Regresyon** : Regresyon problemi, çıktı değişkeninin “dolar” veya “ağırlık” gibi gerçek bir değer olması durumudur.
--------

<p align="center">
  <b> DENETİMSİZ (UNSUPERVISED) ÖĞRENME</b><br>
</p>

* Denetimsiz öğrenme, **yalnızca girdi verilerinizin (X) olduğu** ve **karşılık gelen çıktı değişkenlerinin olmadığı** yerdir. 
* **Denetimsiz öğrenmenin amacı**, veriler hakkında daha fazla bilgi edinmek için verilerdeki **temel yapıyı veya dağılımı modellemektir**.
* Bunlara denetlenmeyen öğrenme denir, çünkü **yukarıda denetlenen öğrenmeden farklı olarak doğru cevaplar yoktur ve öğretmen yoktur.** Algoritmalar, verilerdeki ilginç yapıyı keşfetmek ve sunmak için kendi aygıtlarına bırakılmıştır.

* Denetimsiz öğrenme problemleri kümelenme ve ilişkilendirme problemleri içinde daha da gruplandırılabilir.
    * **Kümelenme(Clustering)** : Kümelenme sorunu, müşterileri satın alma davranışına göre gruplama gibi verilerdeki doğal gruplamaları keşfetmek istediğiniz yerdir.
    * **İlişkilendirme(Association)** : İlişkilendirme kuralı öğrenme sorunu, X'i alan kişiler de Y alma eğilimi gibi verilerinizin büyük bölümlerini tanımlayan kuralları keşfetmek istediğiniz yerdir.
---

<p align="center">
  <b> YARI-DENETİMLİ (SEMI-SUPERVISED) ÖĞRENME</b><br>
</p>

* **Çok miktarda girdi verisine (X) sahip olduğunuz** ve **verilerin yalnızca bir kısmının (Y) etiketli** olduğu problemlere yarı denetimli öğrenme problemleri denir.
* Birçok gerçek dünya makine öğrenme problemi bu alana girer. **Bunun nedeni, etki alanı uzmanlarına erişim gerektirebileceği için verileri etiketlemenin pahalı veya zaman alabilmesidir. Etiketlenmemiş verilerin toplanması ve saklanması ucuz ve kolaydır.**
* *Girdi değişkenlerindeki yapıyı keşfetmek ve öğrenmek için denetimsiz öğrenme tekniklerini kullanabilirsiniz.*
* *Etiketlenmemiş veriler için en iyi tahmin tahminlerini yapmak için denetimli öğrenme tekniklerini kullanabilir, bu verileri denetlenen öğrenme algoritmasına eğitim verisi olarak geri besleyebilir ve modeli yeni görünmeyen veriler üzerinde tahminler yapmak için kullanabilirsiniz.*

-----

<p align="center">
  <b> ÖZET </b><br>
</p>

* **Denetimli** : Tüm veriler etiketlenir ve algoritmalar girdi verilerinden çıktıyı tahmin etmeyi öğrenir.
* **Denetimsiz** : Tüm veriler etiketlenmemiş ve algoritmalar girdi verilerinden doğal yapıyı öğreniyor.
* **Yarı Denetimli** : Bazı veriler etiketlenir, ancak çoğu etiketsizdir ve denetlenen ve denetlenmeyen tekniklerin bir karışımı kullanılabilir.
