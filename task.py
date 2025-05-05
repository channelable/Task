import random

class Pet:
    def __init__(self,name,species,age):
        self.name = name
        self.species = species
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Species: {self.species}, Age:{self.age}")

class Dog(Pet):
    def __init__(self, name, age, breed, colour):
        super().__init__(name, "Dog", age)
        self.breed = breed
        self.colour = colour
        self.preferences = ("Bones", "Walk")
    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}, Color: {self.colour}")
        print(f"Care Preferences: {self.preferences}")

class Cat(Pet):
    def __init__(self, name, age, breed, colour):
        super().__init__(name, "Cat", age)
        self.breed = breed
        self.colour = colour
        self.preferences = ("Fish", "Nap")

    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}, Color: {self.colour}")
        print(f"Care Preferences: {self.preferences}")

pet_dict = {}

def generate_pet_id():
    while True:
        pet_id = random.randint(100, 1000)
        if pet_id not in pet_dict:
            return pet_id
        
def add_pet():
    species = input("Enter species (Dog/Cat): ").upper()
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    breed = input("Enter breed: ")
    colour = input("Enter colour: ")

    pet_id = generate_pet_id()
    if species == "DOG":
        pet = Dog(name, age, breed, colour)
    elif species == "CAT":
        pet = Cat(name, age, breed, colour)
    else:
        print("Invalid species!")

    pet_dict[pet_id] = pet
    print(f"{species} added with ID: {pet_id}")

def view_pet():
     for i in pet_dict.items():
        print(f"\nPet ID: {pet_id}")
        pet.display_info()
def adopt_pet():
    pet_id = int(input("Enter Pet ID to adopt: "))
    if pet_id in pet_dict:
        print("You have successfully adopted!")
        pet_dict[pet_id].display_info()
        del pet_dict[pet_id]
    else:
        print("Pet ID not found!")


def main():
    while True:
        print("--- Pet Adoption Center --- \n")
        print("1. View Pets")
        print("2. Add Pet")
        print("3. Adopt Pet")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            view_pet()
        elif choice == "2":
            add_pet()
        elif choice == "3":
            adopt_pet()
        elif choice == "4":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
