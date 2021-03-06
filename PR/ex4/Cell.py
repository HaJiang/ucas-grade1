'''
struct for every cell
'''


class Cell:
    '''
    active_func : the active function
    '''

    def __init__(self, active_func, value):
        self.net_val = value
        self.active_val = 0
        self.active_func = active_func

    '''
    active the cell
    '''

    def active(self):
        self.active_val = self.active_func(self.net_val)
