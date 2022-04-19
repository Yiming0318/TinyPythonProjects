'''
Yiming Ge
CS 5001, Fall 2021
HW05 -- Problem 3
This a module containing functions for getting basic directions
on the Seattle Link light rail.
'''

LINK_STATIONS = ("Northgate", "Roosevelt", "U District",
                 "University of Washington", "Capitol Hill", "Westlake",
                 "University Street", "Pioneer Square",
                 "International District/Chinatown", "Stadium", "SODO",
                 "Beacon Hill", "Mount Baker", "Columbia City", "Othello",
                 "Rainier Beach", "Tukwila International Boulevard",
                 "SeaTac/Airport", "Angle Lake")


def is_valid_station(station):
    '''
        Function -- is_valid_station
            Checks if a given string is a valid Seattle light rail station.
            Provided station must match a station name exactly. For example,
            "mount baker" would not be valid because the case doesn't match.
        Parameter:
            station -- The string to check
        Returns:
            True if a given string is a valid Seattle light rail station
            name, False otherwise.
    '''
    return station in LINK_STATIONS


def is_valid_trip(start, end):
    '''
        Function -- is_valid_trip
            Checks if the given trip is valid that both stations exist and
            are not the same station.
        Parameters:
            start - The starting station name.
            end - The ending station name.
        Returns:
            True if both stations are valid and the two stations are not the
            same, otherwise False
    '''
    return is_valid_station(start) and is_valid_station(end) and start != end


def get_direction(start, end):
    '''
        Function -- get_direction
            Given start and end station names, determines if the direction is
            Northbound or Southbound.
        Parameters:
            start - The starting station name
            end - The ending station name.
        Returns:
            "Northbound" if the end station is north of the start station, or
            "Southbound" if the end station is south of the start station. If
            either station is invalid, or start and end stations are the same,
            return "No destination found".
    '''
    NORTH = "Northbound"
    SOUTH = "Southbound"
    NO_DESTINATION = "No destination found"
    if is_valid_trip(start, end):
        if LINK_STATIONS.index(start) > LINK_STATIONS.index(end):
            return NORTH
        elif LINK_STATIONS.index(start) < LINK_STATIONS.index(end):
            return SOUTH
    return NO_DESTINATION


def get_num_stops(start, end):
    '''
        Function -- get_num_stops
            Calculates the number of stops from start to end.
        Parameters:
            start - The starting station name
            end - The ending station name.
        Returns:
            The number of stops from start to end. If either station is invalid
            or both stations are the same, return 0.
    '''
    if is_valid_trip(start, end):
        return abs(LINK_STATIONS.index(start) - LINK_STATIONS.index(end))
    return 0
