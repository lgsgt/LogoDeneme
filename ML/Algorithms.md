# The Most Popular Machine Learning Algorithms
---

* Two ways to think about and categorize the algorithms you may come across in the field.
    * The first is a grouping of algorithms by the **learning style**.
    * The second is a grouping of algorithms by **similarity** in form or function (like grouping similar animals together).

* Both approaches are useful, but we will focus in on the grouping of algorithms by similarity and go on a tour of a variety of different algorithm types.

##### Öğrenme Stiline Göre Gruplanan Algoritmalar
---

* Bir algoritmanın, deneyimle veya çevre ile olan etkileşimine veya giriş verilerini ne adlandırmak istediğimize dayanarak problemi modelleyebileceği farklı yollar vardır.

>1) **Supervised Learning (Denetimli Öğrenme)** (xxx)

- Girdi verilerine eğitim verisi (training data) denir ve bir kerede spam / spam olmayan veya hisse senedi fiyatı (stock price) gibi bilinen bir etiketi veya sonucu vardır.
- Bir model, öngörülerde bulunulması gereken ve bu tahminler yanlış olduğunda düzeltilen bir eğitim sürecinde hazırlanır. Eğitim süreci, model eğitim verilerinde istenen bir doğruluk seviyesine ulaşana kadar devam eder.
- Örnek problemler **sınıflandırma ve regresyondur**.
- Örnek algoritmalar, **Lojistik Regresyon (Logistic Regression)** ve **Geri Yayılım Sinir Ağı'nı (Back Propagation Neural Network)** içerir.

>2) **Unsupervised Learning (Denetimsiz Öğrenme)**

- Giriş verileri etiketli değildir ve bilinen bir sonucu yoktur. (not labeled)
- Girdi verilerinde mevcut yapılar çıkarılarak bir model hazırlanır. Bu genel kuralları çıkarmak olabilir. Artıklığı sistematik olarak azaltmak, matematiksel bir işlemle olabilir veya verileri benzerlikle düzenlemek olabilir.
- Örnek problemler **kümeleme (clustering)**, **boyutsallığın azaltılması (dimensionality reduction)** ve **ilişkilendirme kuralı öğrenmesidir (association rule learning)**.
- Example algorithms include: **the Apriori algorithm and k-Means.**

>3) **Semi-Supervised Learning** (xxx)

- Girdi verileri, etiketli ve etiketsiz örneklerin bir karışımıdır. (Labeled & Unlabeled)
- İstenen bir tahmin problemi var ancak model, verileri organize etmek ve tahminler yapmak için yapıları öğrenmeli.
- Example problems are **classification and regression**.
- Örnek algoritmalar, etiketlenmemiş verilerin nasıl modelleneceği konusunda varsayımlarda bulunan diğer esnek yöntemlerin uzantılarıdır. 

---
#### ÖZET(Öğrenme Stiline Göre)
---

- İş kararlarını modellemek için veri toplarken, en çok **denetimli(supervised)** ve **denetimsiz(unsupervised)** öğrenme yöntemlerini kullanıyoruz.
- Şu anda sıcak olan bir konu, çok az etiketli örneklerin bulunduğu büyük veri setlerinin bulunduğu görüntü sınıflandırma gibi alanlarda **yarı denetimli** öğrenme yöntemleridir.
---

##### Benzerliklere Göre Gruplanan Algoritmalar

* Algoritmalar genellikle işlevleri bakımından (nasıl çalıştıkları) benzerlik bakımından gruplandırılır.  Bu algoritmaları gruplandırmanın en kullanışlı yolu ve burada kullanacağımız **yaklaşım**.
* Bu vakaları, algoritmaları iki kez listeleyerek veya öznel olarak **“en uygun”** olan grubu seçerek halledebiliriz.
* Karşılaştığınız en yaygın iki denetimli makine öğrenme problemi olan sınıflandırma ve regresyon için kullanılan algoritmalara karşı güçlü bir **önyargı/sapma(bias) var**.
---
>1)  **Regresyon Algoritmaları**

* Regresyon, model tarafından yapılan tahminlerde bir hata ölçüsü kullanılarak yinelemeli olarak rafine edilmiş değişkenler arasındaki ilişkinin modellenmesi ile ilgilidir.

* En popüler Regresyon Algoritmaları:
    * Ordinary Least Squares Regression (OLSR) (En Küçük Kareler Yöntemi)
    * Linear Regression (Doğrusal)
    * Logistic Regression (Lojistik)
    * Stepwise Regression (Kademeli)
    * Multivariate Adaptive Regression Splines (MARS) 
    * Locally Estimated Scatterplot Smoothing (LOESS)

>2)  **Örnek tabanlı algoritmalar**

* Örnek tabanlı öğrenme modeli, model için önemli veya gerekli görülen eğitim verilerinin örnekleri veya örnekleri ile bir karar sorunudur.
* Bu yöntemler tipik olarak bir **örnek veri veritabanı oluşturur** ve en iyi eşleşmeyi bulmak ve **bir tahmin yapmak için benzerlik ölçüsü kullanarak** yeni verileri veri tabanıyla karşılaştırır. Bu nedenle, örnek tabanlı yöntemler; kazanan yöntemlerle yöntemi ve bellek temelli öğrenme denir. Saklanan örneklerin temsiline ve örnekler arasında kullanılan benzerlik önlemlerine odaklanılır.
* En popüler örnek tabanlı algoritmalar:
    - k-Nearest Neighbor (kNN)
    - Learning Vector Quantization (LVQ)
    - Self-Organizing Map (SOM)
    - Locally Weighted Learning (LWL)

>3)  **Düzenlileştirme(Regularization) Algoritmalar**

* Karmaşıklıklarına göre modelleri cezalandıran, genellikle genellemede daha iyi olan daha basit modelleri tercih eden başka bir yönteme yapılan bir uzantı veya hattır. (tipik olarak regresyon yöntemleri).
* En popüler düzenlileştirme algoritmaları:
    * Ridge Regression
    * Least Absolute Shrinkage and Selection Operator (LASSO)
    * Elastic Net
    * Least-Angle Regression (LARS)

>4)  **Karar Ağacı(Decision Tree) Algoritmaları** (xxx)

* Karar ağacı yöntemleri, verilerdeki özniteliklerin gerçek değerlerini temel alan bir karar modeli oluşturur.
* Ağaç yapılarında verilen kararlar, belirli bir kayıt için tahmin kararı verilene kadar geçerlidir. Karar ağaçları, **sınıflandırma ve regresyon sorunları için veriler üzerinde eğitilmiştir**. Karar ağaçları genellikle **hızlı ve kesindir** ve **makine öğrenmesinde büyük bir favoridir**.
* En popüler karar ağacı algoritmaları:
    * Classification and Regression Tree (CART)
    * Iterative Dichotomiser 3 (ID3)
    * C4.5 and C5.0 (different versions of a powerful approach)
    * Chi-squared Automatic Interaction Detection (CHAID)
    * Decision Stump
    * M5
    * Conditional Decision Trees

>5)  **Bayes Algoritmaları**

* Bayes metotları, sınıflandırma ve regresyon gibi problemler için açıkça Bayes Teoremini uygulayan metodlardır

>5)  **Kümeleme(Clustering) Algoritmaları**

* Kümeleme, regresyon gibi, problem sınıfını ve yöntem sınıfını tanımlar.
* Kümeleme yöntemleri tipik olarak Ağırlık Merkezi Tabanlı ve Hiyerarşik gibi modelleme yaklaşımlarıyla düzenlenir. Tüm yöntemler, verileri **en iyi ortaklığa sahip gruplar** halinde en iyi şekilde düzenlemek için verilerdeki doğal yapıların kullanılmasıyla ilgilidir.

>6)  **Derin Öğrenme Yöntemi (Deep Learning) Algoritmaları**

* Derin Öğrenme yöntemleri, bol miktarda ucuz hesaplamayı kullanan Yapay Sinir Ağları için modern bir güncellemedir.
* Çok daha büyük ve daha karmaşık sinir ağları oluşturmakla ilgileniyorlar ve yukarıda da belirtildiği gibi, çoğu veride, büyük veri kümelerinin çok az etiketli veri içerdiği yarı denetimli öğrenme problemleriyle ilgileniyor.

>7)  **Topluluk(Ensemble) Algoritmaları**

* Topluluk yöntemleri, bağımsız bir şekilde eğitilmiş ve öngörüleri bir şekilde genel tahminde bulunmak için bir araya getirilmiş olan daha zayıf modellerden oluşan modellerdir.

* Ne tür zayıf öğrenicilerin bir araya getirilmesi ve bunların nasıl birleştirileceği konusunda çok çaba harcanmaktadır. Bu, çok güçlü bir teknik sınıfıdır ve bu nedenle **çok popülerdir**.




