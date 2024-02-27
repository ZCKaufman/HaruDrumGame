#!/usr/bin/env python3
import rospy
from HaruDrumGame.msg import DrumMidiSignal

pos = 0
score = 0
mhall_seq = ["yellow", "orange", "red", "orange", "yellow", "yellow", "yellow", "orange",
            "orange", "orange", "yellow", "blue", "blue"]

def drum_callback(sig):
    global pos, score, mhall_seq
    if(sig.delta_time > 1.0):
        print("Oh no! You took too long to hit the drum. Let's try again!")
        return
    if(sig.color == mhall_seq[pos]):
        print("Great!")
        score += 1
        pos += 1
    else:
        print("Oh no! You hit the wrong drum. Let's try again!")
    


if __name__ == "__main__":
    rospy.init_node("mhall_node", anonymous=True)

    sub = rospy.Subscriber(f"replay/00/hit", DrumMidiSignal, drum_callback)
