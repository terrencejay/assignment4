import random
#here we have aprogram that list a random mood for different times of the day, every day of the week. seven different days, three different times, and several moods.

moody = ['Mad','Happy','Sad','Joyus','Anxious','Tired','annoyed','Excited'] #List of moods
days = ['Monday', 'Tuesday', 'Wedenesday', 'Thursday', 'Friday','Saturday','Sunday'] #List of days
times = ['Morning', 'Afternoon', 'Evening'] #list of times

for day in days: #loop through days
    for time in times: #loop through times for every day
        feelings = random.choice(moody) #select a random mood for every time
        print(f"On {day} you felt {feelings} in the {time}") #message