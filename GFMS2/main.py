#BASE_MODULES
import os, datetime

#pathing
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Plugin Importing
with open('resources\\PH', 'r') as FH:
    TAB_LIST = FH.read().split('\n')
SUB_LIST = [[]]
for i in TAB_LIST:
    exec(f'from resources import {i}')
    exec(f'SUB_LIST += [["{i}", {i}.{i}()]]')
del TAB_LIST

#fn


#basic mustknows
def TOP(): return("   ____   _____   __  __   ____    ____  ", "  / ___| |  ___| |  \/  | / ___|  |___ \ " + " "*87 + "\x1b[38;2;;255;mLAST REFRESH\x1b[0m", " | |  _  | |_    | |\/| | \___ \    __) |" + " "*88 + f'\x1b[38;2;;200;m{str(datetime.datetime.now())[8:10] + ' ' + ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC')[int(str(datetime.datetime.now())[5:7]) - 1] + ' ' + str(datetime.datetime.now())[0:4]}\x1b[0m', " | |_| | |  _|   | |  | |  ___) |  / __/ " + " "*94 + f'\x1b[38;2;;200;m{str(datetime.datetime.now())[11:16]}\x1b[0m', "  \____| |_|     |_|  |_| |____/  |_____|", f'\033[38;2;128;;128m{'▄'*140}\033[0m')

def DTSYS(): return(int(''.join(str(datetime.datetime.now())[0:10].split('-'))), int(''.join(str(datetime.datetime.now())[11:16].split(':')))) #System read [0]: date(YYYYMMDD)(len = 8), [1]: time(HHMM)(len = 4)

#int(''.join(str(os.get_terminal_size())[25:len(str(os.get_terminal_size()))][i] for i in range(len(str(os.get_terminal_size())[25:len(str(os.get_terminal_size()))])) if not ',' in str(os.get_terminal_size())[25:len(str(os.get_terminal_size()))][0:(i + 1)]))

#vars
CMD = '' #input controller
CUR_SUB = 'INIT' #indicator for the current subprocess running
#SUB_LIST The list of tabs including CUR_SUB
OUT = []

#main
while CMD != 'TERMINATE':
    print('\x1b[2J\x1b[H', end = '')
    if int(''.join(str(os.get_terminal_size())[25:len(str(os.get_terminal_size()))][i] for i in range(len(str(os.get_terminal_size())[25:len(str(os.get_terminal_size()))])) if not ',' in str(os.get_terminal_size())[25:len(str(os.get_terminal_size()))][0:(i + 1)])) < 140 and CUR_SUB != 'WIDTH_ERROR':
        print('\x1b[38;2;255;;mPLEASE RESIZE SCREEN WIDTH TO 140 CHARS\x1b[0m')
        CUR_SUB = 'WIDTH_ERROR'
    else:
        for i in TOP(): print(i)
        if CUR_SUB in ('WIDTH_ERROR', 'INIT'): CUR_SUB == 'NIL'
        if CMD.split(' ')[0] == 'SWITCH':
            if CMD != 'SWITCH' and len(CMD.split(' ')) == 2 and CMD.split(' ')[1] in [i[0] for i in SUB_LIST]:
                CUR_SUB == CMD.split(' ')[1]
                OUT = SUB_LIST[SUB_LIST.index(CUR_SUB)][1].CMD('INIT')
        elif CMD.split(' ')[0] == 'SCROLL':
            pass
        else:
            SCRO = SUB_LIST[SUB_LIST.index(CUR_SUB)][1].CMD(CMD)
    CMD = input('CMD: ')