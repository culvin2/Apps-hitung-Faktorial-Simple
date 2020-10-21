def fak (n):
    if n ==1:
        return 1
    else:
        return n * fak(n-1)
n = int(input("Masukkan angka yang ingin di faktorkan : "))
print(fak(n))