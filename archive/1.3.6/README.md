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

First, we import the library and then add the screen and input process.
```
import ogzoengine

screen = ogzoengine.GameEngine()
input = ogzoengine.Input()
```

We set the size and title of the screen. The 1st value represents width, the 2nd value represents height, and the 3rd value represents the title.
```
screen.set_screen(800, 600, "Test Game")
```

We set the background color using the RGB code.
```
screen.set_background((0,0,0))
```

We create a function for the game loop.
```
def whiles():
```

Inside the game loop function, we set the drawing basics.
```
                         # (start_x, start_y, x_end, y_end, rgb_code, thickness)
    line1 = ogzoengine.Line(250, 300, 130, 130, (255,255,255), 5)
                             # (x_position, y_position, size, rgb_code)
    circle1 = ogzoengine.Circle(100, 200, 50, (255, 0, 0))
                             # (x_position, y_position, x_size, y_size, rgb_code)
    square1 = ogzoengine.Square(400, 400, 50, 50, square1_color)
                            # (x_position, y_position, text)
    #image1 = ogzoengine.Image(400, 200, "img.png")
                         # (x_position, y_position, text, font_location, font_size, rgb_code)
    text1 = ogzoengine.Text(50, 50, "No font text", None, 20, (255, 255, 255))
```
We draw the shapes.
```
    line1.draw(screen.screen)
    circle1.draw(screen.screen)
    square1.draw(screen.screen)
    #image1.draw(screen.screen)
    text1.draw(screen.screen)
```
We set the screen to clear when the ESC key is pressed.
```
                   #(check keyboard library for key codes)
    if input.pressed('esc'):
        # Colors the screen to the selected background and clears all drawings made up to that point.
        screen.clear_screen()
```


We specify the name of the function we want to repeat.
```
screen.use_while(whiles)
```

We create functions for touching and clicking the square.
```
    if square1.mouse_touch():
       print("The mouse is touching the square")
    if square1.mouse_clicked(screen.mouse_pressed, screen.mouse_click_type, 1):
        print("The square is clicked")
```

We read the position and status of the mouse.
```
    # Read the mouse position
    mouse_pos = screen.get_mouse_pos()
    # Read the mouse status
    mouse_type = screen.get_mouse_info()
```


Run the screen
```
screen.run()
```