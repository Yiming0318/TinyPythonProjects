'''
Lab12
CS 5001, Fall 2021
Yiming Ge
This module contains a class representing a TV show.
'''
# from actor import Actor

class Show:
    '''
        Class -- Show
            Represents a TV show.
        Attributes:
            title -- the show's title
            cast -- a list of actors appearing in the show
        Methods:
            cast_contains -- Checks if a particular Actor has been in the show.
    '''

    def __init__(self, title, cast):
        '''
            Constructor -- Creates a new instance of Show
            Parameters:
                self -- The current Show object
                title -- the show's title
                cast -- a list of actors appearing in the show
        '''
        self.title = title
        self.cast = cast

    def cast_contains(self, actor):
        '''
            Method -- cast_contains
                Checks if a given Actor is in this Show's cast.
            Parameters:
                self -- the current Show object.
                actor -- the Actor to search for.
            Returns:
                True if the Actor is in the cast, False otherwise.
        '''
        # This can be simplified if we write __eq__ for Actor
        for a in self.cast:
            if a == actor:
            # if a.firstname == actor.firstname and a.lastname == actor.lastname:
                return True
        return False

    def __str__(self):
        # actors = ','.join(self.cast)
        return '{} in {}'.format(self.cast, self.title)

    def __eq__(self, other):
        if type(self) != type(other):
            return False
        return self.cast == other.cast and self.title == other.title

# actor1 = Actor("Actor", "1")
# actor2 = Actor("Actor", "2")
# actor3 = Actor("Actor", "3")
# show1 = Show("Monday Show", [actor1, actor2])
# show2 = Show("Tuesday Show", [actor1, actor2, actor3])
# print(show1.cast_contains(actor3))
# # print(show1 == show2)
# # print(show1)
# # print(actor1)