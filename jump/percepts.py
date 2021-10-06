import win32gui
from PIL import ImageGrab
import cv2
import re

class Percepts:
    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)
        
    
    def findTheKing(self):
        #This number is tailored to my 1920x1080 monitor with game window not moving after booting game up and window size being 960x720
        gameCap = ImageGrab.grab(bbox=(480,171,1440,890))
        gameCap.save('currentScreen.jpg')
        
        method = cv2.TM_SQDIFF_NORMED
        
        #Finds the King's location
        kingImg = cv2.imread('leftKing.jpg')
        gameImg = cv2.imread('currentScreen.jpg')
        result = cv2.matchTemplate(kingImg, gameImg, method)
        
        _,_,mnLoc,_ = cv2.minMaxLoc(result)
        
        kingX, kingY = mnLoc
        
        #Identifies the screen King is on
        screensImg = cv2.imread("tempjumpKingScreens.png")
        cropGameImg = gameImg[0:720, 0:50]
        sResult = cv2.matchTemplate(cropGameImg, screensImg, method)
        
        _,_,minLoc,_ = cv2.minMaxLoc(sResult)
        
        screenX,_ = minLoc
        screen = 1
        if screenX > 0:
            #Div by 50 because of composite img of all screens
            screen = (screenX // 50)+1
        
        return (kingX, kingY, screen)