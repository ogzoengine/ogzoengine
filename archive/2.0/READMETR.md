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

```
import BS.engine as bs

screen1 = bs.Screen()

# Varyantlar
width, height = 1200, 600

# Çizimler
circle1 = bs.Circle(200,200,25,[255,255,255])
line1 = bs.Line(200,300,100,150,[255,255,255],3)
squ1 = bs.Square(500,500,45,45,[255,255,255])
text1 = bs.Text(350,350,"Hello",None,20,(255,255,255))

saved = None
# Klavye algılama fonksiyonu
def listener():
    if bs.inputs(screen1.return_keys(),'a').return_key():
        print("a clicked")

# Çizim fonksiyonu
def draw():
    circle1.draw(screen1)
    line1.draw(screen1)
    squ1.draw(screen1)
    text1.draw(screen1)

# Tekrar Fonksiyonu
def whiles():
    pass

# Fonksiyonları çağırma işlemleri
screen1.use_drawing(draw)
screen1.use_while(whiles)
screen1.use_listener(listener)


screen1.set_screen(width,height,"Engine test")
screen1.run()
```