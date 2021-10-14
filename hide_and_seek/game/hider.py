import random

class Hider:
    """A code template for our hider. The responsibility of this class of
    objects is to watch the seeker and give hints.
    
    Stereotype:
        Information Holder

    Attributes:
        location (integer): The location of the hider (1-1000).
        distance (list): The distance from the seeker.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Hider): An instance of Hider.
        """
        self.location = random.randint(1, 1000)
        self.distance = [0, 0]


    def watch(self, location):
        """Keeps track of how far away the seeker is by calculating the difference
        between their locations. The distance is appended to the corresponding attribute for later use.

        Args:
            self (Hider): An instance of Hider.
            location (number): An whole number that is passed internally
        """

        distance = abs(self.location - location)
        self.distance.append(distance)


    def get_hint(self):
        """Returns a hint that depends on whether or not the seeker has moved
        closer or farther away. This is determined by inspecting the last two distances contained
        in the distance attribute.

        Args:
            self (Hider): An instance of Hider.
        
        Returns:
            string: A response for the seeker.
        """
        
        if self.distance[-1] == 0:
            response = "\nº__º You found me!"
        elif self.distance[-1] <= self.distance[-2]:
            response = "*__* Getting warmer!"
        elif self.distance[-1] >= self.distance[-2]:
            response = "`__´ Getting colder!"
        return response