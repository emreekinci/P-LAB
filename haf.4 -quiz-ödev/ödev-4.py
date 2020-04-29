
# fonksiyonların açıklamaları ve fonksiyonlar
def insertItemToHeap(myheap_1, item):  #Eklenmek isteneni diziye(heap durumunda zaten) heap olacak şekilde ekler.(uygun haliyle)
    myheap_1.append(item)              #.append ile eleman ekledikten sonra tekrar heap haline getirilir.
    index_value = len(myheap_1) - 1
    if index_value <= 0:
        return
    parent_value = (index_value - 1) // 2
    while parent_value >= 0 and myheap_1[parent_value] > myheap_1[index_value]:
        myheap_1[parent_value], myheap_1[index_value] = myheap_1[index_value], myheap_1[parent_value]
        index_value = parent_value
        parent_value = (index_value - 1) // 2


def removeItemFrom(myheap_1):  # En son elemanımızı heapten silen fonksiyondur.
    index = len(myheap_1)
    if index <= 0:                   # Eğer hiç eleman yoksa buna da dikkat edilmeli.(uyarı mesajı verilmeli)
        print("Heapte hiç eleman yok...")
        return
    myheap_1.pop()

def heap_sirala(dizi):    # sıralama algoritması
    dizi = dizi.copy()    # Array değiştirilmeden .copy ile array değişkenine yazılır.
    heap_olustur(dizi)
    sorted_array = []     # Sıralı olarak yazdırılacak dizi için yer ayırılır.(sorted_array[]-->boş dizi )
    for _ in range(len(dizi)):
        dizi[0], dizi[-1] = dizi[-1], dizi[0]
        sorted_array.append(dizi.pop())
        min_heapify_function(dizi, 0)
    return sorted_array


def min_heapify_function(array, i):  #Diz heap haline getirilir ve 2 değeri karşılaştır sınırı geçme ve en küçük = min yap).
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify_function(array, smallest)


# QUIZ KISMI..

def heap_olustur(array):  # n dizi uzunluğu olmak üzere(n/2) den 0'a kadar düğümleri min_heapfy'a aktarma yapılır.
    for p in reversed(range(len(array) // 2)):
        min_heapify_function(array, p)



dizim_1 = [6,11, 13, 24, 79, 36, 16, 9, 26]     # Dizimiz.
heap_olustur(dizim_1)                        # Dizinin Heap buildı.
print(dizim_1)

insertItemToHeap(dizim_1, 12)             # Heap'e eleman eklemek.
insertItemToHeap(dizim_1, 67)
insertItemToHeap(dizim_1, 3)
insertItemToHeap(dizim_1, 18)
insertItemToHeap(dizim_1, 4)
insertItemToHeap(dizim_1, 59)
insertItemToHeap(dizim_1, -85)
insertItemToHeap(dizim_1, 56)
insertItemToHeap(dizim_1, 44)


removeItemFrom(dizim_1)# Eklenen elemanlarımız en sondan tek tek silinir bu işlemle.
                      # last in first out vardır..
removeItemFrom(dizim_1)

removeItemFrom(dizim_1)

removeItemFrom(dizim_1)

removeItemFrom(dizim_1)

removeItemFrom(dizim_1)

removeItemFrom(dizim_1)

removeItemFrom(dizim_1)

print(dizim_1)# diziye dahil edilen ve atılanlarla birlikte son hali.
print(sorted(dizim_1))# dizinin son halinin sıralanmış yeni durumu..