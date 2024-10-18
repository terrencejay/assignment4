import random

mood = ["Happy", "Sad", "Angry","Calm","relaxed","anxious","Depressed"]
days =["Monday","Tuesday","Wedenesday","Thursday","Friday","Saturday","Sunday"]

for day in days:
    feelings = random.choice(mood)
    print (f"On {day} you were feelings {feelings}")