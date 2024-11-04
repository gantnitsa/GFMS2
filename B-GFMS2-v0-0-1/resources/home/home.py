class home:
    def __init__(self): pass
    def CMD(self, IN:str, DTSYS:tuple):
        if IN == 'Init':
            return([['Home sweet home'], '\'home\' initialised'])
        elif IN == '':
            return([['Home sweet home'], ''])
        else:
            return([['BRO', 'NO'], '\033[38;2;255;;m\'home\' doesn\'t do anything. Please do not give it a command\033[0m'])