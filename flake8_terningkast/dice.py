import os

base_path = os.path.dirname(os.path.realpath(__file__))+"/images/"


def dice1():
    """Catimg dice with 1."""
    path_dice1 = base_path + "terningkast1.png"
    os.system(f"catimg -w 80 {path_dice1}")  # noqa: B605, B607


def dice2():
    """Catimg dice with 2."""
    path_dice2 = base_path + "terningkast2.png"
    os.system(f"catimg -w 80 {path_dice2}")  # noqa: B605, B607


def dice3():
    """Catimg dice with 3."""
    path_dice3 = base_path + "terningkast3.png"
    os.system(f"catimg -w 80 {path_dice3}")  # noqa: B605, B607


def dice4():
    """Catimg dice with 4."""
    path_dice4 = base_path + "terningkast4.png"
    os.system(f"catimg -w 80 {path_dice4}")  # noqa: B605, B607


def dice5():
    """Catimg dice with 5."""
    path_dice5 = base_path + "terningkast5.png"
    os.system(f"catimg -w 80 {path_dice5}")  # noqa: B605, B607


def dice6():
    """Catimg dice with 6."""
    path_dice6 = base_path + "terningkast6.png"
    os.system(f"catimg -w 80 {path_dice6}")  # noqa: B605, B607
