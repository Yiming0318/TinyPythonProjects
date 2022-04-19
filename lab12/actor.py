'''
Lab12 Starter Code
CS 5001, Fall 2021
Yiming Ge
This module contains a class representing an actor.
'''


class Actor:
    '''
        Class -- Actor
            Represents an actor.
        Attributes:
            firstname -- the Actor's first name
            lastname -- the Actor's last name
            shows -- a list of Shows the Actor has appeared in.
        Methods:
            appears_in -- Checks if the Actor has appeared in a Show.
    '''

    def __init__(self, firstname, lastname):
        '''
            Constructor -- Creates a new instance of Actor
            Parameters:
                self -- The current Actor object
                firstname -- the Actor's first name
                lastname -- the Actor's last name
        '''
        self.firstname = firstname
        self.lastname = lastname
        self.shows = []

    def appears_in(self, show):
        '''
            Method -- appears_in
                Checks if this Actor appeared in a given Show by searching in
                this Actor's shows list.
            Parameters:
                self -- The current Actor
                show -- A Show object
            Returns:
                True if the current Actor appeared in the given Show, False
                otherwise.
        '''
        # This can be simplified if we write __eq__ for Show
        for s in self.shows:
            if show.title == s.title:
                return True
        return False

    def __str__(self):
        return '{}{}'.format(self.firstname, self.lastname)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        if self.firstname == other.firstname and\
           self.lastname == other.lastname:
            return True
        else:
            return False

