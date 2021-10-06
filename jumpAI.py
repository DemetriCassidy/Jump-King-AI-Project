import time
import gym
from jump.percepts import Percepts
from jump.jumpCommand import JumpCommand as jc
from jump.jumpEnviroment import JumpKingEnv
import numpy as np
from jump.agent import Agent
    
if __name__ == '__main__':        
    #Focus on Jump King
    jumpEyes = Percepts()
    jumpEyes.find_window_wildcard("Jump King")
    jumpEyes.set_foreground()
    
    #Setup Agent
    #Must have the game already running and in a session
    #Game must be played in windowed x2 mode
    env = JumpKingEnv()
    king = Agent(alpha=.00001, n_actions = env.action_space.n)
    gameNum = 10
    
    bestScore = env.reward_range[0]
    scoreHistory = []
    averageScoreHistory = []
    runScoreHistory = np.zeros((gameNum,50))
    demo = False
    
    king.load_models()
    episode = 0
    for i in range(gameNum):
        observation = env._reset()
        done = False
        score = 0
        moveNum = 0
        while not done:
            action = king.choose_action(observation)
            observation_, reward, done, info = env._step(action)
            score += reward
            runScoreHistory[episode][moveNum] = reward
            moveNum += 1
            if not demo:
                king.learn(observation, reward, observation_, done)
            observation = observation_
        
        episode += 1
        scoreHistory.append(score)
        averageScore = np.mean(scoreHistory[-10:])
        averageScoreHistory.append(averageScore)
        
        king.lowerExploration()
        np.savetxt('runScoreHistory.csv', runScoreHistory, delimiter=',')
        
        if averageScore > bestScore:
            bestScore = averageScore
            if not demo:
                king.save_models()
        
        print('Game ', i, ', Score: %.1f' % score,', Average Score: %.1f' % averageScore) 
        
    
