#This code draws information from its neighbouring file, Berry_info.txt, and returns it to the user on the command of 'goober me timbers'
class TMAS: #Within the file, define an eponymous class - this is where your command parser will rest as a handler for the 'main.py'
    def __init__(self): #Add an __init__ for your class. All functions will be carried out as *handler*.*command*
        self.happy = 'happiness' #define your variables as self.*something* so the system does not mess up
    def CMD(self, IN:str, DTSYS:tuple): #Add a CMD function exactly as such. All system commands will be received here.
#The variables of CMD:
#1. IN: the command from the system
#2. DTSYS: the system datetime - the first element in such will be int(YYYYMMDD) and the second will be int(HHMM)
        if IN == 'Init': #Leave the three system commands and 'Init' command - the 'Init' is used for initialisation.
            return([['Berrytown, hell yeah!'], '\'TMAS\' initialised']) #Return what response you want on the screen as the first element, and then the second as the console response.
        if IN == 'goober me timbers':
            return([Berry(), 'Have a nice day!'])
        else:
            return([[], ''])
def Berry(): #Internal functions are stored outside of the class
    with open('TMAS\Berry_info.txt', 'r') as FH: #Remember, the path of the 'main.py' is in GFMS2\resources.
        return(FH.read().split('\n'))