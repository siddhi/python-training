from .adventure import Game, GameOverException
from .worlds import world


if __name__ == "__main__":
    try:
        Game(world).run()
    except GameOverException as e:
        print(e)
