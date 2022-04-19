from lightrail import is_valid_station, is_valid_trip, get_direction,\
            get_num_stops


def test_is_valid_station():
    assert(is_valid_station("Angle Lake"))
    assert(not is_valid_station("Bellingham"))
    assert(is_valid_station("SeaTac/Airport"))
    assert(is_valid_station("Northgate"))


def test_is_valid_trip():
    assert(not is_valid_trip("Angle Lake", "Angle Lake"))
    assert(is_valid_trip("Northgate", "Angle Lake"))
    assert(not is_valid_trip("Aloha Street", "Mercer Street"))


def test_get_direction():
    assert(get_direction("Northgate", "Angle Lake")
           == "Southbound")
    assert(get_direction("Angle Lake", "Northgate")
           == "Northbound")
    assert(get_direction("University Street", "University Street")
           == "No destination found")


def test_get_num_stops():
    assert(get_num_stops("Northgate", "Angle Lake") == 18)
    assert(get_num_stops("Angle Lake", "University of Washington") == 15)
    assert(get_num_stops("University Street", "University Street") == 0)
    assert(get_num_stops("University Street", "Tacoma") == 0)
