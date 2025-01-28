# Racing Car

**This project is related to the homework assigned by Fun AI 2025 camp. See the original repository for latest and further details.** 
- **[Racing car link](https://github.com/PAIA-Playful-AI-Arena/racing_car)**
- **version of this project：** 4.0.1

## Set up virtual environment(recommended) (Applicable to Racing_car version 4.0.1)
### Windows
```python
# 新建 MLGame 資料夾, 所有遊戲可以放在這裡 (Ex. Arkanoid)
mkdir MLGame 
cd MLGame

# 建立虛擬環境
python -m venv funai
# 進入虛擬環境(在MLGame中執行)
.\funai\Scripts\activate.bat

# 安裝需要的套件 (請一定要從上到下逐行執行)
pip install mlgame
pip install gymnasium
pip install scikit-learn
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118 # 安裝 pytorch (eg. cuda 11.8)
pip install stable-baselines3
pip install numpy==1.26.4
```
### Mac
```python
# 新建 MLGame 資料夾, 所有遊戲可以放在這裡 (Ex. Arkanoid)
mkdir MLGame 
cd MLGame

# 建立虛擬環境
python3 -m venv funai
# 進入虛擬環境
source funai/bin/activate

# 安裝需要的套件 (請一定要從上到下逐行執行)
pip install mlgame
pip install gymnasium
pip install scikit-learn
pip install torch torchvision torchaudio
pip install stable-baselines3
pip install numpy==1.26.4
```

### Linux
```python
# 新建 MLGame 資料夾, 所有遊戲可以放在這裡 (Ex. Arkanoid)
mkdir MLGame 
cd MLGame

# 安裝對應的 python 虛擬環境
sudo apt install python3.10-venv
# 進入虛擬環境
python3.10 -m venv funai 
# 進入虛擬環境
source funai/bin/activate 

# 安裝需要的套件 (請一定要從上到下逐行執行)
pip install mlgame
pip install gym
pip install scikit-learn
pip install torch torchvision torchaudio
pip install stable-baselines3
pip install numpy==1.26.4
```

## Game commands

**Open the cmd/powershell/Terminal in the arkanoid folder and execute the lines below regarding your needs.**

  - **玩遊戲指令** 
  ```python
    python -m mlgame -f 120 -i ml/ml_play_template.py ./ --game_type NORMAL --car_num 40 --racetrack_length 10000  --round 5 --sound off
  ```
  - **手動玩遊戲指令** 
  ```python
    python -m mlgame -f 120 -i ml/ml_play_manual.py ./ --game_type NORMAL --car_num 40 --racetrack_length 10000  --round 5 --sound off
  ```
  - **訓練遊戲指令+不顯示畫面(--nd)** 
  ```python
    python -m mlgame -f 120 --nd -i ml/rl_training_PPO.py ./ --game_type NORMAL --car_num 40 --racetrack_length 10000  --round 5 --sound off
  ```
  - **訓練遊戲指令** 
  ```python
    python -m mlgame -f 120 -i ml/rl_training_PPO.py ./ --game_type NORMAL --car_num 40 --racetrack_length 10000  --round 5 --sound off 
  ```
  - **訓練後玩遊戲指令** 
  ```python
    python -m mlgame -f 120 -i ml/rl_play_PPO.py ./ --game_type NORMAL --car_num 40 --racetrack_length 10000  --round 5 --sound off
  ```

## About homework and ML

The training model used is a PPO model. The details are in `/rl_training_PPO.py`.  
The model and log is stored in the `save` folder.
The homework is to design a reward function that can pass the racetrack of 10000 units, which is in `environment.py`.  
Furthermore, the car knows how and when to switch lane and execute it accurately.
The default training frequency is to train every 200 rounds. You can adjust it in `/rl_training_PPO.py` line 59.  
Parameters about the game can be adjusted in `game_config.json`    

The model I've trained can control the car to the finish line of the racetrack of 10000 units with over 50% probability.    

Other information such as the mechanics of the game are described in the README of the original source. Below are the information of the 4.0.1 version.
At last, wish you a happy ML experience. ^_^

# README of the root repository(version: 4.0.1)
<img src="https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/racing_car/main/asset/logo.png" alt="logo" width="100"/> 

![racing_car](https://img.shields.io/github/v/tag/PAIA-Playful-AI-Arena/RacingCar)
[![Python 3.9](https://img.shields.io/badge/python->3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![MLGame](https://img.shields.io/badge/MLGame->10.4.6a2-<COLOR>.svg)](https://github.com/PAIA-Playful-AI-Arena/MLGame)

讓你的AI控制車子，全速衝刺邁向終點，不過要小心，別撞到別人＼被別人撞到了。
![](./asset/racingcar.gif)


---
## 版本更新（4.0.1）
1. 更新遊戲畫面
2. 更新回傳資料格式，符合 `mlgame 10.4.6a2` 以上的規範

# 基礎介紹

## 啟動方式

- 直接啟動 [main.py](https://github.com/PAIA-Playful-AI-Arena/racing_car/blob/master/main.py) 即可執行

### 遊戲參數設定

```python
# main.py 
game = RacingCar.RacingCar(user_num=2, game_mode="NORMAL", car_num=50, racetrack_length=10000, rounds=1, sound="off")

```

- `user_num`：玩家數量，最多可以4個玩家同時進行同一場遊戲，如果以鍵盤控制，最多只能2位玩家。
- `game_type`：遊戲模式，分為普通模式(`NORMAL`)、重生模式(`RELIVE`)與金幣模式(`COIN`)。
- `car_num`：車子數量的上限，包含玩家與電腦的車都會被計入。
- `rounds`：遊戲重複啟動的次數，系統將計算每輪遊戲結果並提供積分。
- `sound`：可輸入`on`或是`off`，控制是否播放遊戲音效。
- `racetrack_length`：遊戲終點距離

## 玩法

- 遊戲最多可以四個人同時進行，有普通模式、金幣模式和重生模式。
- 使用鍵盤 上、下、左、右 (1P)與 Ｗ、Ａ、Ｓ、Ｄ (2P)控制自走車。
- 若車子之間發生碰撞，則雙方皆淘汰出局。
- 在重生模式下，玩家與其他車子發生碰撞時並不會出局，唯速度減速為0，並進入三秒的無敵時間，此三秒內與其他車子碰撞不會導致玩家降速。
- 在金幣模式下，玩家之間可以控制車子爭奪金幣。

## 目標

1. 普通模式：以最快的速度到達終點。
2. 金幣模式：在遊戲時間截止前，盡可能吃到更多的金幣
3. 重生模式：以最快的速度到達終點。

### 通關條件

1. 無論是何種遊戲模式，車子能順利到達終點即可過關。

### 失敗條件

1. 車子在遊戲過程中被淘汰，即算失敗。

## 遊戲系統

1. 行動機制
    - 上鍵(W鍵)：車子以3px/frame的速度向左平移
    - 下鍵(S鍵)：車子以3px/frame的速度向右平移
    - 右鍵(D鍵)：車子向前加速    
    - 左鍵(A鍵)：車子剎車減速
    
    車子的最高速度為15px/frame，當車子左右平移時速度將會略微下降為14px/frame。
    車子沒有加速或剎車時，會以0.9px/frame左右的速度怠速前進。
    
2. 座標系統
    使用pygame座標系統，左上角為(0,0)，x方向以右為正，y方向以下為正，單位為px。
    ![](https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/game-web-readme/main/racing_car/images/side1.svg)
    ![](https://raw.githubusercontent.com/PAIA-Playful-AI-Arena/game-web-readme/main/racing_car/images/side2.svg)

3. 遊戲物件
    - 螢幕大小 1000 x 700px
    - 車子大小 60 x 30px
    - 金幣大小 30 x 30px
4. 物件移動方式
    - 電腦的車
        車子從畫面左方或右方出現，不會切換車道。 前方有車(不論是電腦還是玩家)會剎車減速，否則不斷加速至最高速
        每台車最高速度皆不一樣，範圍為10~14。
    - 金幣
        隨機從畫面右方出現，以5 px/frame的速度移動。
        電腦車子碰到金幣時金幣不會消失。
    

---

# 進階說明

## 使用ＡＩ玩遊戲

```bash

# Begin from MLGame 9.5.*
python -m mlgame -i ml/ml_play_template.py ./ --game_type COIN --car_num 40 --racetrack_length 10000  --round 2 --sound off

```

遊戲參數依序是 `game_type` `car_num` `racetrack_length` `rounds` `sound`

## ＡＩ範例

```python
class MLPlay:
    def __init__(self,ai_name:str,*args,**kwargs):
        self.other_cars_position = []
        self.coins_pos = []
        self.ai_name = ai_name
        print("Initial ml script")
        print(ai_name)
        print(kwargs)

    def update(self, scene_info: dict,*args,**kwargs):
        """
        Generate the command according to the received scene information
        """
        # print(scene_info)
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        return ["SPEED"]

    def reset(self):
        """
        Reset the status
        """
        # print("reset ml script")
        pass

```

## 遊戲資訊

- scene_info 的資料格式如下

```json
{
    "frame": 25,
    "id": 1,
    "x":20,
    "y": 260,
    "all_cars_pos": [
        [20,260],
        [20,260]
    ],
    "distance": 27,
    "velocity":0.9,
    "coin_num":0,
    "coin":[
        [825,460]
    ],
    "status": "GAME_ALIVE"
}
```

- `frame`：遊戲畫面更新的編號。
- `id`:玩家的遊戲編號。
- `x`：玩家車子的Ｘ座標，表示車子的左邊座標值。
- `y`：玩家車子的Ｙ座標，表示車子的上方座標值。
- `all_cars_pos`：場景中所有車子的位置清單，清單內每一個物件都是一個車子的左上方座標值。
- `distance`：玩家目前已行近的距離。
- `velocity`:玩家目前的車速。
- `coin_num`：玩家目前吃到的金幣數量（若為普通模式則固定為0）。
- `coin`：場景中所有金幣的位置清單，清單內每一個物件都是一個金幣的左上方座標值。（若為普通模式則為空清單）。
- `status`：目前遊戲的狀態
    - `GAME_ALIVE`：遊戲進行中
    - `GAME_PASS`：遊戲通關
    - `GAME_OVER`：遊戲結束

## 動作指令

- 在 update() 最後要回傳一個字串，主角物件即會依照對應的字串行動，一次可以執行多個行動。
    - `SPEED`：向前加速
    - `BRAKE`：煞車減速
    - `MOVE_LEFT`：向左移動
    - `MOVE_RIGHT`：向右移動

## 遊戲結果

- 最後結果會顯示在console介面中，若是PAIA伺服器上執行，會回傳下列資訊到平台上。

```json
{
  "frame_used": 100,
  "status": "un_passed",
  "attachment": [
    {
        "player_num": "1P",
        "coin":1,
        "distance": "6490m",
        "single_rank":1,
        "accumulated_score":4
    }
  ]
}
```

- `frame_used`：表示使用了多少個frame
- `status`：表示遊戲結束的狀態
  - `finish`:完成此遊戲
  - `fail`:遊戲過程出現問題
  - `passed`:單人的情況下，成功走到終點，回傳通過
  - `un_passed`:單人的情況下，成功走到終點，回傳不通過
  
- `attachment`：紀錄遊戲各個玩家的結果與分數等資訊
    - `player_num`：玩家編號
    - `coin`：玩家單局吃到的金幣（若為普通模式則無此欄位）
    - `distance`：玩家單局行走的距離
    - `single_rank`：玩家單局的排名
    - `accumulated_score`：玩家的累計積分（用於玩多次遊戲時）

---
