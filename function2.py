
# #encapsulation
# def dis_fonksiyon(sayi1):
#     print("dis fonksiyon calisti")
#     def ic_fonskyion(sayi1):
#         print("ic fonskyion calisti")
#         return sayi1 **2
#     sayi2 = ic_fonskyion(sayi1)
#     print(sayi2,sayi1)
#
# dis_fonksiyon(5)


def faktoriyel(number):
    if not isinstance(number,int):
        raise TypeError("girdiginiz veri tam sayi olmali")
    if not number>=0:
        raise ValueError("girdiginiz sayi sifirdan buyuk olmali")
    def ic_fak(number):
        if number <= 1:
            return 1
        return number * ic_fak(number-1)
    return ic_fak(number)

try:
    print(faktoriyel(-2))
except Exception as e:
    print(e)


