import time
import sys

print("Loading lyrics...")

lyrics=[
    "Kahi Na Kahi Teri Aankhein\n" 
    "Teri Baatein Par Rahe Hai Hum\n",
    "Kahina Kahin Tere Dil Mein\n" 
    "Dhadkano Mein Dhal Rahe Hai Hum\n",
    "Tu Har Lamha, Tha Mujhse Juda Chahe Dhur Tha MeinYa Pass Raha..\n" 
    "Uss Din Tu Ha Udaas Rahe\nTujhe Jis Din Hum\nNa Dikhe Na Miley",
    "Uss Din Tu Chup Chap Rahe Tujhe Jis Din Kuch Na Kahe Na Sune" 
    "Uss Din Tu Chup Chap Rahe Tujhe Jis Din Kuch Na Kahe Na Sune"
]
timings=[0.9, 0.9, 1.2, 1.5]

typing_speed = 0.05

for line,delay in zip(lyrics, timings):
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(typing_speed)
    print()
    time.sleep(delay)