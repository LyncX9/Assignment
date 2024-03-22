def hitung_harga_jual(kosmetik):
    harga_jual = {}
    for nama, harga_beli in kosmetik.items():
        harga_jual_baru = harga_beli * 1.10
        harga_jual[nama] = harga_jual_baru
    return harga_jual

kosmetik = {
    "Foundation": 10,
    "Bedak tabur": 6,
    "Lipstik": 5,
    "Mascara": 6,
    "Eyeliner": 4,
    "Blush on": 8,
    "Eyeshadow palette": 13,
    "Concealer": 7,
    "Highlighter": 8,
    "Setting spray": 6
}

harga_jual = hitung_harga_jual(kosmetik)

print("Supplier Price:")
for nama, harga_beli in kosmetik.items():
    print(f"{nama}: ${harga_beli:.2f}")

print("\nPrice:")
for nama, harga_jual_baru in harga_jual.items():
    print(f"{nama}: ${harga_jual_baru:.2f}")