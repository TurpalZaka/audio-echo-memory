import os

PATH = "high_score.txt"

def load_highscore():
    if not os.path.exists(PATH):
        return 0
    try:
        return int(open(PATH, "r", encoding="utf-8").read().strip())
    except:
        return 0

def save_highscore(score:int):
    with open(PATH, "w", encoding="utf-8") as f:
        f.write(str(score))
