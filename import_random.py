import random

moods = ["happy", "sad", "excited", "calm", "angry", "content", "anxious", "relaxed"]
today_mood = random.choice(moods)

print(f"Today's mood is {today_mood}.")
if today_mood == "happy":
    print("Enjoy your day!!")
elif today_mood == "sad":
    print("Cheer up!")
elif today_mood == "excited":
    print("Get ready for an amazing day!")
elif today_mood == "calm":
    print("Take a deep breath and relax.")
elif today_mood == "angry":
    print("Stay calm and find your inner peace.")
elif today_mood == "content":
    print("Appreciate the present moment.")
elif today_mood == "anxious":
    print("Take it one step at a time.")
elif today_mood == "relaxed":
    print("Take a break and enjoy some downtime.")
else:
    print("Unknown mood.")