# PageRank Algoritması Uygulaması

Bu depo, Google'ın web sayfalarının önemini belirlemek için kullandığı PageRank algoritmasının temel prensiplerini ve hesaplama yöntemlerini açıklamaktadır. Bu README, algoritmanın nasıl çalıştığını, formülünü ve pratik bir örnek üzerinden uygulamasını detaylandırarak, temel bir anlayış sağlamayı amaçlar.

## İçindekiler

1.  [Temel Amaç](#temel-amaç)
2.  [PageRank Nedir?](#pagerank-nedir)
3.  [PageRank Formülü](#pagerank-formülü)
4.  [Hesaplama Adımları ve Örnek](#hesaplama-adımları-ve-örnek)
    * [Bağlantı Sayılarının Hesaplanması (C(Wi))](#bağlantı-sayılarının-hesaplanması-cwi)
    * [PageRank Değerlerinin Hesaplanması](#pagerank-değerlerinin-hesaplanması)
    * [Dangling Node (Asılı Düğüm) Çözümü](#dangling-node-asılı-düğüm-çözümü)
    * [Matris Tabanlı Hesaplama](#matris-tabanlı-hesaplama)

---

## Temel Amaç

PageRank algoritmasının temel amacı, bir web sayfasının internetteki önemini ve otoritesini belirlemektir.

## PageRank Nedir?

* PageRank, sayfalara gelen bağlantıları, o sayfanın önemi için verilmiş "oylar" gibi düşünür.
* Bir sayfa, ne kadar çok ve **kaliteli** sayfadan bağlantı alırsa, PageRank değeri o kadar yüksek olur.
* Sadece bağlantı sayısı değil, bağlantıyı veren sayfanın **kendi PageRank'i** de önemlidir.
* Bir sayfadan çıkan çok sayıda bağlantı varsa, her bir bağlantıya aktarılan PageRank değeri azalır.

## PageRank Formülü

PageRank (PR) aşağıdaki formülle hesaplanır:

`PR(A) = (1 - d) + d * Σ(PR(Ti) / C(Ti))`

**Formüldeki Terimler:**

* **`PR(A)`**: Sayfa A'nın PageRank değeri.
* **`d`**: Damping faktörü (genellikle 0.85 olarak alınır). Rastgele bir sonraki sayfaya atlama olasılığını temsil eder.
* **`T₁, ..., Tn`**: A sayfasına bağlantı veren sayfalar (yani, A'ya oy veren sayfalar).
* **`C(Ti)`**: Sayfa Ti'nin verdiği toplam dış bağlantı sayısı.

Bu formülü uygulayabilmek için ilk olarak `C(Ti)` değerlerini (yani her sayfanın dışarı verdiği bağlantı sayısını) hesaplamak gerekmektedir.

## Hesaplama Adımları ve Örnek

PageRank değerlerini hesaplamak için iteratif bir yaklaşım kullanılır.

### Bağlantı Sayılarının Hesaplanması (C(Wi))

Verilen bir ağ grafiğinde, her bir sayfanın dışarı verdiği bağlantı sayısı (`C(Wi)`) belirlenir.

**Örnek:**

* **W1**: W2, W3, W4 ve W5 sayfalarına bağlantı verir, bu nedenle `C(W1) = 4`.
* **W2**: W1 ve W4 sayfalarına bağlantı verir, bu nedenle `C(W2) = 2`.
* **W3**: W1, W4 ve W5 sayfalarına bağlantı verir, bu nedenle `C(W3) = 3`.
* **W4**: W1 sayfasına bağlantı verir, bu nedenle `C(W4) = 1`.
* **W5**: W4 sayfasına bağlantı verir, bu nedenle `C(W5) = 1`.

### PageRank Değerlerinin Hesaplanması

Başlangıç PageRank değerleri genellikle tüm sayfalara eşit olarak atanır (örneğin, N adet sayfa varsa her biri 1/N). Ardından, yukarıdaki formül kullanılarak her sayfanın PageRank değeri iteratif olarak (tekrarlı bir şekilde) hesaplanır. Daha doğru PageRank değerleri için bu hesaplama belirli sayıda tekrarlanabilir (algoritma yakınsayana kadar).

**Örnek İlk İterasyon Sonuçları:**

* `PR(W1) = 0.34`
* `PR(W2) = 0.07`
* `PR(W3) = 0.07`
* `PR(W4) = 0.38`
* `PR(W5) = 0.13`

### Dangling Node (Asılı Düğüm) Çözümü

PageRank algoritmasında, hiçbir dış bağlantısı olmayan web sayfalarına (asılı düğümler) özel çözümler uygulanır. Bu düğümlerin PageRank değerlerini kaybetmemesi ve ağdaki diğer sayfalara dağıtabilmesi için çeşitli stratejiler kullanılır. Genellikle, bu düğümlerden tüm diğer sayfalara eşit olasılıkla bağlantı varmış gibi kabul edilir veya PageRank'leri diğer sayfalara dağıtılır.

### Matris Tabanlı Hesaplama

PageRank hesaplaması, bir geçiş matrisi (A) ve başlangıç PageRank vektörü (`v0`) kullanılarak matris çarpımı ile de yapılabilir.

`U = d * A.T + (1 - d) / N`

Burada `N` düğüm sayısıdır, `A.T` ise `A` matrisinin transpozudur. Bu işlemden sonra PageRank hesaplamak için `U` matrisi ile `v` (PageRank vektörü) matrisi nokta çarpımı yapılır ve bu işlem itere edilerek daha doğru PageRank değerleri elde edilebilir. Örneğin, bu işlem 10 kez tekrarlanırsa daha doğru PageRank değeri elde edilecektir.

**Örnek 10. İterasyon Sonucu (`v10`):**

`v10 = [0.354; 0.105; 0.105; 0.293; 0.134]`
