# Membuat Fungsi Baru 'counterClockwise'
def counterClockwise ():

# Input Data
    listku = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]  

# Proses Pemecahan dan Penggabungan Data
    listku1 = listku[0][2],listku[1][2],listku[2][2] 
    listku1_list = list(listku1)

    listku2 = listku[0][1],listku[1][1],listku[2][1]
    listku2_list = list(listku2)

    listku3 = listku[0][0],listku[1][0],listku[2][0]
    listku3_list = list(listku3)

# Cetak 
    print('List Awal = ', listku,'\n')
    print('List Akhir = ',[listku1_list,listku2_list,listku3_list],'\n')

# Memanggil Fungsi 'counterClockwise'
counterClockwise ()