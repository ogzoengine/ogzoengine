This game engine is based on pygame. Our goal is to make it easy for people, even those who don't know python or coding, to create games.

If you want to get started with this game engine by creating a sample game,

### **How to Download**

First, you need to download Python. You can do this by going to the [Python official website](https://www.python.org/downloads/) and downloading it according to your operating system.

After downloading, to check, you can write this code in the terminal or CMD:
``` 
python --version
```
**If the result is ```Python 3.11.5``` or higher, you are ready to download the game engine. You can do this by typing the following code in the terminal or CMD:**
``` 
pip install ogzoengine
```

Download a code editor of your choice. Recommended code editors are:
- **Visual Studio**: It has powerful debugging and code completion features but can be challenging for beginners and takes up a lot of space. [Visual Studio Code Download Page](https://code.visualstudio.com/Download)
- **PyCharm**: Specifically made for the Python language, it provides a fast and efficient coding experience but the full version is not free. [PyCharm Download Page](https://www.jetbrains.com/pycharm/download/)
- **Sublime Text**: It's fast and lightweight, offering quick performance, but the full version is paid and updates are not frequent. [Sublime Text Download Page](https://www.sublimetext.com/download)
- **Atom**: It has good auto-completion and provides GitHub assistance with integrated Git support, but it may cause high memory usage for some users. [Atom Download Page](https://www.atom.io/)
- **Notepad++**: It's simple and takes up less storage space, but it has a poor interface and lacks features like code completion. [Notepad++ Download Page](https://notepad-plus-plus.org/downloads/)

****
## **Coding**

```
import ogzoengine as og

screen1 = og.Screen()

# Variables
width, height = 1200, 600

# Drawwing
circle1 = og.Circle(200,200,25,[255,255,255])
line1 = og.Line(200,300,100,150,[255,255,255],3)
squ1 = og.Square(500,500,45,45,[255,255,255])
text1 = og.Text(350,350,"Hello",None,20,(255,255,255))

saved = None
# listener function
def listener():
    if og.inputs(screen1.return_keys(),'a').return_key():
        print("a clicked")

# drawwing function
def draw():
    circle1.draw(screen1)
    line1.draw(screen1)
    squ1.draw(screen1)
    text1.draw(screen1)

# While function 
def whiles():
    pass

# Using function
screen1.use_drawing(draw)
screen1.use_while(whiles)
screen1.use_listener(listener)


screen1.set_screen(width,height,"Engine test")
screen1.run()
```
