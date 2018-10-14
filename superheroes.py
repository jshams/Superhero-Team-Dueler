import random

class Hero:
    def __init__(self, name, health = 100):
        self.abilities = list()
        self.name = name

        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0
    def add_ability(self, ability):
        self.abilities.append(ability)
    def attack(self):
        if len(self.abilities) == 0:
            return 0
        else:
            return sum([a.attack() for a in self.abilities])
    def defend(self):
        if self.health == 0:
            return 0
        return sum([a.defend() for a in self.armors])
    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the
        hero's health.

        If the hero dies update number of deaths.
        """
        self.health -= damage_amt
        if self.health <= 0:
            self.deaths += 1

    def add_kill(self, num_kills):
        self.kills += num_kills
        """
        This method should add the number of kills to self.kills
        """




class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = attack_strength
    def attack(self):
        return randInt(self.attack_strength // 2, self.attack_strength)
    def update_attack(self, updated_attack_strength):
        self.attackStrength = updated_attack_strength

class Weapon(Ability):
    def attack(self):
        return randInt(0, self.attack_strength())
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """

class Team:
    def init(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = []

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(self.Hero)

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        if self.name in self.heroes:
            z = index(self.name)
            self.heroes.pop(z)
        else:
            return 0

    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """
        if self.name in self.heroes:
            return self.name
        else:
            return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        print(self.heroes)

    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on each hero with the number of kills made.
        """
        attack_strength = sum([hero.attack() for hero in self.heroes])
        kills = other_team.defend(attack_strength)


    def defend(self, damage_amt):
        defend_strength = sum([hero.defend() for hero in self.heroes])
        if defend_strength < damage_amt:
            excess_damage = damage_amt - defend_strength
            return self.deal_damage(excess_damage)
        return 0
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack.
        """

    def deal_damage(self, damage):
        for hero in self.heroes hero.health -= int(damage/len(self.heroes))
        for hero in self.heroes:
            if hero.health <= 0:
                update_kills()


        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """

    def revive_heroes(self, health = 100):
        for hero in self.heroes:
            hero.health = 100
        """
        This method should reset all heroes health to their
        original starting value.
        """

    def stats(self):
        print("kills:deaths = " + str(self.kills) + ":" + str(self.deaths))

        """
        This method should print the ratio of kills/deaths for each member of the team to the screen.

        This data must be output to the terminal.
        """

    def update_kills(self):
        for hero in self.heroes hero.kills +=1

        """
        This method should update each hero when there is a team kill.
        """

class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense

    def defend(self):
        return randInt(0, self.defense)
        """
        Return a random value between 0 and the
        initialized defend strength.
        """

class Arena:
    def __init__(self):
        """
        Declare variables
        """
        self.team_one = self.build_team_one()
        self.team_two = self.build_team_two()

    def build_team(self):
        team_name = input("Enter your team's name: ")
        newTeam = Team(team_name)
        continue_adding = True
        while continue_adding == True:
            hero = Hero(input("Enter your hero's name: "))

    def add_abilities(self, addition, hero):
        abilities = list()
        if self.yesNo("Add " + addition + " to " + hero + "? (y/n): "):
            continue_request = True
            

    def yesNo (self, prompt):
        inp = input(prompt)
        if inp in "YyNn":
            if inp in "Yy":
                return True
            else:
                return False
        else:
            print("Invalid input")
            return self.yesNo(prompt)

    def build_team_one(self):




        """
        This method should allow a user to build team one.
        """

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """

    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """

    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
