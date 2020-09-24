import datetime

class Timer():

    def __init__(self):
        self.start_time = self.now()
        self.end_time = None
        self.elapse = None

    def now(self):
        return datetime.datetime.now()

    def elapse_time(self, unit='minute'):
        unit_list = ['minute', 'second', 'hours']
        if unit not in unit_list:
            raise ValueError('unit_list : {} '.format(unit_list))
        self.end_time = self.now()
        self.elapse = (self.end_time - self.start_time)

        if unit == 'second':
            return self.elapse.seconds
        elif unit == 'minute':
            return self.elapse.seconds / 60
        else:
            return self.elapse.seconds / 3600
