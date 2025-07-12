# %% pandas ve numpy kütüphanesini içe aktar
import pandas
import numpy
# txt dosyasını bir veri çerçevesine oku
data = pandas.read_csv("C:/Users/ramaz/Masaüstü/Dosyalar/Ders/Yazılım Mühendisliği/3. Sınıf/Yaz Dönemi/Bilişim Matematiği/pageRankCode/California.txt", delimiter=' ')

# %% verileri önceden işle
# yalnızca 'e' türündeki satırları seç
adjacencies = data.loc[data['Type'] == 'e']
# 'Type' sütununu bırak
adjacencies = adjacencies.drop(columns = 'Type')
# bitişiklik listesini bir NumPy dizisine dönüştür
adjacencies = adjacencies.to_numpy()

# %% bitişiklik listesini int türüne dönüştür
adjacencies = adjacencies.astype('int')
# bitişiklik listesini yazdır
print(adjacencies)

# %% PageRank fonksiyonu
def PageRank(A, d=0.85, eps=0.0005, maxIterations=10, verbose = False):
    # find the size of the "Internet"
    N = A.shape[0]
    
    # initialize the old and new PageRank vectors
    vOld = numpy.ones([N])
    vNew = numpy.ones([N])/N
    
    # initialize a counter
    i = 0
    # compute the update matrix
    U = d * A.T + (1 - d) / N
    while numpy.linalg.norm(vOld - vNew) >= eps:
        # if the verbose flag is true, print the progress at 
        # each iteration
        if verbose:
            print('At iteration', i, 'the error is',
              numpy.round(numpy.linalg.norm(vOld - vNew), 
                3), 'with PageRank', numpy.round(vNew, 3))
            
        # save the current PageRank as the old PageRank
        vOld = vNew
        
        # update the PageRank vector
        vNew = numpy.dot(U, vOld)
        
        # increment the counter
        i += 1
        
        # if it runs too long before converging, stop and notify the 
        # user
        if i == maxIterations:
            print('The PageRank algorithm ran for',
                   maxIterations, 'with error',
                    numpy.round(numpy.linalg.norm(vOld - vNew), 
                     3))
            
            # return the PageRank vector and the 
            return vNew, i
        # return the steady state PageRank vector and iteration 
        # number
        return vNew, i
# %% komşuluk listesini bir komşuluk matrisine dönüştür
# web sayfası sayısını bul ve A'yı başlat
N = numpy.max(adjacencies) + 1
A = numpy.zeros([N, N])
# komşuluk listesinin satırları üzerinde yineleme yap
for k in range(adjacencies.shape[0]):
    # bitişik tepe numaralarını bul
    i, j = adjacencies[k,]
    
    # komşuluk matrisine 1 koy
    A[i, j] = 1
    
    # A'yı geçiş olasılık matrisine dönüştür
    # A'nın her satırını satır toplamına böl
    rowSums = A.sum(axis = 1)[:,None]
    # A'yı rowSums'a böl
    C = numpy.divide(A, rowSums, where = rowSums != 0)
    # PageRank'i çalıştır.
    v, i = PageRank(A)
    # sabit durum PageRank vektörünü ve yineleme numarasını yazdır
    print(v)
    print(i)

# %% PageRank'leri artan düzende sırala
ranks = numpy.argsort(v)
# PageRank'leri azalan sırada bul
ranks = numpy.flip(ranks)

# %% ilk birkaç web sayfasının URL'lerini döndür
rankedPages = pandas.DataFrame(columns = ['Type', 'Source',
 'Destination'])
# ilk 10 sıradaki web sayfalarını ekle
for i in range(10):
    row = data.loc[(data['Type'] == 'n')
    & (data['Source'] == ranks[i])]
    rankedPages = rankedPages.append(row)

# ilk 10'u göster
rankedPages.drop(columns = ['Type', 'Source'])