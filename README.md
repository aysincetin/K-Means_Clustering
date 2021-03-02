                                        K-MEANS (K-ORTALAMALAR) YÖNTEMİ İLE KÜMELEME
                                        
1. GİRİŞ (INTRODUCTİON)
Problemin tanımı

K-Means (K-Ortalamalar) algoritması çok fazla verinin belirli özelliklerine göre sınıflandırılmasını daha doğrusu kümelenmesini sağlayan bir algoritmadır. Bir gözetimsiz öğrenme yöntemidir ve burada amaç verilerin k adet kümeye ayrılması ve her bir kümenin de küme içi benzerliklerinin maksimum olmasıdır. Kümeler arasında ise bu durum tam tersidir.
Bu çalışmada K Means (K-Ortalamalar) yöntemi kullanılarak “calisan.csv” data setindeki veriler euclidean metriği kullanılarak hesaplanmıştır. Kullanıcıdan istenen cluster ve eksen bilgisi değerinde clustering işlemi yapılması hedeflenmiştir.


2.KULLANILAN YÖNTEM (METHOD)
2.1 Veri Seti (Data Set)

Çalışma için kullanılan veri seti rastgele oluşturulmuş olup gerçek değerler ile alakası bulunmamaktadır. Çalışanlara ait demografik bilgileri içeren veri seti Kilo(kg), Yas, Maas(tl), SehirPlakaKodu, KullanilanIzin(gun) olmak üzere 6 adet feature (özellik) ve 300 örnek (data) ile oluşturulmuştur.

![image](https://user-images.githubusercontent.com/29736070/109711004-6cd00f00-7baf-11eb-95bf-45b9760d252d.png)

2.1 Kümeleme Yöntemi (Clustering Method)

Veri madenciliği yöntemlerinde belli başlı problem tipleri vardır. K-Means yöntemi de kümeleme problemlerine yardımcı olan, verilen bir veri seti üzerinden belirli sayıda kümeyi (k adet) gruplamak için geliştirilmiş en sade ve basit algoritmadır. K-Means algoritması üç adımda özetlenebilir. İlk olarak veriler alınıp küme sayısı(k adet) belirlenir ve ağırlık merkezleri yani centroidler belirlenir. Sonrasında her nokta en uygun gruba atanır ve atamadan sonra centroid tekrar hesaplanır. Buna göre değer değişiyorsa güncelleme yapılıp bir önceki adıma gidilir, değer sabit kalıyorsa işlem tamamlanmış olur. K-Means yönteminde üç adet metrik vardır. Bunlar Euclidean, Manhattan ve Minkowski uzaklıklarıdır. Bu çalışmada Euclidean uzaklığı kullanılarak verilerin centroidlere olan uzaklığı hesaplanmıştır. Aşağıda Euclidean uzaklığı formülü verilmiştir.

![image](https://user-images.githubusercontent.com/29736070/109711116-8e30fb00-7baf-11eb-9641-f8d1977a8eb2.png)

3. ALGORİTMA TASARIMI (ALGORITHM DESIGN)
3.1 Problemin çözümünde kullanılan algoritma

K means yöntemi ile kümeleme yapmak için öncelikle istenen sayıda centroid rastgele noktalar içinden seçilmiştir. Sonrasında seçilen noktalar kendileriyle ve diğer centroidlerle karşılaştırılmayacak şekilde kalan diğer noktalarla Euclidean mesafeleri hesaplanarak minimum uzaklıkta olan her nokta için o centroid, bulunan noktaya göre güncellenmiştir. Bunun için for döngüleri ve 2 boyutlu arraylerden yararlanılmıştır.
Tüm centroidler tüm noktalarla karşılaştırılıp yeni centroid noktaları oluşturulduktan sonra bu noktalar tekrar hesaplanmak üzere yeni bir fonksiyona gönderilmiştir. Bu fonksiyon gelen centroid noktalarını elimizdeki tüm noktalarla Euclidean mesafeleri hesaplanarak ikinci iterasyon oluşturulur. Daha sonra birinci ve ikinci iterasyon karşılaştırılarak eşit olup olmadıkları kontrol edilir. Eşitlik yoksa ikinci iterasyon sonucu bulunan centroidler tekrar hesaplanmak için fonksiyona gönderilir ve üçüncü iterasyon centroidler oluşturulur. Daha sonra üçüncü iterasyon ve ikinci iterasyon centroidler karşılaştırılır. Eşitlik sağlanana kadar döngü bu şekilde devam eder. Eşitlik sağlandığı durumda döngü bitirilerek optimum centroid noktaları bulunmuş olur. Bulunan optimum centroid noktaları clusterları oluşturulmak üzere bir fonksiyona gönderilir. Bu fonksiyonda gelen centroid noktaları veri setindeki noktalarla Euclidean mesafeleri hesaplanarak noktalar yakın oldukları centroidlere göre 2 boyutlu array kullanılarak clusterlara bölünmüş olur. Daha sonra bu clusterlar ekrana bastırılıp görsel olarak ifade edilir.

4. DENEYSEL SONUÇLAR (EXPERİMENTAL RESULTS)

Bu çalışmada elde edilen sonuçlar aşağıdaki gibidir.

![image](https://user-images.githubusercontent.com/29736070/109711281-bfa9c680-7baf-11eb-93e4-e9c6afc780c9.png)

Cluster adedini 3, X eksenini=4, Y eksenini=2 ve Z eksenini=5 seçtiğimizde oluşan centroid noktaları aşağıdaki gibidir.

![image](https://user-images.githubusercontent.com/29736070/109711339-cf290f80-7baf-11eb-877f-da5bd0be4593.png)

![image](https://user-images.githubusercontent.com/29736070/109711408-e7009380-7baf-11eb-8cf4-1f79e02fe16b.png)

![image](https://user-images.githubusercontent.com/29736070/109711484-fa136380-7baf-11eb-9c34-3c4ef097eef6.png)

Oluşan kümeler görselleştirildiğinde aşağıdaki sonuçlar elde edilmiştir.
2 Boyutta sonuçlar:

![image](https://user-images.githubusercontent.com/29736070/109711588-13b4ab00-7bb0-11eb-830f-9c3ed305eee9.png)

3 Boyutta sonuçlar:

![image](https://user-images.githubusercontent.com/29736070/109711641-20d19a00-7bb0-11eb-965e-f27412747854.png)

(Not: Her hesaplama da centroid noktalarında değişim olabilir bunun sebebi 1 den fazla optimum nokta bulunmasıdır. Görsellerdeki kaymalar ise tamamen eksen boyutlarıyla alakalı olup hesaplamalarda herhangi bir yanlışlık olmamaktadır.)
