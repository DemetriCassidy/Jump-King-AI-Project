from pynput.keyboard import Key, Controller
import time
keyboard = Controller()

def tapKey(k):
        keyboard.press(k)
        time.sleep(.3)
        keyboard.release(k)
        time.sleep(.5)

def correctPos():
    time.sleep(.1)
    keyboard.press(Key.left)
    time.sleep(.01)
    keyboard.release(Key.left)
    time.sleep(3)
    
class JumpCommand:
        
    def resetGame():
        tapKey(Key.esc)

        for i in range(3):
            tapKey(Key.down)
            
        
        tapKey(Key.space)
        tapKey(Key.down)
        tapKey(Key.space)
        time.sleep(.5)
        
        tapKey(Key.space)
        time.sleep(.3)
        tapKey(Key.space)
        time.sleep(2)
        
        tapKey(Key.space)
        tapKey(Key.down)
        tapKey(Key.down)
        tapKey(Key.space)
        tapKey(Key.down)
        tapKey(Key.space)
        time.sleep(9)

    def moveLeft():
        keyboard.press(Key.left)
        time.sleep(.1)
        keyboard.release(Key.left)
        correctPos()
        
    def moveRight():
        keyboard.press(Key.right)
        time.sleep(.1)
        keyboard.release(Key.right)
        
    def moveShortJumpLeft():
        keyboard.press(Key.left)
        keyboard.press(Key.space)
        time.sleep(.1)
        keyboard.release(Key.space)
        keyboard.release(Key.left)
        correctPos()

    def moveShortJumpRight():
        keyboard.press(Key.right)
        keyboard.press(Key.space)
        time.sleep(.1)
        keyboard.release(Key.space)
        keyboard.release(Key.right)
    
    def moveMedJumpLeft():
        keyboard.press(Key.left)
        keyboard.press(Key.space)
        time.sleep(.3)
        keyboard.release(Key.space)
        keyboard.release(Key.left)
        correctPos()
    
    def moveMedJumpRight():
        keyboard.press(Key.right)
        keyboard.press(Key.space)
        time.sleep(.3)
        keyboard.release(Key.space)
        keyboard.release(Key.right)
    
    def moveHighJumpLeft():
        keyboard.press(Key.left)
        keyboard.press(Key.space)
        time.sleep(.6)
        keyboard.release(Key.space)
        keyboard.release(Key.left)
        correctPos()
        
    def moveHighJumpRight():
        keyboard.press(Key.right)
        keyboard.press(Key.space)
        time.sleep(.6)
        keyboard.release(Key.space)
        keyboard.release(Key.right)
    
    def standUp():
        keyboard.press(Key.space)
        time.sleep(.1)
        keyboard.release(Key.space)
        time.sleep(1)