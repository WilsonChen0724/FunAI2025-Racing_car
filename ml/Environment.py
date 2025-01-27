import gymnasium as gym
from gymnasium import spaces
import numpy as np
from sklearn.preprocessing import OneHotEncoder


class Environment(gym.Env):
    def __init__(self, n_actions, n_observations):
        super(Environment, self).__init__()
        
        # self.action_space = spaces.Discrete(n_actions) #start from 0
        # self.observation_space = spaces.Discrete(n_observations) #start from 0
        observations = np.array([i for i in range(7)])
        observations = observations.reshape(len(observations), 1)
        self.onehot_encoder = OneHotEncoder(sparse_output=False)
        self.observation_one_hot = self.onehot_encoder.fit_transform(observations)
        # print(self.observation_one_hot)
                
        self.front = 0 # 前
        self.top = 0 # 上
        self.down = 0 # 下

        self.length = -45 # 判斷上下

        self.car_size = (40, 20) # 車車多胖(x, y)

    def set_scene_info(self, scene_info):
        self.scene_info = scene_info
    
    def get_action(self):
        return self.action

    def is_hit(self, a, b, size):
        return (a + size > b - size) and (b + size > a - size)

    #設定observation
    def reset(self):        
        if self.scene_info["velocity"] < 10:
            self.length = -60
        cars_pos = self.scene_info["all_cars_pos"]
        position = cars_pos[0]

        observation = 0
        self.front = 0
        self.top = 0
        self.down = 0
        for i in range (1,len(cars_pos)):
            if self.is_hit(cars_pos[i][1], position[1], self.car_size[1]):    # 同賽道有車
                if self.is_hit(cars_pos[i][0], position[0]+self.car_size[0]*2, self.car_size[0]*2):   # 前方有車
                    self.front = 1
                    break
            else:
                self.front = 0
    
        if self.front == 1:  # 如果前方有車
            for j in range(1,len(cars_pos)):
                if self.is_hit(cars_pos[i][1], position[1] - 30, self.car_size[1]) and self.is_hit(cars_pos[i][0], position[0], self.car_size[0]): # 上方有車
                    self.top = 1
                if self.is_hit(cars_pos[i][1], position[1] + 30, self.car_size[1]) and self.is_hit(cars_pos[i][0], position[0], self.car_size[0]): # 下方有車
                    self.down = 1

        if position[1] < 120:
            self.top = 1
        if position[1] > 530:
            self.down = 1

        if self.front == 0:          # 前方沒車
            if self.top == 1:     # 沒車-但在最上面的賽道
                # print("沒車-但在頂部")
                observation = 2 
            elif self.down == 1:     # 沒車-但在最下面的賽道
                # print("沒車-但在尾部")
                observation = 1 
            else:
                # print("沒車")
                observation = 0  

        elif self.front == 1 :     # 前方有車
            if self.top == 1 and self.down == 1:   # 上下前都有車
                observation = 3 
                # print("上下前都有車")
            elif self.top == 1:       # 上前有車
                observation = 4 
                # print("上前有車")
            elif self.down == 1:     # 前下有車
                observation = 5 
                # print("前下有車")
            else:                    # 只有前面有車
                observation = 6 
                # print("前面有車")
        else:
            pass
        
        # reward, done, info can't be included
        return self.observation_one_hot[observation]



    def step(self, action):      
        reward = 0
        # action => 0: brake / 1: speed / 2: left / 3: right / 4: nothing

        observation = self.reset()

        ###########################################
        # TODO : 請自行設定reward的數值
        if np.array_equal(observation, self.observation_one_hot[0]):      # 前方沒車
            if action == 0:
                reward += -10
            if action == 1:
                reward += 15
            if action == 2:
                reward += -10
            if action == 3:
                reward += -10
            if action == 4:
                reward += -10
            
        if np.array_equal(observation, self.observation_one_hot[1]):      # 前方沒車且車子在路線上方
            if action == 0:
                reward += -10
            if action == 1:
                reward += -5       
            if action == 2:
                reward += -10
            if action == 3:
                reward += 15      
            if action == 4:
                reward += -10
            
        if np.array_equal(observation, self.observation_one_hot[2]):      # 前方沒車且車子在路線下方
            if action == 0:
                reward += -10
            if action == 1:
                reward += -5     
            if action == 2:
                reward += 15   
            if action == 3:
                reward += -10
            if action == 4:
                reward += -10
            
        if np.array_equal(observation, self.observation_one_hot[3]):      # 上下前都有車
            if action == 0:
                reward += 5
            if action == 1:
                reward += -20
            if action == 2:
                reward += -10
            if action == 3:
                reward += -10
            if action == 4:
                reward += 10

        if np.array_equal(observation, self.observation_one_hot[4]):      # 前上有車
            if action == 0:
                reward += -15
            if action == 1:
                reward += -30
            if action == 2:
                reward += -35
            if action == 3:
                reward += 25
            if action == 4:
                reward += -25
                
        if np.array_equal(observation, self.observation_one_hot[5]):      # 前下有車
            if action == 0:
                reward += -15
            if action == 1:
                reward += -30
            if action == 2:
                reward += 25
            if action == 3:
                reward += -35
            if action == 4:
                reward += -25
        
        if np.array_equal(observation, self.observation_one_hot[6]):      # 只有前面有車
            if action == 0:
                reward += -15
            if action == 1:
                reward += -35
            if action == 2:
                reward += 15
            if action == 3:
                reward += 15
            if action == 4:
                reward += -25
        ###########################################

        if self.scene_info["status"] != "GAME_ALIVE":
            done = 1
            reward -= 1000
        else:
            done = 0

        info = {}

        return observation, reward, done, info