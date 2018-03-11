import os

base_path = os.path.dirname(os.path.realpath(__file__))+"/images/"


def dice(value):
    """Catimg correct dice."""
    path_dice = f"{base_path}terningkast{value}.png"
    os.system(f"catimg -w 80 {path_dice}")  # noqa: B605, B607
