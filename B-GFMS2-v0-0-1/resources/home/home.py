from random import randint
import os
class home:
    def __init__(self): pass
    def CMD(self, IN:str, DTSYS:tuple):
        return([['Home sweet home', '', 'Fact of the second:', facto(), '', 'Here\'s a house', '° , ° ˚___Π_____*☽*˚ ,', '✩ ˚˛˚*/______/__\\。✩˚ ˚', '˚ ˛˚˛｜ 田田｜門｜ ˚ ˚', '\' ̛ ̛ \'\' \'\' \'\' ̛ ̛ \'\' \'\' \'\'', '', 'Command Help:', commands(0) + ': ends the program', commands(1) + ': scrolls to specified page', commands(2) + ': switches tabs to specified program'], '\'home\' refreshed. Enjoy your new fact!'])
def facto():
    with open('home\\Facts.txt') as FH:
        i = FH.read().split('\n')
        if i != ['']:
            return(i[randint(0,len(i) - 1)])
        else:
            return('No facts available. Go to "' + os.path.dirname(os.path.abspath(__file__)) + '\\Facts.txt" cahnge this fact.')
def commands(j):
    with open('Config') as FH:
        return(list(i.split(' ')[0] for i in FH.read().split('\n'))[j])