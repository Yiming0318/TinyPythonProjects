from actor import Actor
from show import Show
from channel import Channel


def show_starring(actor, channels):
    total_list = []
    for channel in channels:
        total_list.append(channel.get_shows_by_actor(actor))
    return total_list


def get_channel_info(show, channels):
    info_list = []
    for channel in channels:
        info_list.append(channel.channel_info_based_on_show(show))
    return info_list


def get_the_shows(day, channels):
    show_list = []
    for channel in channels:
        show_list.append(channel.get_schedule().get(day))
    return show_list

def main():
    actor1 = Actor("Actor", "1")
    actor2 = Actor("Actor", "2")
    actor3 = Actor("Actor", "3")
    show1 = Show("Monday Show", [actor1, actor2])
    show2 = Show("Tuesday Show", [actor1, actor2, actor3])
    show3 = Show("Friday Show", [actor2, actor3])
    channel1 = Channel("DEF", 42, [show1, show2])
    channel2 = Channel("XYZ", 31, [show2, show3])
    channels = [channel1, channel2]
    print(show_starring(actor1, channels))
    # channel info which contains Monday show
    print(get_channel_info(show1, channels))
    # channel1 monday schedule show
    print(channel1.get_schedule().get('Monday'))
    # get all shows on Monday
    print(get_the_shows('Monday', channels))
if __name__ == '__main__':
    main()