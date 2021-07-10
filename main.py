# bu sorunun çözümünde kaç tane nested list yapısı olabileceğini önceden bilemediğimiz için
# recursive fonksiyon yapısını kullandım


def flat(l1, l2):  # fonksiyonumuza parametre olarak iki tane obje gireriz veririr
    # l1 objesi flat edilecek olan listedir  l2 ise flat edilmiş olan liste olacak
    for i in range(len(l1)):#bu satırda l1'in tüm elemanları içinde iterasyon yapılır

        if type(l1[i]) == list: # bu kod satırında ise l1 listesinin elemanlarının tipinin liste olup olmadığına
                                # bakıyoruz
            flat(l1[i], l2)     # l1'in list tipindeki elemanları için fonksiyon tekrar çağırılır.
        else:
            l2.append(l1[i])    #list tipinde olmayan elemanlar l2 listesine atılır.

    return l2                   #bu satırda oluşturulan l2 listesi döndürülür


#örnek
bosliste = []

liste = [[9, [1, 2, 3]], [1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5, 6, [[[7, 6, 5], [4, 3], [2, 1]]]]

print(flat(liste, bosliste))
