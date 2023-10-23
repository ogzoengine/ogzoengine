# **Ogzoengine**

Bu Oyun Motoru pygame temellidir. Amacımız python hatta kodlama bile bilmeyen kişilerin kolayca oyun yapabilmesidir.

Eğer oluşturduğumuz örnek oyunla

### **Nasıl indirilir**

Öncelikle python indirmelisiniz. Bunu [pythonın ana safyasına](https://www.python.org/downloads/) gidip oradan işletim sisteminize göre indirerek yapabilirsiniz.

Bunu indirdikten sonra kontrol etmek için terminal yada CMD'ye şu kodu yazabilirsiniz:
``` 
python --version
```
**Eğer sonuç ```Python 3.11.5``` veya daha yüksek ise artık oyun motorunu indirmeye hazırsınız. Bunu terminale veya CMDye şu kodu yazarak yapabilirsiniz:**
``` 
pip install ogzoengine
```
İstediğiniz bir kod editörü indirin. Önerdiğimiz kod editörleri:
- **Visual Studio**: Güçlü hata ayıklama ve kod tamamlama özellikleri mevcuttur ama fazla yer kaplar ve yeni başlayanlar için zor olabilir. [Visual Studio Code İndirme Sayfası](https://code.visualstudio.com/Download)
- **PyCharm**: Sadece python dili için yapılmıştır buda Hızlı ve verimli bir kod yazma deneyimi sağlar ama Tam sürümü ücretsiz değildir. [PyCharm İndirme Sayfası](https://www.jetbrains.com/pycharm/download/)
- **Sublime Text**: Hızlı ve hafiftir hızlı performans verir ama Tam sürümü ücretlidir ve güncellemeler genelde sık sık gelmez. [Sublime Text İndirme Sayfası](https://www.sublimetext.com/download)
- **Atom**: İyi bir otomatik tamamlaması vardır ve entegre git desteği gibi github yardımı sağlar ama kimi kullanıcılara yüksek bellek kullanımı sorunu yaratabilir. [Atom İndirme Sayfası](https://www.atom.io/)
- **Notepad++**: Basittir ve az depolama alanı kaplar ama arayüzü kötüdür ve kod tamamlama gibi özelliklere sahip değildir. [Notepad++ İndirme Sayfası](https://notepad-plus-plus.org/downloads/)
****
## **Kodlama**

Öncelikle kütüphaneyi import ediyoruz sonra ekranı ve input işlemini ekliyoruz.
```
import ogzoengine

screen = ogzoengine.GameEngine()
input = ogzoengine.Input()
```

Ekranın boyutunu ve başlığını ayarlıyoruz. 1. Değer genişlik, 2. değer yükseklik, 3. değer başlığı temsil ediyor
```
screen.set_screen(800, 600, "Test Game")
```

Arka plan rengini rgb kodu ile ayarlıyoruz. 
```
screen.set_background((0,0,0))
```

Tekrar döngüsü için fonksiyon oluşturuyoruz.
```
def whiles():
```

Tekrar fonksiyonunun içine çizim temellerini atıyoruz
```
                         # (başlangıç_x, başlangıç_y, x_bitiş, y_bitiş, rgb_kodu, kalınlık)
    line1 = ogzoengine.Line(250, 300, 130, 130, (255,255,255), 5)
                             # (x_pozisyonu, y_pozisyonu, boyutu, rgb_kodu)
    circle1 = ogzoengine.Circle(100, 200, 50, (255, 0, 0))
                             # (x_pozisyonu, y_pozisyonu, x_boyutu, y_boyutu, rgb_kodu)
    square1 = ogzoengine.Square(400, 400, 50, 50, square1_color)
                            # (x_pozisyonu, y_pozisyonu, konumu)
    #image1 = ogzoengine.Image(400, 200, "img.png")
                         # (x_pozisyonu, y_pozisyonu, yazı, font_konumu, font_boyutu, rgb_kodu)
    text1 = ogzoengine.Text(50, 50, "No font text", None, 20, (255, 255, 255))
```
resimleri çiziyoruz
```
    line1.draw(screen.screen)
    circle1.draw(screen.screen)
    square1.draw(screen.screen)
    #image1.draw(screen.screen)
    text1.draw(screen.screen)
```
esc tuşuna basınca ekranın temizlenmesini ayarlıyoruz
```
                   #(tuşların kodları için keyboard kütüphanesine bakabilirsiniz)
    if input.pressed('esc'):
        # Ekranı seçilen arka plana boyar ve o ana kadar yapılan tüm çizimleri siler.
        screen.clear_screen()
```


Tekrar etmesini istediğimiz fonksiyonun ismini yazıyoruz
```
screen.use_while(whiles)
```
Kareye dokunma ve basma fonksiyonlarını yapıyoruz
```
    if square1.mouse_touch():
       print("fare kareye dokunuyor")
    if square1.mouse_clicked(screen.mouse_pressed, screen.mouse_click_type, 1):
        print("kareye tıklandı")
```

farenin pozisyonu ve durumunu okuyoruz
```
    # Farenin pozisyonunu oku
    mouse_pos = screen.get_mouse_pos()
    # Farenin durumunu oku
    mouse_type = screen.get_mouse_info()
```


Ekranı çalıştırın
```
screen.run()
```