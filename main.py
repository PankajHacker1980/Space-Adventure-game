import random
import time

class SpaceAdventure:
    def __init__(self):
        self.player_name = ""
        self.ship_health = 100
        self.fuel = 100
        self.money = 0
        self.planets_visited = []
        self.current_event = None
        self.events = [
            {"name": "Asteroid Belt", "description": "Navigate through a dangerous asteroid belt.", "health_loss": 20, "fuel_loss": 30},
            {"name": "Trading Post", "description": "Visit a trading post to buy and sell goods.", "options": ["Buy Fuel", "Sell Resources"]},
            {"name": "Alien Encounter", "description": "Interact with a friendly or hostile alien species.", "health_gain": 10, "money_gain": 50},
            {"name": "Black Hole", "description": "Navigate through a mysterious black hole.", "health_loss": 30, "fuel_loss": 50},
            {"name": "New Planet", "description": "Land on a new planet to explore its resources.", "options": ["Explore", "Leave"]}
            # Add more events as needed
        ]
    
    def display_status(self):
        print(f"\n--- {self.player_name}'s Space Adventure ---")
        print(f"Ship Health: {self.ship_health}")
        print(f"Fuel Level: {self.fuel}")
        print(f"Money: {self.money}")
        print(f"Planets Visited: {', '.join(self.planets_visited)}")
    
    def choose_player_name(self):
        self.player_name = input("Enter your name, Captain: ").strip()
        print(f"Welcome aboard, {self.player_name}!")
    
    def encounter_event(self):
        self.current_event = random.choice(self.events)
        print(f"\nYou encounter: {self.current_event['name']}")
        print(self.current_event['description'])
        time.sleep(1)
        
        if self.current_event['name'] == "Asteroid Belt":
            self.ship_health -= self.current_event['health_loss']
            self.fuel -= self.current_event['fuel_loss']
            print(f"Your ship took {self.current_event['health_loss']} damage.")
            print(f"You lost {self.current_event['fuel_loss']} fuel navigating the asteroid belt.")
        elif self.current_event['name'] == "Trading Post":
            self.visit_trading_post()
        elif self.current_event['name'] == "Alien Encounter":
            self.interact_with_alien()
        elif self.current_event['name'] == "Black Hole":
            self.ship_health -= self.current_event['health_loss']
            self.fuel -= self.current_event['fuel_loss']
            print(f"You ventured through the black hole, losing {self.current_event['health_loss']} health and {self.current_event['fuel_loss']} fuel.")
        elif self.current_event['name'] == "New Planet":
            self.explore_new_planet()
    
    def visit_trading_post(self):
        print("\nWelcome to the Trading Post!")
        print("What would you like to do?")
        for idx, option in enumerate(self.current_event['options'], start=1):
            print(f"{idx}. {option}")
        
        choice = input("Enter your choice (1-2): ").strip()
        if choice == "1":
            if self.money >= 50:
                self.fuel += 20
                self.money -= 50
                print("You bought 20 units of fuel.")
            else:
                print("You don't have enough money to buy fuel.")
        elif choice == "2":
            resources_sold = random.randint(10, 30)
            self.money += resources_sold
            print(f"You sold resources for {resources_sold} money.")
        else:
            print("Invalid choice.")
    
    def interact_with_alien(self):
        friendly_chance = random.random()
        if friendly_chance < 0.5:
            self.ship_health += self.current_event['health_gain']
            self.money += self.current_event['money_gain']
            print("You encountered a friendly alien species.")
            print(f"You gained {self.current_event['health_gain']} health and {self.current_event['money_gain']} money.")
        else:
            damage_taken = random.randint(10, 30)
            self.ship_health -= damage_taken
            print("You encountered a hostile alien species.")
            print(f"You took {damage_taken} damage.")
    
    def explore_new_planet(self):
        print("\nYou landed on a new planet.")
        time.sleep(1)
        for option in self.current_event['options']:
            print(f"- {option}")
        choice = input("Enter your choice (explore/leave): ").strip().lower()
        
        if choice == "explore":
            resources_found = random.randint(1, 3)
            self.money += resources_found * 10
            self.planets_visited.append(self.current_event['name'])
            print(f"You explored the planet and found {resources_found} resources.")
            print(f"You earned {resources_found * 10} money.")
        elif choice == "leave":
            print("You decide to leave the planet.")
        else:
            print("Invalid choice.")
    
    def play_game(self):
        self.choose_player_name()
        
        while self.ship_health > 0:
            self.display_status()
            action = input("\nEnter your action (explore/quit): ").strip().lower()
            
            if action == "quit":
                print("Exiting the Space Adventure. Goodbye, Captain!")
                break
            elif action == "explore":
                self.encounter_event()
            else:
                print("Invalid action. Choose explore or quit.")
            
            if self.ship_health <= 0:
                print("Your ship has been destroyed. Game over.")
                break
        
        if self.ship_health > 0:
            print("Congratulations, Captain! You have completed your Space Adventure.")

if __name__ == "__main__":
    game = SpaceAdventure()
    game.play_game()
