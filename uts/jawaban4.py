def pilih():
    a = "capucino"
    b = "teh"
    print("pilihan")
    print("1.",a)
    print("2.",b)
    print("3. EXIT")

def capucino():
    cap = "memilih capucino"
    print(cap)
    capucino = int(input("masukan harga : "))
    ppn = 10/100
    pajak = capucino*ppn
    total = capucino+pajak
    print("jumlah yang harus dibayar : ",total)

def teh():
    teh = "memilih teh"
    print(teh)
    teh = int(input("masukan harga : "))
    ppn = 10/100
    pajak = teh*ppn
    total = teh+pajak
    print("jumlah yang harus dibayar : ",total)

while True:
    pilih()
    pil = int(input("masukkan pilihan :"))
    if pil == 1:
        capucino()
    elif pil == 2:
        teh()
    elif pil == 3:
        break
    else:
        print("pilihan salah")