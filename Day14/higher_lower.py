from data_dict import data
import random
#person1=random.choice(data)
#person2=random.choice(data)
while True :
    person1=random.choice(data)
    person2=random.choice(data)
    print(person1['name'])
    print(person2['name'])
    choice=input("Who has higher follower count?")
    if choice==person1["name"] and person1["follower_count"]< person2["follower_count"]:
        print("Wrong!")
        break
