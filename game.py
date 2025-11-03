import random, time
from audio import play_key, success, fail, KEY_FREQS
from storage import load_highscore, save_highscore

class Game:
    def __init__(self):
        self.sequence = []
        self.score = 0
        self.high = load_highscore()
        self.allowed = list(KEY_FREQS.keys())

    def new_round(self):
        self.sequence.append(random.choice(self.allowed))
        for k in self.sequence:
            play_key(k)
            time.sleep(0.15)

    def input_phase(self, get_key_fn):
        for k in self.sequence:
            pressed = get_key_fn()
            if pressed != k:
                fail()
                self.finish(False)
                return False
        success()
        self.score += 1
        return True

    def finish(self, won_round):
        if self.score > self.high:
            self.high = self.score
            save_highscore(self.high)

def play_loop(get_key_fn):
    g = Game()
    keep = True
    while keep:
        g.new_round()
        keep = g.input_phase(get_key_fn)
    return g.score, g.high
