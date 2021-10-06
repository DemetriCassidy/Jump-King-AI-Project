from gym import Env
from gym.spaces import Discrete, Box
from jump.percepts import Percepts as p
from jump.jumpCommand import JumpCommand as jc
import numpy as np
import time

class JumpKingEnv(Env):
    metadata = {'render.modes': ['human']}
    
    def __init__(self):
        super(JumpKingEnv, self).__init__()
        
        #8 Different Moves
        self.action_space = Discrete(8)
        
        #[x, y, screen number]
        self.observation_space = Box(low=np.array([0,0,1]), high=np.array([960,720,44]), dtype=np.uint8)
        
        #Range of Reward
        self.reward_range = (-999999, 100000)
        self.stepsTaken = 0
        self.eyes = p()
        
        self.eyes.find_window_wildcard("Jump King")
        
    def _step(self, action):
        #Do Action
        self._take_action(action)
        state_ = self.eyes.findTheKing()
        
        #Reward Calulation
        reward = (720 - state_[1]) + (720 * (state_[2] - 1))
        
        #Update state
        self.state = state_
        self.stepsTaken += 1
        
        if self.stepsTaken == 50:
            done = True
        else:
            done = False
        
        info = {}
        
        return self.state, reward, done, info
    
    def _take_action(self, action):
        if action == 0:
            jc.moveLeft()
        elif action == 1:
            jc.moveRight()
        elif action == 2:
            jc.moveShortJumpLeft()
        elif action == 3:
            jc.moveShortJumpRight()
        elif action == 4:
            jc.moveMedJumpLeft()
        elif action == 5:
            jc.moveMedJumpRight()
        elif action == 6:
            jc.moveHighJumpLeft()
        elif action == 7:
            jc.moveHighJumpRight()
            
        #Wait for animation to play out
        time.sleep(4)
        #jc.standUp()
        
    def _render(self):
        pass
    
    def _reset(self):
        jc.resetGame()
        time.sleep(.5)
        observation = self.eyes.findTheKing()
        self.stepsTaken = 0
        return observation