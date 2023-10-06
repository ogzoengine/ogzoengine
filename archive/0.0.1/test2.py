import ogengine.engine as o # Ana motoru çalıştırın

# Ekranın boyutunu ve adını değiştirir
o.set_screen("Caption", (800, 600))

# Ekran arkaplanını değiştirin
o.set_background_color(o.black)

# Font ayarlama
o.set_font('test_assets//font//main.ttf')

# Tekrar döngüsünü buradan kontrol edebilirsiniz
o.whiles_sys(True)

