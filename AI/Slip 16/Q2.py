import random

actions = ["Attack", "Defend", "Run"]

for i in range(5):
    action = random.choice(actions)
    reward = random.randint(1, 10)

    print("Action:", action, "Reward:", reward)

print("Game Over")