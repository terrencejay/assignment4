import random

mood = ["Happy", "Sad", "Angry","Calm","relaxed","anxious","Depressed"]
days =["Monday","Tuesday","Wedenesday","Thursday","Friday","Saturday","Sunday"]

for i in range(len(days)):
    feelings = random.choice(mood)
    print (f"On {days[i]} you were feelings {feelings}")
