class Seat:
    """
    Class defined as "Seat".
    """
    def __init__(self, free: bool = True, occupant: str = None):
        """
        Function to initialize the argument of the Class "Seat".

        :param free: A Bool value that = True.
        :param occupant: An str value that = None.
        """

        self.free = free
        self.occupant = occupant

    def __str__(self):
        """
        Function string.

        return: "A free spot" if free = True.
        or
        return: "{Value of occupant} is sitting there".
        """

        if self.free == True:
            return "A free spot"
        else:
            return "{self.occupant} is sitting there".format(self=self)

    def set_occupant(self, name: str):
        """
        Function to assign a name to a sit if it's free.

        :name: An str who can be assign to occupant if the result is True.
        """

        if self.free == True:
            self.occupant = name
            self.free = False

    def remove_occupant(self):
        """
        Function to remove a name from a seat.

        :return:"{name} was sitting here".
        """

        self.free = True
        print(f'{self.occupant} was sitting here')
        self.occupant = None


# Defining and initiating class Table

class Table():
    """
    Class defined as "Table"
    """

    def __init__(self, capacity: int = 4):
        """
        Function to initialize the parameters of the Class "Table".

        :capacity: An int that define the number of seat allowed by table and add the number of "seat" to the table.
        """

        self.capacity = capacity
        self.seats = []
        for i in range(capacity):
            self.seats.append(Seat())

    def has_free_spot(self):
        """
        Function to check if each seat for a table, is free or not.

        :return: True if the seat is free.
        """

        for seat in self.seats:
            if seat.free:
                print(True)
                break

    def left_capacity(self):
        """
        Function with the free spot left in a list, to know the number of free seat left.

        :return: An int, who is the number of seat not assigned yet or telling us "last spot remaining" if int = 1 or "no more free spots" if int = 0 .
        """

        free_spot_list = []
        for seat in self.seats:
            if seat.free == True:
                free_spot_list.append(seat)

        if len(free_spot_list) == 1:
            print(f'{len(free_spot_list)} last spot remaining')
            return len(free_spot_list)
        elif len(free_spot_list) > 1:
            print(f'{len(free_spot_list)} spots remaining')
            return len(free_spot_list)
        else:
            print('No more free spots')
            return 0

    def assign_seat(self, name: str = None):
        """
        Function that will had name to the free seats.

        :return: put name in occupant if seat = free or pass if free = False or tell us "No more free spots" if there is no seat left.
        
        """

        for index, seat in enumerate(self.seats):
            if seat.free == True:
                seat.set_occupant(name)
                break
            elif seat.free == False:
                pass
            else:
                print('No more free spots')
