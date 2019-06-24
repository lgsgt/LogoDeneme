### MAKİNE ÖĞRENME ALGORİTMALARI NASIL ÇALIŞIR ? (HOW MACHINE LEARNING ALGORITHMS WORKS?)
----

##### Bir İşlevi Öğrenmek (Learning a Function)
- Makine öğrenme algoritmaları, giriş değişkenlerini (X) bir çıkış değişkenine (Y) en iyi eşleyen bir hedef fonksiyonunu (f) öğrenme olarak tanımlanmaktadır.

<p align="center">
  <b>Y = f (X)</b><br>
</p>

* (F) fonksiyonunun neye benzediğini veya şeklini bilmiyoruz. Yapsaydık, doğrudan kullanırdık ve makine öğrenme algoritmaları kullanarak veriden öğrenmemize gerek kalmazdı.
* Giriş verilerinden (X) bağımsız bir hata da var (e).

<p align="center">
  <b>Y = f (X) + e</b><br>
</p>

* Bu hata, X'ten Y'ye en iyi eşleştirmeyi yeterince nitelemek için yeterli özniteliklere sahip olmama gibi bir hata olabilir. Hedef fonksiyonunu (f) tahmin etmede ne kadar iyi olursa olsun, bu hatayı azaltamazsak, bu hataya indirgenemez hata adı verilir.

##### Tahmin Yapmak İçin Bir İşlevi Öğrenmek (Learning a Function To Make Prediction )
- En yaygın makine öğrenmesi türü, yeni X için Y'nin tahminlerini yapmak üzere Y = f (X) eşlemesini öğrenmektir. Buna tahmine dayalı modelleme veya tahmine dayalı analitik denir ve hedefimiz en doğru tahminin mümkün olmasını sağlamaktır. Bu nedenle, öğrendiğimiz **fonksiyonun şekli (f) ile gerçekten ilgilenmiyoruz, sadece doğru tahminlerde bulunuyoruz.**

* Verilerdeki ilişki hakkında daha fazla bilgi edinmek için Y = f (X) eşlemesini öğrenebiliriz ve buna **istatistiksel çıkarım** denir. Amaç bu olsaydı, doğru tahminleri yapmak için yukarıda öğrenilen modeli ve (f) şeklini anlamak için daha basit yöntemler ve değer kullanırdık.

* Bir işlevi (f) öğrendiğimizde, formunu elimizdeki verilerden tahmin ediyoruz. Bu nedenle, bu tahminde hata olacaktır. X'in verdiği Y'nin altında yatan varsayımsal en iyi eşleşme için mükemmel bir tahmin olmayacak.

* Uygulamalı makine öğreniminde, **temel fonksiyonun tahminini iyileştirmek ve terim olarak model tarafından yapılan tahminlerin** performansını iyileştirmek için **çok zaman harcanmaktadır**.


##### İşlevi Öğrenmek İçin Teknikler (Techniques For Learning a Function)

* Makine öğrenme algoritmaları, giriş değişkenlerini (X) verilen çıkış değişkenini (Y) tahmin etmek için hedef fonksiyonun (f) tahmin edilmesine yönelik tekniklerdir.

* Farklı gösterimler, lineer olup olmadığı gibi öğrenilen fonksiyonun şekli hakkında farklı varsayımlarda bulunur.

* Farklı makine öğrenme algoritmaları, **işlevin şekli ve yapısı ve bir gösterimi yaklaşık olarak en iyi duruma getirmek için en iyi yöntemle ilgili farklı varsayımlarda bulunur.** Makine öğrenmesi probleminde farklı algoritmalardan oluşan bir takım denemenin çok önemli olmasının nedeni budur, çünkü **elimizden önce, yaklaştırmaya çalıştığımız temel fonksiyonun yapısını tahmin etmede hangi yaklaşımın en iyi olacağını bilmiyoruz.**
----
##### ÖZET

* Bu yazıda, öngörülü modelleme için tüm makine öğrenme algoritmalarının amacını açıklayan **temel prensibi**, Makine öğrenme algoritmalarının, **giriş değişkenleri (X) veya Y = f (X) verilen çıkış değişkenlerinin (Y) eşleşme(mapping) fonksiyonunu (f) tahmin etmeye çalıştığını** öğrendiniz. Ayrıca **farklı makine öğrenme algoritmalarının,** temel fonksiyonun şekli hakkında **farklı varsayımlarda bulunduğunu** da öğrendiniz. 
