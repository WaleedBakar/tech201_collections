story1 = {"start": "Waleed woke up on a random Sunday feeling strange. He soon realized he had gained powers to control the wind.",
          "middle": "Waleed decided to use his powers for good and became a superhero named Waleed the Windrider. He quickly became famous for his bravery and the amazing feats he accomplished.",
          "end": "Years passed and Waleed the Windrider was known as one of the greatest superheroes the world had ever seen. His legend lived on, inspiring future generations to do good in the world."}

print("The entire dictionary:")
print(story1)


print(type(story1))


print(story1.keys())


print(story1.values())


print("Start: " + story1["start"])
print("Middle: " + story1["middle"])
print("End: " + story1["end"])

story1["hero"] = "Waleed the Windrider"

print(story1)
