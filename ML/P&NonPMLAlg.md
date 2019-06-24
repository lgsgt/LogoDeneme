### PARAMETRİK VE PARAMETRİK OLMAYAN ALGORİTMALAR (P&NON-P ML ALG)
----

<p align="center">
  <b> PARAMETRİK ALGORİTMALAR</b><br>
</p>


* Varsayımlar öğrenme sürecini büyük ölçüde basitleştirebilir, ancak öğrenilebilecekleri sınırlayabilir. Fonksiyonu bilinen bir forma basitleştiren algoritmalara parametrik makine öğrenme algoritmaları denir.
* *Verileri sabit büyüklükteki parametrelerle (eğitim örnekleri sayısından bağımsız olarak) özetleyen bir öğrenme modeli parametrik model olarak adlandırılır. **Parametrik bir modelde ne kadar veri attığınız önemli değil**, ne kadar parametre gerektiğine ilişkin fikrini değiştirmez.*

* Algoritmalar iki adımı içerir:
    
    * 1. İşlev için bir form seçin.
    * 2. Fonksiyonun katsayılarını eğitim verilerinden öğrenin.

##### Parametrik Makine Öğrenme Algoritmalarının Yararları:
---
* **Daha Basit** : Bu yöntemlerin sonuçlarını anlamak ve yorumlamak daha kolaydır.
* **Hız** : Parametrik modeller verilerden öğrenmek için çok hızlı.
* **Daha Az Veri** : Çok fazla eğitim verisi gerektirmezler ve verilere uygun mükemmel olmasa bile iyi çalışabilirler.

##### Parametrik Makine Öğrenme Algoritmalarının Sınırlamaları:
---
* **Sınırlı** : İşlevsel bir form seçerek, bu yöntemler belirtilen forma oldukça sınırlıdır.
* **Sınırlı Karmaşıklık** : Yöntemler daha basit problemlere daha uygundur.
* **Kötü Fitleme** : Uygulamada yöntemlerin, temel haritalama işleviyle eşleşmesi olası değildir.

--------
<p align="center">
  <b> PARAMETRİK OLMAYAN ALGORİTMALAR</b><br>
</p>

* **Haritalama(Mapping) fonksiyonunun şekli hakkında güçlü varsayımlarda bulunmayan** algoritmalara parametrik olmayan makine öğrenme algoritmaları denir. Varsayımlarda bulunmayarak, **eğitim verilerinden herhangi bir fonksiyonel formu öğrenmekte özgürdürler**.
* *Parametrik olmayan yöntemler, **çok fazla veriye sahip olduğunuz ve önceden bilgi sahibi olmadığınız** zaman ve **yalnızca doğru özellikleri seçme konusunda çok fazla endişe etmek istemediğinizde iyidir**.*

##### Parametrik Olmayan Makine Öğrenimi Algoritmalarının Yararları:
---
* **Esneklik** : Çok sayıda işlevsel forma sığma kabiliyeti.
* **Güç** : Temel fonksiyon hakkında varsayımlar (veya zayıf varsayımlar) yok.
* **Performans** : Tahmin için daha yüksek performans modellerine neden olabilir.
---
##### Parametrik Olmayan Makine Öğrenmesi Algoritmalarının Sınırlamaları:

* **Daha fazla veri** : Haritalama fonksiyonunu tahmin etmek için daha fazla egzersiz verisi isteyin.
* **Yavaş** : Eğitmek için çok daha fazla parametreye sahip oldukları için eğitmek için çok daha yavaştır.
* **Overfitting** : Eğitim verisine overfit olması daha risklidir ve yapılan spesifik tahminin nedenini açıklama daha zordur.

---

#### OZET

* **Parametrik yöntemlerin**, girdi değişkenlerinin çıktı değişkenine eşlenmesiyle ilgili büyük varsayımlarda bulunduğunu ve sırayla daha hızlı eğitildiğini, daha az veri gerektirdiğini ancak bu kadar güçlü olamayacağını öğrendiniz.

* **Parametrik olmayan yöntemlerin** hedef işlev hakkında az veya hiç varsayımda bulunmadığını ve sırayla çok daha fazla veri gerektirdiğini, daha yavaş eğitildiğini ve daha yüksek bir model karmaşıklığına sahip olduğunu ancak daha güçlü modellerle sonuçlanabileceğini öğrendiniz.
