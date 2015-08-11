class GameOverException(Exception):
    pass


class GameException(Exception):
    pass


class Item:
    def __init__(self, params):
        self.params = params

    def __getitem__(self, key):
        return self.params[key]

    def __setitem__(self, key, value):
        self.params[key] = value

    def __contains__(self, key):
        return key in self.params

    def __eq__(self, another_item):
        if isinstance(another_item, Item):
            return self["name"] == another_item["name"]
        elif isinstance(another_item, str):
            return self["name"] == another_item
        return False

    def __str__(self):
        return "Item: {name}".format(**self.params)


class World:
    locations = {}
    inventory = []

    @property
    def current_room(self):
        return self.locations[self.current_location]

    def _get_item(self, item_name, item_list):
        for item in item_list:
            if item == item_name:
                return item
        raise GameException("That item isn't here")

    def describe_location(self):
        if "on_look" in self.current_room:
            self.current_room["on_look"](self)
        else:
            print(self.current_room["description"])
        print()
        items = self.current_room["items"]
        for item in items:
            print(item["description"])
        exits = self.current_room["exits"]
        for exit in exits:
            print(exit["description"])

    def pick_up_item(self, item_name):
        items = self.current_room["items"]
        item = self._get_item(item_name, items)
        items.remove(item)
        return item

    def add_inventory(self, item):
        self.inventory.append(item)

    def move_to(self, direction):
        exits = self.current_room["exits"]
        for exit in exits:
            if direction in exit:
                self.current_location = exit[direction]
                return
        raise GameException("You can't go there!")


class CommandExecutor:
    def __init__(self, world):
        self.world = world

    def execute(self, command):
        parts = command.split()
        try:
            method = getattr(self, "command_" + parts[0])
            method(*parts[1:])
        except AttributeError:
            raise GameException("Unknown command")
        except TypeError:
            raise GameException("Wrong command format. Type 'help' to view the command format")

    def command_quit(self):
        """quit -> Quit the game"""
        raise GameOverException("Thanks for playing!")

    def command_help(self):
        """help -> Get help on available commands"""
        for method_name in dir(self):
            if method_name.startswith("command_"):
                method = getattr(self, method_name)
                print(method.__doc__)

    def command_look(self):
        """look -> Describe your current location"""
        self.world.describe_location()

    def command_get(self, object_name):
        """get <object_name> -> Pick up the object mentioned"""
        item = self.world.pick_up_item(object_name)
        self.world.add_inventory(item)
        print("OK")
        if "on_get" in item:
            item["on_get"](self.world)

    def command_inventory(self):
        """inventory -> Show items you are carrying"""
        print("You are carrying:")
        if len(self.world.inventory) > 0:
            print(" ".join([item["name"] for item in self.world.inventory]))
        else:
            print("Nothing")

    def command_go(self, direction):
        """go <direction> -> Go in the given direction"""
        self.world.move_to(direction)
        self.execute("look")

    def command_use(self, object_name):
        """use <object> -> Use the object in the current location"""
        if not object_name in self.world.inventory:
            raise GameException("You don't have that item!")
        item = self.world._get_item(object_name, self.world.inventory)
        if not "on_use" in item:
            raise GameException("You can't do that here")
        item["on_use"](self.world)


class Game:
    def __init__(self, world):
        self.world = world

    def run(self):
        print("-"*75)
        print("From ancient times, rumour exists of a treasure hidden under your house")
        print("Can you find it?")
        print("WELCOME TO ADVENTURE!")
        print("-"*75)
        print("Type 'help' to get started\n\n")
        executor = CommandExecutor(self.world)
        executor.execute("look")
        while True:
            try:
                command = input("\n> ")
                executor.execute(command.lower())
            except GameException as e:
                print(e)
