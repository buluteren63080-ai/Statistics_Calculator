
# ekstra bir kütüphane kullanmadan yazılan istatistik dersi için gerekli matematiksel işlemlerin fonksiyonları
# main.py da çağırılıcak fonksiyonlar
# başka bir projede de bu dosya projeye dahil edilip kullanılabilir bu fonksiyonlar


# len fonksiyonu ile listede kaç veri olduğu bulunur
# return bu fonksiyon bitince fırlatılan değer için
def number_of_data(data):
    number = len(data)
    return number

# sum listedeki değerleri toplamak için kullanılan bir fonksiyon
def total_sum(data):
    total_sum = sum(data)
    return total_sum

# aritmetik ortalama için toplam veri sayısına bölünür
def aritmetic_mean(data):
    t_sum = sum(data)
    l = len(data)
    a_mean = t_sum / l
    return a_mean

# medyan tek ve çift olması etkilediği için if  ile ( % ) parametresi ile teklik çiftlik kontrol edilir
# tek ise ( // ) ile float olmadan tam sayıya yuvarlayan bölme işlemi yapılıp medyana karşılık gelicek index elde edilir
# çift ise ortadaki iki sayının index i bulunur, ( / ) ile yapılan bölme float olarak dönüyor o yüzden int() ile integer a çevir
def median(data):
    n = len(data)
    sorted_data = sorted(data)

    if n % 2 != 0:
        i = n // 2
        odd_median = sorted_data[i]
        return odd_median

    if n % 2 == 0:
        index_1 = int(n/2) - 1
        index_2 = int(n/2)
        even_median = (sorted_data[index_1] + sorted_data[index_2]) / 2
        return even_median

# range en büyük ile en küçüğün farkı, python içinde gelen min ve max fonksiyonları ile bulunabiliyor
def data_range(data):
    data_range = max(data) - min(data)
    return data_range

# örnek varyansı n - 1 e bölündüğü için 2 den küçükse hata verir başta if ile onu kontrol edilip none döndürülür
# for döngüsü alt alta değil tek satır içinde ( for number_in_data in data ) diye de yazılabilir
# sum ile for döngüsüyle data listesi içindeki değerlerin hepsinin ortalama ile farkı toplanır
# ( n - 1 ) ile bölünüp return ile fonksiyon dışına gönderilir
def sample_variance(data):
    n = len(data)
    if n < 2:
        return None

    mean = aritmetic_mean(data)
    return sum((number_in_data - mean) ** 2 for number_in_data in data) / (n - 1)

# evren varyansı aslen örneklem varyansının aynısı sadece n - 1 ile değil n ile bölünnen hali
def population_variance(data):
    n = len(data)

    mean = aritmetic_mean(data)
    return sum((number_in_data - mean) ** 2 for number_in_data in data) / n

# örneklem ve evren standart sapması örneklem ve evren varyansının karekökü
# karekök math kütüphanesi ile alınabiliyormuş ama kütüphane olmadan da oluyor
# bir sayının 0.5 inci üssü karekökü demek o yüzden ** (1/2) yazmak lazım
def sample_standard_deviation(data):
    return sample_variance(data) ** (1/2)
def population_standard_deviation(data):
    return population_variance(data) ** (1/2)

# z skoru her bir veriye özel olduğu için lsitedeki her verinin ayrı ayrı hesaplanıp append ile ayrı bi listeye ekleniyor
# ortalama ve standart sapma için önceden yazdığım fonksiyonları kullandım
def z_scores_list(data):

    z_scores_list =[]

    for x in data:
        z_score = (x - aritmetic_mean(data)) / sample_standard_deviation(data)
        z_scores_list.append(z_score)

    return z_scores_list

# Q1 medyanın sol tarafının medyanı demek olduğu için önce ayrı bir liste olarak almak lazım
# eleman sayısı çift ise ikiye bölüp sorted_data[:x] diyerek o index e kadar olan kısma slicing yaptım x dahil değil
# tek ise de aynı mantık çünkü orda ortadaki değeri katmadan sağı ve soluna bakılacağından slicing yaptım
# // gene tam sayıya çevirmesi için bölümü, 3.5 değil 3 mesela ( // ) bu işe yarıyor
def Q1(data):
    n = len(data)
    sorted_data = sorted(data)

    if n % 2 == 0:
        x = int(n/2)
        e_first_half = sorted_data[:x]
        return median(e_first_half)

    if n % 2 != 0 :
        y = n // 2
        o_first_half = sorted_data[:y]
        return median(o_first_half)

# Q3 de Q1 deki işlemlerin aynısı ama sağ taraf için o yüzden sorted_data[x:] diyerek ayrılacağı indexden itibaren diye değiştirdim
def Q3(data):
    n = len(data)
    sorted_data = sorted(data)

    if n % 2 == 0:
        x = int(n/2)
        e_second_half = sorted_data[x:]
        return median(e_second_half)

    if n % 2 != 0 :
        y = n // 2
        o_second_half = sorted_data[y + 1:]
        return median(o_second_half)

# çeyrekler açıklığı Q3 ve Q1 in farkı
def IQR(data):
    return Q3(data) - Q1(data)
