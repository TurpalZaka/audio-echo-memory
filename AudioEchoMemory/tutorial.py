import time
from audio import play_key, success, fail, KEY_FREQS

def run_tutorial(get_key_fn):
    print("Tutorial: Learn keys 1–4. Press the key that matches the tone you hear.")
    order = list(KEY_FREQS.keys())
    for k in order:
        while True:
            play_key(k)
            time.sleep(0.15)
            pressed = get_key_fn()
            if pressed == k:
                success()
                print(f"Correct: {k}")
                break
            else:
                fail()
                print("Wrong, try again.")
    print("Tutorial completed.")
    return True
