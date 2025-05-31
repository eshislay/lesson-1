class fruit:
    taste = "sweet"

    def __init__(self, name, color):
     self.name = name
     self.color = color

apple = fruit("Apple", "Red")
banana = fruit("Banana", "Yellow")

print(f"{apple.name} is {apple.color} and tastes {apple.taste}.")
print(f"{banana.name} is {banana.color} and tastes {banana.taste}.")
