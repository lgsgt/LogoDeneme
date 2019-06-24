### Makine Öğrenmesi Algoritmaları İle OVERFITTING ve UNDERFITTING
----

<p align="center">
  <b> MAKİNE ÖĞRENMESİNDE YAKLAŞIK HEDEF FONKSİYONU </b><br>
</p>


* Denetimli makine öğrenmesi, giriş değişkenlerini (X) bir çıkış değişkenine (Y) eşleştiren bir hedef fonksiyona (f) yaklaşmak olarak en iyi şekilde anlaşılır.

<p align="center">
  <b> Y = f (X) </b><br>
</p>


* Bu karakterizasyon, sınıflandırma ve tahmin problemlerinin kapsamını ve bunları çözmek için kullanılabilecek makine algoritmalarını açıklar.

* Hedef fonksiyonun eğitim verilerinden öğrenilmesinde önemli bir husus, **modelin yeni verilere ne kadar iyi genellediğidir**. **Genelleme önemlidir, çünkü topladığımız veriler sadece bir örnek, eksik ve gürültülüdür.**

--- 

<p align="center">
  <b> MAKİNE ÖĞRENMESİNDE GENELLEME </b><br>
</p>

* Makine öğreniminde hedef fonksiyonun eğitim verilerinden öğrenilmesini **tümevarışsal öğrenme** olarak tanımlarız.
* **Tümevarım**, genel kavramların, denetlenen makine öğrenmesi problemlerinin çözmeyi amaçladığı problem olan spesifik örneklerden öğrenmeyi ifade eder. (Spesifik --> Genel)
* **Genelleme**, bir makine öğrenme modeli tarafından öğrenilen kavramların, öğrenme sırasında model tarafından görülmeyen belirli örneklere ne kadar iyi uygulandığını gösterir.
* **İyi bir makine öğrenme modelinin amacı, eğitim verilerinden problem alanından gelen tüm verilere iyi bir şekilde genellemektir.** Bu, modelin hiç görmediği veriler hakkında gelecekte tahminler yapmamızı sağlar.

* Bir makine öğrenim modelinin ne kadar iyi öğrendiğini ve genelleştirdiğini, yani fazladan takma ve destekleme konularını konuştuğumuzda, makine öğrenmesinde kullanılan bir terminoloji vardır.

    * **OverFitting** ve **UnderFitting**, makine öğrenmesi algoritmalarının düşük performansının en büyük iki nedenidir.

----

<p align="center">
  <b> İSTATİSTİKSEL UYUM </b><br>
</p>



* İstatistiklerde, bir uyum, bir hedef işlevi ne kadar iyi kullandığınıza karşılık gelir.

* Bu, makine öğrenmede kullanmak için iyi bir terminolojidir çünkü denetimli makine öğrenme algoritmaları, giriş değişkenleri verilen çıkış değişkenleri için bilinmeyen temel haritalama fonksiyonunu yaklaşık olarak hesaplamayı hedeflemektedir.

* İstatistikler genellikle işlevin yakınlığının hedef işlevle ne kadar iyi eşleştiğini tahmin etmek için kullanılan önlemleri ifade eden uyum iyiliğini tanımlar.

--------

<p align="center">
  <b> MAKİNE ÖĞRENMESİNDE OVERFITTING </b><br>
</p>

* OverFitting , eğitim verilerini çok iyi modelleyen bir modeli ifade eder.

* **Overfitting**, bir modelin eğitim verilerindeki detay ve gürültüyü öğrendiğinde, modelin yeni veriler üzerindeki performansını olumsuz yönde etkilediği ölçüde gerçekleşir. Bu, eğitim verilerindeki gürültü veya rastgele dalgalanmaların model tarafından kavramlar olarak toplandığı ve öğrenildiği anlamına gelir. Sorun, bu kavramların yeni veriler için geçerli olmaması ve modelleri genelleme yeteneğini olumsuz yönde etkilemesidir.

* Overfitting, bir hedef işlevi öğrenirken **daha fazla esnekliğe sahip olan parametrik olmayan** ve ***doğrusal olmayan modellerde daha olasıdır.** Dolayısıyla, parametrik olmayan makine öğrenmesi algoritmalarının birçoğunda, modelin ne kadar ayrıntı öğrendiğini sınırlamak ve sınırlamak için parametreler veya teknikler de bulunur.

    * Örneğin, karar ağaçları çok esnek olan ve aşırı eğitime dayanan verilere tabi olan parametrik olmayan bir makine öğrenme algoritmasıdır. Bu problem, topladığı bazı detayların kaldırılması için bir ağaç öğrendikten sonra budama ile çözülebilir.
    
-----

<p align="center">
  <b> MAKİNE ÖĞRENMESİNDE UNDERFITTING </b><br>
</p>

* **Underfitting**, eğitim verilerini modelleyemeyen ya da yeni verilere genelleştirilebilen bir model anlamına gelir.

Bir underfit makine öğrenme modeli uygun bir model değildir ve eğitim verilerinde düşük performansa sahip olacağı açıktır. Underfitting, **genellikle iyi bir performans ölçütü verildiğini tespit etmek kolay olduğu için tartışılmaz.** Çözüm, devam etmek ve alternatif makine öğrenme algoritmaları denemektir. Bununla birlikte, **overfitting sorununa iyi bir kontrast sağlar**.


* **Makine öğrenmesinde önyargı ve varyans arasındaki ilişkiden kaçış yoktur.**

    * Önyargıyı artırmak, varyansı azaltacaktır.
    * Varyansı artırmak yanlılığı azaltacaktır.

* Bu iki kaygı ile seçtiğiniz algoritmalar ve bunları yapılandırmayı seçtiğiniz yöntem arasında bir takas var, bu takasta sorununuzu çözmek için farklı dengeler buluyorsunuz.

* Gerçekte, gerçek sapma ve varyans hata terimlerini hesaplayamayız çünkü asıl hedef hedef fonksiyonunu bilmiyoruz. Bununla birlikte, bir çerçeve olarak, önyargı ve varyans, makine öğrenmesi algoritmalarının öngörücü performans arayışındaki davranışını anlama araçlarını sağlar.

------

<p align="center">
  <b> MAKİNE ÖĞRENMESİNDE İYİ UYUM (GOOD FITTING)  </b><br>
</p>

* İdeal olarak, overfitting ile underfitting arasında tatlı noktada bir model seçmek istersiniz. Amaç budur ancak pratikte oldukça zordur.Bu amacı anlamak için, bir eğitim verilerini öğrenirken zaman içinde bir makine öğrenme algoritmasının performansına bakabiliriz.
* Zaman içinde, eğitim verilerindeki modelin hatası azalır ve test veri setindeki hata da düşer.** Çok uzun süre denemeler yaparsak**, eğitim veri setindeki **performans düşmeye devam edebilir**, çünkü model eğitim veri setindeki alakasız ayrıntı ve gürültüyü abartıyor ve öğreniyor. Aynı zamanda, **test setinin hatası, modelin genelleme yeteneği azaldıkça tekrar artmaya başlar**.Tatlı nokta, **test veri setindeki hatanın artmaya başlamasından hemen önceki nokta,** *modelin hem eğitim veri seti hem de görünmeyen test veri seti üzerinde iyi bir beceri olduğu yerlerde artmaya başlıyor.*
* Uygulamada tatlı noktayı bulmak için kullanabileceğiniz iki ek teknik vardır: **yeniden örnekleme yöntemleri** ve **bir doğrulama veri seti.** (Resampling Methods & Validation Dataset)

------

<p align="center">
  <b> OVERFITTING'I SINIRLANDIRMA  </b><br>
</p>

* Hem **overfitting** hem de **underfitting** model, **düşük model performansına** yol açabilir. Ancak, uygulamalı makine öğrenimindeki **en yaygın sorun overfitting'dir.**

* Overfitting'i sınırlamak için makine öğrenme algoritmalarını değerlendirirken kullanabileceğiniz iki önemli teknik vardır:

    * Model doğruluğunu tahmin etmek için bir yeniden örnekleme tekniği kullanın. (Resampling Methods)
        * En popüler yeniden örnekleme tekniği, k-katlama çapraz doğrulamadır. Modelinizi farklı zaman dilimlerinde k-kez eğitmenize ve test etmenize ve bir makine öğrenim modelinin görünmeyen veriler üzerindeki performansını tahmin etmenize olanak sağlar.
    * Doğrulama veri kümesini geri tutun. (Validation Dataset)
        * **Doğrulama veri kümesi,** yalnızca makine öğrenme algoritmalarınızdan projenizin sonuna kadar sakladığınız eğitim verilerinizin bir alt kümesidir. Eğitim veri kümenizde makine öğrenme algoritmalarınızı seçtikten ve ayarladıktan sonra, **modellerin görünmeyen veriler üzerinde nasıl performans gösterebileceği konusunda nihai bir fikir edinmek için** doğrulama veri kümesinde öğrenilen modelleri değerlendirebilirsiniz.

----

* ***Çapraz doğrulama kullanmak, görünmeyen verilerde model doğruluğunu tahmin etmek için uygulamalı makine öğrenmesinde altın bir standarttır. Verilere sahipseniz, bir doğrulama veri kümesi kullanmak da mükemmel bir uygulamadır.***

----

<p align="center">
  <b> ÖZET  </b><br>
</p>

* **Overfitting** : Eğitim verilerinde iyi performans verirken, diğer verilere kötü genelleme yapar.
* **Underfitting** : Eğitim verilerinde düşük performans ve diğer verilere zayıf genelleme yapar.

----


















