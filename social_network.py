class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
   class SocialNetwork:
    def __init__(self):
        self.people = {}  # key: person name, value: Person instance

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} already exists in the network!")

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people or person2_name not in self.people:
            missing = person1_name if person1_name not in self.people else person2_name
            print(f"Friendship not created. {missing} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        for name, person in self.people.items():
            friend_names = [f.name for f in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names)}")



network = SocialNetwork()

for name in ["Alex", "Jordan", "Morgan", "Taylor", "Casey", "Riley"]:
    network.add_person(name)

network.add_person("Alex")

network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Jordan", "Johnny")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

network.print_network()



"""
Design Memo:

Graphs are a perfect model for representing social networks because they naturally show people and their relationships.
Each person is a node and each friendship is an edge connecting them. This makes it super easy to wrap your head around when seeing who is friends with who.
Using a list or a tree wouldnt have worked as well because a list is just a line of items so it wouldnt have show the connections between people.
A tree forces a hierarchyu with parents and children whihc doesnt make sense for friendships because everyone is on the same level.
One thing that I noticed while building this is that adding friends was pretty straightforward and quick since you just update each persons list.
Printing the network is also pretty easy but if the network gets too huge it might take awhile longer.
The nice thing about using adjacency lists is that it doesnt waste memory. It reserves space for all possible connections even if most people arent friends.
In general this setip makes it easy to see relationships, add new people, and figure out connections. It's a practical way to model social network without overcomplicating things.
"""