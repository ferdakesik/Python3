
def urunEkle(urunAdi,fiyat,stoktami,kategoriler):
    urun={
        "urunAdi":urunAdi,
        "fiyat":fiyat,
        "stoktami":stoktami,
        "kategoriler":kategoriler
    }

    import json
    with open("urunler.json","w") as file:
        json.dump(urun,file,ensure_ascii=False,indent=2)


urunEkle("LG",13000,True,["TV","ELEKTRONIK"])

def urunleriGetir():
    import json
    with open("urunler.json") as file:
        urun=json.load(file)

    kategoriler=" ".join([kategori for kategori in urun["kategoriler"]])
    print(kategoriler)
    print(f'urun adi:{urun["urunAdi"]} fiyat:{urun["fiyat"]} kategoriler:{kategoriler}')
urunleriGetir()
