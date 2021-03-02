import random
import sys
import xlrd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

print("Maksimum 8 cluster giriniz...")
quantity = int(input("Cluster sayısı giriniz: "))
rows = []
columns = []
selected = []
temp_array = []
clusters = []
chosen_numbers = []
numbers = []
a = []

loc = ('calisan.xlsx')
wb = xlrd.open_workbook(loc)  # open_workbook fonk ile bir çalışma sayfası oluşturmak için
sheet = wb.sheet_by_index(0)  # sheet_by_index fonk ile 0. indexten itibaren sayfaları almak için

# satırları arraye kopyalayan döngü
for j in range(1, sheet.nrows):
    row = sheet.row_values(j, 0).copy()
    rows.append(row)

# sütunları arraye kopyalayan döngü
for m in range(sheet.ncols):  # sheet.ncols: tüm sütunları almak için
    column = sheet.col_values(m, 1).copy()
    columns.append(column)  # append ile sütunları ekleme


def centroid_selection(quantity):
    numbers.clear()
    chosen_numbers.clear()
    selected.clear()
    temp_array.clear()

    #row sayısı arraye koyulur daha sonra centroid noktası seçilmek için kullanılır
    for i in range(len(rows)):
        numbers.append(i)
    #numbers içinden istenen cluster sayısı kadar nokta seçilir ve uniq olması için o sayı arrayden silinir
    for j in range(quantity):
        r = random.choice(numbers)
        chosen_numbers.append(r)
        numbers.remove(r)

    #belirlenen centroid noktalarının arraye yerleştirilmesi
    for z in range(len(chosen_numbers)):
        selected.append(rows[chosen_numbers[z]])

    #centroid noktası dışında kalanların arraye yerleştirilmesi
    for c in range(len(numbers)):
        temp_array.append(rows[numbers[c]])

#optimum centroid noktaların bulmak için fonk.
def optimum_centroid_choise():
    centroid_selection(quantity)  #random centroid oluşturulur

    first_calculate = np.array((first_calculation(selected, temp_array)))
    sec_calculate = np.array((second_calculation(first_calculate)))

    comparison = first_calculate == sec_calculate  #ilk ve ikinci arrayi birbiriyle karşılaştırmak için
    equal_arrays = comparison.all()

    #son centroid bir önceki centroid eşit olana kadar devam eden kontrol döngüsü
    while equal_arrays == False:

        first_calculate = sec_calculate # son centroidler bir önceki noktaya atanır
        sec_calculate = np.array((second_calculation(first_calculate))) #son centroidler tekrar hesaplanmaya gönderilerek yeni centroidler oluşturulur

        comparison = first_calculate == sec_calculate
        equal_arrays = comparison.all()# oluşan centroid ilk centroid ile karşılaştırılır

    global centroids
    centroids = first_calculate.copy()

    clustering(first_calculate)

#seçilen centroidler dışında kalan noktalara göre hesaplama yapılır
def first_calculation(selected, temp_array):
    total = 0
    totals_array = []
    temp_array = temp_array.copy()
    selected = selected.copy()
    diveders = []

    for n in range(quantity):
        diveders.append(2)

    for j in range(len(temp_array)):
        for i in range(len(chosen_numbers)):
            for k in range(len(temp_array[i])):
                a = pow(selected[i][k] - float(temp_array[j][k]), 2)
                total += a
            totals_array.append(sqrt(total))
            total = 0
        index = totals_array.index(min(totals_array))

        for l in range(sheet.ncols):
            temp = format(((selected[index][l] * (diveders[index] - 1)) + temp_array[j][l]) / diveders[index], '.3f') # işlem
            selected[index][l] = float(temp)
        diveders[index] += 1
        totals_array = []

    return selected
#oluşan yeni centroidleri tüm noktalarla karşılaştırır
def second_calculation(selected_):
    selected = selected_.copy()
    total = 0
    totals_array = []
    diveders = []
    rows = []
    #öklid uzaklığında her centroid için hesaplanırken formülde ortalama için kullanılan değerler
    for n in range(quantity):
        diveders.append(2)

    for j in range(1, sheet.nrows):
        row = sheet.row_values(j, 0).copy()
        rows.append(row)
    #her centroidi tek tek noktalarla öklid uzaklığı hesabı yapan ve hesaba göre centroidi güncelleyen döngüler
    for j in range(len(rows)):
        for i in range(len(chosen_numbers)):
            for k in range(len(rows[i])):
                a = pow(selected[i][k] - rows[j][k], 2) #
                total += a                              # öklid hesabı
            totals_array.append(sqrt(total))            #
            total = 0
        index = totals_array.index(min(totals_array))
        #noktaya en yakın centroid güncelleyen döngü
        for l in range(sheet.ncols):
            temp = format(((selected[index][l] * (diveders[index] - 1)) + rows[j][l]) / diveders[index], '.3f')
            selected[index][l] = float(temp)

        diveders[index] += 1
        totals_array = []

    return selected
#kümeleme işlemi için oluşturulan fonk.
def clustering(winners):
    selected = winners.copy()
    total = 0
    totals_array = []
    diveders = []
    rows = []

    for n in range(quantity):
        diveders.append(2)

    for j in range(1, sheet.nrows):
        column = sheet.row_values(j, 0).copy()
        rows.append(column)
    #uzaklıklar kontrol edilerek noktaların hangi centroide ait olduğu bulunur centroid 2 boyutlu arrayde tutulur
    for l in range(quantity):
        temp_cluster = []
        for j in range(len(rows)):
            for i in range(len(chosen_numbers)):
                for k in range(len(rows[i])):
                    a = pow(selected[i][k] - rows[j][k], 2)
                    total += a
                totals_array.append(sqrt(total))
                total = 0
            index = totals_array.index(min(totals_array))
            totals_array = []

            if index == l:
                temp_cluster.append(rows[j])
        clusters.append(temp_cluster)

optimum_centroid_choise()
colors = ['b','g','r','c','m','y','k','w']
colors2 = ['bo', 'go', 'ro', 'co', 'mo',"yo", 'ko', 'wo']

print("Lütfen 0 - " + str((sheet.ncols) - 1) + " aralığında giriniz.")
x_eksen = int(input("x ekseni: "))  #
y_eksen = int(input("y ekseni: "))  # kullanıcıdan grafikteki x,y,z eksenini almak için
z_eksen = int(input("z ekseni: "))  #
div = 50
x_ = int(max(columns[x_eksen]) + (max(columns[x_eksen]) / div))
y_ = int(max(columns[y_eksen]) + (max(columns[y_eksen]) / div ))
xx_ = int(min(columns[x_eksen]) - (min(columns[x_eksen]) / div))
yy_ = int(min(columns[y_eksen]) - (min(columns[y_eksen]) / div))
centroid_size = 100

def twoD():
    plt.title("K- Means Kümeleme \n")
    for aa in range(len(clusters)):
        for aa2 in range(len(clusters[aa])):
            plt.scatter(clusters[aa][aa2][x_eksen], clusters[aa][aa2][y_eksen], c=colors[aa])
    for bb in range(quantity):
        plt.scatter(centroids[bb][y_eksen], centroids[bb][x_eksen], c=colors[bb], s=centroid_size,
                    edgecolors='k', marker="s")  # ağırlık merkezini grafikte göstermek için

    plt.axis([xx_, x_, yy_, y_])
    plt.show()
def threeD():
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    plt.title("K- Means Kümeleme \n")
    for a in range(len(clusters)):
        for a2 in range(len(clusters[a])):
            ax.scatter3D(clusters[a][a2][x_eksen], clusters[a][a2][y_eksen], clusters[a][a2][z_eksen], color=colors[a]);

    for b in range(quantity):
        ax.scatter3D(centroids[b][x_eksen], centroids[b][y_eksen], centroids[b][z_eksen], color=colors[b], marker="s",
                     s=centroid_size,
                     edgecolors='k');

    fig.show()
def screenWriter():
    print("Clusters :")
    print("")
    for clu in range(len(clusters)):
        print("centroid " + str(clu) + ": " + str(selected[clu]))
        print("Bu centroidin oluşturduğu cluster :")
        print(str(len(clusters[clu])) + " adet nokta bulnmaktadır")
        cluu = 0
        while cluu < len(clusters[clu]):
            if cluu < len(clusters[clu]):
                sys.stdout.write(str(clusters[clu][cluu]) + " - ")
                cluu += 1
            if cluu % 3 == 0:
                print("")
        print("")
        print("")
twoD()
threeD()
screenWriter()