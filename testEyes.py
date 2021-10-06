from jump.percepts import Percepts
from jump.jumpCommand import JumpCommand as jc
import time

if __name__ == '__main__':
    jumpEyes = Percepts()
    jumpEyes.find_window_wildcard("Jump King")
    jumpEyes.set_foreground()
    
    time.sleep(1)
    
    while True:
        result = jumpEyes.findTheKing()
        
        time.sleep(1)
        
        jc.moveLeft()
        
        print(result[0], result[1], result[2])
    