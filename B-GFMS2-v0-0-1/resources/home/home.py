class home:
    def __init__(self): pass
    def CMD(self, IN:str, DTSYS:tuple):
        if IN == '':
            return([[], '\'HOME\' initialised'])
        else:
            return([[], '\033[38;2;255;;m\'HOME\' doesn\'t do anything. Please do not give it a command\033[0m'])