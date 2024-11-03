class home:
    def __init__(self): pass
    def CMD(self, IN:str, DTSYS:tuple):
        if IN == '':
            return([[], '\'home\' initialised'])
        else:
            return([[], '\033[38;2;255;;m\'home\' doesn\'t do anything. Please do not give it a command\033[0m'])