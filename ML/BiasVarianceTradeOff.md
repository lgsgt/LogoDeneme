### MAKİNE ÖĞRENMESİNDE EĞİLİM/VARYANS TAKASINA GİRİŞ 
----

<p align="center">
  <b> EĞİLİM/SAPMA ve VARYANSA GENEL BAKIŞ</b><br>
</p>


* Denetimli makine öğreniminde bir algoritma, eğitim verilerinden bir model öğrenir. Denetlenen herhangi bir makine öğrenme algoritmasının amacı, giriş verileri (X)'e verilen çıkış değişkeni (Y) için eşleme fonksiyonunu (f) en iyi şekilde tahmin etmektir. Eşleme işlevi genellikle hedef işlev olarak adlandırılır, çünkü belirli bir denetimli makine öğrenme algoritmasının yaklaşık olarak hesaplamayı hedeflediği işlevdir.

* Herhangi bir makine öğrenme algoritması için tahmin hatası üç bölüme ayrılabilir:
* 
    * **Eğilim/Sapma/Ön Yargı Hatası**
    * **Varyans Hatası**
    * **İndirgenemez Hata**

* **İndirgenemez hata**, hangi algoritmanın kullanıldığına bakılmaksızın **azaltılamaz.** Problemin **seçilen çerçevesinden kaynaklanan hatadır** ve **giriş değişkenlerinin çıkış değişkenine eşlenmesini etkileyen bilinmeyen değişkenler gibi faktörlerden** kaynaklanabilir.

--- 

<p align="center">
  <b> EĞİLİM/SAPMA/ÖN YARGI (BIAS) HATASI </b><br>
</p>

* Önyargı, **hedef işlevi öğrenmeyi kolaylaştırmak için bir model tarafından yapılan basitleştirici varsayımlardır.**
* Genel olarak, **parametrik algoritmalar, öğrenmeyi hızlı ve anlaşılması daha kolay ancak genellikle daha az esnek kılan yüksek önyargıya sahiptir.** Buna karşılık, algoritmaların önyargılarının sadeleştirici varsayımlarını yerine getiremeyen **karmaşık problemlerde tahmin performansı düşüktür**.

    * **Düşük Sapma** : Hedef işlevin şekli hakkında daha az varsayım önerir.
    * **Yüksek Sapma** : Hedef fonksiyonun şekli hakkında daha fazla varsayım önerir.

----

<p align="center">
  <b> VARYANS HATASI </b><br>
</p>



* Varyans, farklı egzersiz verileri kullanılıyorsa hedef fonksiyonun tahmininin değişeceği miktardır.
* Hedef fonksiyon, eğitim verilerinden bir makine öğrenme algoritması tarafından tahmin edilir, bu nedenle algoritmanın **biraz farklılık göstermesini beklemeliyiz**. **İdeal olarak, bir eğitim veri setinden diğerine çok fazla değişmemelidir**, bu da algoritmanın girdiler ve çıktı değişkenleri arasındaki **altta yatan,gizli eşlemeyi seçmekte iyi olduğu anlamına gelir.
* **Varyansı yüksek** olan makine öğrenme algoritmaları, **eğitim verilerinin özelliklerinden güçlü bir şekilde etkilenir**. Bu, eğitimin özelliklerinin **haritalama fonksiyonunu karakterize etmek için kullanılan parametre sayısını ve türlerini etkilediği anlamına gelir**.
    
    * **Düşük Varyans** : Eğitim veri setinde değişikliklerle hedef fonksiyonun tahmininde küçük değişiklikler önerir.
    * **Yüksek Varyans** : Eğitim veri setinde değişikliklerle hedef fonksiyonun tahmininde büyük değişiklikler önerir.
    
* Genel olarak, çok fazla esnekliğe sahip olan parametrik olmayan makine öğrenme algoritmaları yüksek bir varyansa sahiptir. 
--------

<p align="center">
  <b> SAPMA/EĞİLİM - VARYANS TAKASI </b><br>
</p>

* **Denetimli herhangi bir makine öğrenme algoritmasının amacı, düşük sapma ve düşük varyansa ulaşmaktır. Buna karşılık algoritma iyi tahmin performansı sağlamalıdır.**
* Yukarıdaki örneklerde genel bir eğilim görebilirsiniz:

    * **Parametrik veya doğrusal** makine öğrenme algoritmaları genellikle **yüksek önyargıya, ancak düşük bir varyansa sahiptir.**
    * **Parametrik olmayan veya doğrusal olmayan** makine öğrenme algoritmaları **genellikle düşük yanlılığa, ancak yüksek bir varyansa sahiptir.**
    
* ***Makine öğrenmesi algoritmalarının parametreleştirilmesi çoğu zaman önyargı ve varyansı dengelemek için bir mücadeledir.***
    
* Aşağıda, belirli algoritmalar için bias-varyans değişimini yapılandırmanın iki örneği verilmiştir:

    * **k-nearest neighbors** algoritması düşük önyargıya ve yüksek varyansa sahiptir, ancak takas k tahminini artıran ve sonuçta modelin önyargısını artıran komşu sayısını artırarak değiştirilebilir.
    * **support vector machine** algoritması düşük önyargıya ve yüksek değişkenliğe sahiptir, ancak alıştırma, önyargıyı artıran ancak varyansı azaltan eğitim verilerinde izin verilen marjın ihlal sayısını etkileyen C parametresini artırarak değiştirilebilir.
    
-----

* **Makine öğrenmesinde önyargı ve varyans arasındaki ilişkiden kaçış yoktur.**

    * Önyargıyı artırmak, varyansı azaltacaktır.
    * Varyansı artırmak yanlılığı azaltacaktır.

* Bu iki kaygı ile seçtiğiniz algoritmalar ve bunları yapılandırmayı seçtiğiniz yöntem arasında bir takas var, bu takasta sorununuzu çözmek için farklı dengeler buluyorsunuz.

* Gerçekte, gerçek sapma ve varyans hata terimlerini hesaplayamayız çünkü asıl hedef hedef fonksiyonunu bilmiyoruz. Bununla birlikte, bir çerçeve olarak, önyargı ve varyans, makine öğrenmesi algoritmalarının öngörücü performans arayışındaki davranışını anlama araçlarını sağlar.
