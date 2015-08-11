from .adventure import World, Item, GameException, GameOverException


def load_flashlight(self):
    if "batteries" in self.inventory and "flashlight" in self.inventory:
        print("You load the batteries into the flashlight")
        batteries = self._get_item("batteries", self.inventory)
        self.inventory.remove(batteries)
        flashlight = self._get_item("flashlight", self.inventory)
        flashlight["loaded"] = True


def tie_rope(self):
    if self.current_location != "well":
        raise GameException("You can't do that here")
    else:
        print("You tie the rope to the well. You can now go 'down' into the well")
        exits = self.current_room["exits"]
        exits.append({"down": "wellbottom",
                      "description": "A long rope leads 'down' into the well"})
        self.inventory.remove("rope")


def see_well(self):
    print("It is pitch dark here")
    if "flashlight" in self.inventory:
        flashlight = self._get_item("flashlight", self.inventory)
        if flashlight["loaded"]:
            print("Using the flashlight you make out a small tunnel")
            new_exit = {"north": "tunnel", "description": "There is a small tunnel heading 'north'"}
            exits = self.current_room["exits"]
            if not exit in exits:
                exits.append(new_exit)


def get_treasure(self):
    raise GameOverException("Contratulations! You found the ancient treasure!")


world = World()
world.load_flashlight = load_flashlight
world.locations = {
    "home": {
        "description": "You are at your home. It is a nice place, although a little messy",
        "items": [Item({"name": "batteries",
                        "description": "There are some batteries here",
                        "on_get": load_flashlight})],
        "exits": [{"north": "garden",
                   "description": "The door to the 'north' goes into the garden"},
                  {"up": "storeroom",
                   "description": "The stairs going 'up' lead to the store room"}]
    },
    "garden": {
        "description": "You are at the garden outside your home. You feel the warmth of the rising sun as insects buzz about",
        "items": [],
        "exits": [{"east": "well",
                   "description": "To the 'east' is a small well"},
                  {"south": "home",
                   "description": "The way 'south' leads into the home"},
                  {"west": "workshop",
                   "description": "Your carpentry workshop is to the 'west'"}]
    },
    "storeroom": {
        "description": "It has been years since you cleaned this place. The store room is full of junk",
        "items": [Item({"name": "flashlight",
                        "description": "There is a flashlight without batteries here",
                        "loaded": False,
                        "on_get": load_flashlight})],
        "exits": [{"down": "home",
                   "description": "Stairs lead 'down' into the home"}]
    },
    "well": {
        "description": "There is a well here. It seems to lead down forever",
        "items": [],
        "exits": [{"west": "garden",
                   "description": "You can see the garden to the 'west'"}]
    },
    "workshop": {
        "description": "There is the smell of sawdust here.",
        "items": [Item({"name": "rope",
                        "description": "A long piece of rope lies here",
                        "on_use": tie_rope})],
        "exits": [{"east": "garden",
                   "description": "You can see the garden to the 'east'"}]
    },
    "wellbottom": {
        "on_look": see_well,
        "items": [],
        "exits": [{"up": "well",
                   "description": "A rope leads back 'up' the well"}]
    },
    "tunnel": {
        "description": "You are in a small underground room",
        "items": [Item({"name": "chest",
                        "description": "A treasure chest lies here",
                        "on_get": get_treasure})],
        "exits": [{"south": "wellbottom",
                   "description": "A dim tunnel goes 'south'"}]
    }
}
world.current_location = "home"
