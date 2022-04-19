from show import Show
class Channel:
    def __init__(self, name, number, shows_on_channel):
        self.name = name
        self.number = number
        self.shows_on_channel = shows_on_channel
    
    def get_shows_by_actor(self, actor):
        show_list = []
        for show in self.shows_on_channel:
            if show.cast_contains(actor):
                show_list.append(show.title)
        return show_list
    
    def channel_info_based_on_show(self, show):
        if show in self.shows_on_channel:
            show_names = []
            for a_show in self.shows_on_channel:
                show_names.append(a_show.title)
            return 'Channel name is {} number is {} contains {}'.format(self.name, self.number,','.join(show_names))
        return 'Channel {} does not contain {}'.format(self.name, show.title)
    
    def get_schedule(self):
        schedule = {}
        for show in self.shows_on_channel:
            day = show.title.split()[0]
            schedule[day] = show.title
        return schedule