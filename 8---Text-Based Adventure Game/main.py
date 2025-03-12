import random

def print_color(text, text_color="reset", bg_color=None, bold=False):
    colors = {
        "reset": "\033[0m",
        "black": "\033[30m", "red": "\033[91m", "green": "\033[92m",
        "yellow": "\033[93m", "blue": "\033[94m", "magenta": "\033[95m",
        "cyan": "\033[96m", "white": "\033[97m"
    }
    
    bg_colors = {
        "black": "\033[40m", "red": "\033[41m", "green": "\033[42m",
        "yellow": "\033[43m", "blue": "\033[44m", "magenta": "\033[45m",
        "cyan": "\033[46m", "white": "\033[47m"
    }
    
    text_code = colors.get(text_color, colors["reset"])
    bg_code = bg_colors.get(bg_color, "")
    bold_code = "\033[1m" if bold else ""

    print(f"{bold_code}{bg_code}{text_code}{text}{colors['reset']}")

class Character:
    def __init__(self, name, char_class, Hp, Atk, Mp, Durability):
        self.name = name
        self.char_class = char_class
        self.health = Hp
        self.max_health = Hp
        self.attack = Atk
        self.magic = Mp
        self.armor = Durability
        self.level = 1
        self.xp = 0
        self.gold = 100
        self.inventory = {"Health Potion": 2}

    def level_up(self):
        self.level += 1
        self.max_health += 10
        self.health = self.max_health
        self.attack += 2
        self.magic += 2
        self.armor += 1
        print_color("\n✨ You leveled up! Your stats have increased!", "light_yellow")

    def show_stats(self):
        print_color(f"\n📜 {self.name} the {self.char_class} | Level {self.level}", "cyan", "white", bold=True)
        print_color(f"❤️ Health: {self.health}/{self.max_health} | ⚔️ Attack: {self.attack} | 🔮 Magic: {self.magic} | 🛡 Armor: {self.armor}", "cyan")
        print_color(f"💰 Gold: {self.gold} | 🎒 Inventory: {self.inventory}", "cyan")

def combat(player, enemy):
    print_color(f"\n⚔️ A Wild {enemy['name']} appears!", "red")

    while player.health > 0 and enemy["health"] > 0:
        print("\n1️⃣ Attack  2️⃣ Magic  3️⃣ Use Item  4️⃣ Run")
        action = input("Choose Action: ").strip()

        if action == "1":
            damage = max(1, player.attack - enemy['armor'])
            enemy["health"] -= damage
            print_color(f"⚔️ You hit the {enemy['name']} for {damage} damage!", "cyan")

        elif action == "2":
            if player.magic > 0:
                damage = player.magic * 2
                enemy["health"] -= damage
                print_color(f"🔮 You cast a spell and deal {damage} magic damage!", "light_yellow")
                player.magic -= damage // 2
            else:
                print_color("❌ Not enough magic!", "red")

        elif action == "3":
            if player.inventory.get("Health Potion", 0) > 0:
                player.health = min(player.max_health, player.health + 20)
                player.inventory["Health Potion"] -= 1
                print_color("🍷 You used a Health Potion! Health restored.", "blue")
            else:
                print_color("❌ No potions left!", "red")

        elif action == "4":
            if random.random() > 0.3:
                print_color("🏃‍♂️ You successfully ran away!", "green")
                return
            else:
                print_color("❌ Escape failed!", "black")

        if enemy["health"] > 0:
            enemy_damage = max(1, enemy["attack"] - player.armor)
            player.health -= enemy_damage
            print_color(f"💥 The {enemy['name']} attacks you for {enemy_damage} damage!", "magenta")

        if player.health <= 0:
            print_color("\n💀 You have been defeated...", "black")
            exit()
    
    print_color(f"\n🎉 You defeated the {enemy['name']}!", "blue")
    player.xp += enemy["xp"]
    player.gold += enemy["gold"]
    print_color(f"💰 You found {enemy['gold']} gold!", "yellow")

    if player.xp >= player.level * 10:
        player.level_up()

def explore(player):
    print_color("\nYou stand at a crossroad. Where do you go?", "white")
    print("1️⃣ Forest  2️⃣ Village  3️⃣ Dungeon  4️⃣ Castle")
    choice = input("Enter Choice: ").strip()

    if choice == "1":
        print_color("\n🌲 You enter the Dark Forest...", "green")
        if random.random() > 0.5:
            combat(player, {"name": "Goblin", "health": 30, "attack": 5, "armor": 2, "xp": 5, "gold": 8})
        else:
            print_color("🍄 You find some herbs and gain 5 gold!", "yellow")
            player.gold += 5

    elif choice == "2":
        print("\n🏡 You arrive at the village.")
        print("1️⃣ Shop  2️⃣ Rest")
        sub_choice = input("Enter choice: ").strip()
        
        if sub_choice == "1":
            print("\n🛒 Welcome to the shop!")
            print("1️⃣ Buy Health Potion (10 gold)  2️⃣ Leave")
            shop_choice = input("Enter choice: ").strip()
            if shop_choice == "1" and player.gold >= 10:
                player.inventory["Health Potion"] += 1
                player.gold -= 10
                print_color("🛒 Purchased Health Potion!", "blue")
            else:
                print_color("❌ Not enough gold!", "red")

        elif sub_choice == "2":
            print_color("\n😴 You rest at the inn and regain full health!", "green")
            player.health = player.max_health

    elif choice == "3":
        print("\n🕳️ You descend into the dungeon...")
        combat(player, {"name": "Skeleton Warrior", "health": 40, "attack": 7, "armor": 3, "xp": 10, "gold": 15})

    elif choice == "4":
        print("\n🏰 You approach the Dark Lord's castle...")
        combat(player, {"name": "Dark Lord", "health": 100, "attack": 15, "armor": 8, "xp": 50, "gold": 100})

    else:
        print_color("Invalid choice.", "red")

def choose_character(name):
    print_color("\nChoose your class:", "red")
    print_color("1️⃣ Warrior (High attack & armor)", "cyan")
    print_color("2️⃣ Mage (Powerful magic)", "cyan")
    print_color("3️⃣ Rogue (Agile and critical strikes)", "cyan")

    choice = input("Enter choice (1-3): ").strip()

    return Character(name, "Warrior", 50, 8, 2, 5) if choice == "1" else \
           Character(name, "Mage", 40, 5, 20, 2) if choice == "2" else \
           Character(name, "Rogue", 45, 7, 5, 3)

def main():
    name = input("\n📝 Enter your character's name: ").strip()
    player = choose_character(name)

    while True:
        player.show_stats()
        explore(player)

if __name__ == "__main__":
    main()
