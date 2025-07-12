# PageRank Algoritması Uygulaması

Bu depo, Google'ın web sayfalarının önemini belirlemek için kullandığı PageRank algoritmasının temel prensiplerini ve hesaplama yöntemlerini açıklamaktadır. Sunum, algoritmanın nasıl çalıştığını, formülünü ve pratik bir örnek üzerinden uygulamasını detaylandırmaktadır.

## Temel Amaç

PageRank algoritmasının temel amacı, bir web sayfasının internetteki önemini ve otoritesini belirlemektir.

## PageRank Nedir?

* PageRank, sayfalara gelen bağlantıları, o sayfanın önemi için verilmiş "oylar" gibi düşünür.
* Bir sayfa, ne kadar çok ve kaliteli sayfadan bağlantı alırsa, PageRank değeri o kadar yüksek olur.
* Sadece bağlantı sayısı değil, bağlantıyı veren sayfanın kendi PageRank'i de önemlidir.
* Bir sayfadan çıkan çok sayıda bağlantı varsa, her bir bağlantıya aktarılan PageRank değeri azalır.

## PageRank Formülü

PageRank (PR) aşağıdaki formülle hesaplanır:

PR(A) = (1 - d) + d * Σ(PR(Ti) / C(Ti))

**Formüldeki Terimler:**

* PR(A): Sayfa A'nın PageRank değeri.
* d: Damping faktörü (genellikle 0.85 olarak alınır).
* T1, ..., Tn: A sayfasına bağlantı veren sayfalar.
* C(Ti): Sayfa Ti'nin verdiği toplam bağlantı sayısı.

Bu formülü uygulayabilmek için ilk olarak C(Wi) değerlerini hesaplamak gerekmektedir.

## Hesaplama Adımları ve Örnek

PageRank değerlerini hesaplamak için iteratif bir yaklaşım kullanılır.

### Bağlantı Sayılarının Hesaplanması (C(Wi))

Verilen bir ağ grafiğinde, her bir sayfanın dışarı verdiği bağlantı sayısı (C(Wi)) belirlenir. Örneğin:

* W1, W2, W3, W4 ve W5 sayfalarına bağlantı verir, bu nedenle C(W1) = 4.
* W2, W1 ve W4 sayfalarına bağlantı verir, bu nedenle C(W2) = 2.
* W3, W1, W4 ve W5 sayfalarına bağlantı verir, bu nedenle C(W3) = 3.
* W4, W1 sayfasına bağlantı verir, bu nedenle C(W4) = 1.
* W5, W4 sayfasına bağlantı verir, bu nedenle C(W5) = 1.

### PageRank Değerlerinin Hesaplanması

Başlangıç PageRank değerleri genellikle tüm sayfalara eşit olarak atanır. Ardından, yukarıdaki formül kullanılarak her sayfanın PageRank değeri iteratif olarak hesaplanır. Daha doğru PageRank değerleri için bu hesaplama belirli sayıda tekrarlanabilir.

**Örnek İlk İterasyon Sonuçları:**
* PR(W1) = 0.34
* PR(W2) = 0.07
* PR(W3) = 0.07
* PR(W4) = 0.38
* PR(W5) = 0.13

### Dangling Node (Asılı Düğüm) Çözümü

PageRank algoritmasında, hiçbir dış bağlantısı olmayan web sayfalarına (asılı düğümler) özel çözümler uygulanır. Kaynak web sitesinin PageRank'inden bağlantı verilen sayfalara aktarılacak olan PageRank miktarını temsil eden ağırlıklar (Wi) kenarlara eklenir.

### Matris Tabanlı Hesaplama

PageRank hesaplaması, bir matris A ve başlangıç PageRank vektörü v0 kullanılarak da yapılabilir.

U = d * A.T + (1 - d) / N

Burada N düğüm sayısıdır, A.T matris A'nın transpozudur. Bu işlemden sonra PageRank hesaplamak için U matrisi ile v matrisi nokta çarpımı yapılır. Nokta çarpımı itere edilerek daha doğru PageRank değerleri elde edilebilir. Örneğin, bu işlem 10 kez tekrarlanırsa daha doğru PageRank değeri elde edilecektir.

**Örnek 10. İterasyon Sonucu (v10):**
v10 = [0.354; 0.105; 0.105; 0.293; 0.134]
