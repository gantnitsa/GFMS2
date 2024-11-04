#BASE_MODULES
import os, datetime

#pathing
os.chdir(os.path.dirname(os.path.abspath(__file__)) + '\\resources')

#Plugin Importing
with open('Plugins', 'r') as FH:
    TAB_LIST = FH.read().split('\n')
SUB_LIST = []
for i in TAB_LIST:
    exec(f'from resources.{i} import {i}')
    exec(f'SUB_LIST += [["{i}", {i}.{i}()]]')
del TAB_LIST

#Cmd config
with open('Config', 'r') as FH:
    commands = FH.read().split('\n')

#fn
def assemble():
    POUT = []
    for i in OUT[0]:
        for k in i:
            POUT += [k]
        POUT += ['\n']
    for i in range(30): POUT += ['\n']
    PPOUT = [f' Current Tab: {CUR_SUB}', f'\033[38;2;128;;128m{'▄'*100}\033[0m', ' ']
    while len(PPOUT) < 33:
        if POUT[0] == '\n':
            PPOUT.append(' ')
        elif len(PPOUT[len(PPOUT) - 1]) == 100:
            PPOUT.append(' ' + POUT[0])
        else:
            PPOUT[len(PPOUT) - 1] += POUT[0]
        POUT = POUT[1:len(POUT)]
    del POUT
    PTABS = ([f'Tab Page: {SUB_PAGE}{' '*39}'[0:39] + '\033[38;2;128;;128m█\033[0m', f'\033[38;2;128;;128m{'▄'*39}\033[0m\033[38;2;128;;128m█\033[0m'] + [(str(i + 1) + '. ' + SUB_LIST[i][0] + ' '*39)[0:39] + '\033[38;2;128;;128m█\033[0m' for i in range(len(SUB_LIST))][slice((SUB_PAGE - 1)*30, SUB_PAGE*30)] + [f'{' '*39}\033[38;2;128;;128m█\033[0m' for i in range(32)])[0:32]
    return([PTABS[i] + PPOUT[i] for i in range(32)] + [f'\033[38;2;128;;128m{'▄'*39}█{'▄'*100}\033[0m', f'\033[38;2;;200;mPREV_CMD: {CMD}\033[0m', OUT[1]])

#Sys info
def DTSYS(): return(int(''.join(str(datetime.datetime.now())[0:10].split('-'))), int(''.join(str(datetime.datetime.now())[11:16].split(':')))) #System read [0]: date(YYYYMMDD)(len = 8), [1]: time(HHMM)(len = 4)

#vars
CMD = '' #input controller
CUR_SUB = 'init' #indicator for the current subprocess running
#SUB_LIST The list of tabs including CUR_SUB
SUB_PAGE = 1
OUT = [[], ''] #plugin output

#main
while CMD != commands[0]:
    os.system('cls')
    if int(''.join(str(os.get_terminal_size())[25:len(str(os.get_terminal_size()))][i] for i in range(len(str(os.get_terminal_size())[25:len(str(os.get_terminal_size()))])) if not ',' in str(os.get_terminal_size())[25:len(str(os.get_terminal_size()))][0:(i + 1)])) < 140 and CUR_SUB != 'WIDTH_ERROR':
        print('\x1b[38;2;255;;mPlease resize the screen to a width of 140 characters or above\x1b[0m')
        CUR_SUB = 'width_error'
    else:
        for i in ("   ____   _____   __  __   ____    ____  ", "  / ___| |  ___| |  \\/  | / ___|  |___ \\ " + " "*87 + "\x1b[38;2;;255;mLAST REFRESH\x1b[0m", " | |  _  | |_    | |\\/| | \\___ \\    __) |" + " "*88 + f'\x1b[38;2;;200;m{str(datetime.datetime.now())[8:10] + ' ' + ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC')[int(str(datetime.datetime.now())[5:7]) - 1] + ' ' + str(datetime.datetime.now())[0:4]}\x1b[0m', " | |_| | |  _|   | |  | |  ___) |  / __/ " + " "*94 + f'\x1b[38;2;;200;m{str(datetime.datetime.now())[11:16]}\x1b[0m', "  \\____| |_|     |_|  |_| |____/  |_____|", f'\033[38;2;128;;128m{'▄'*140}\033[0m'): print(i)
        if CUR_SUB in ('width_error', 'init'):
            CUR_SUB = 'home'
            OUT = [[], '']
        if CMD.split(' ')[0] == commands[2]:
            if CMD != commands[2] and len(CMD.split(' ')) == 2 and CMD.split(' ')[1] in [i[0] for i in SUB_LIST]:
                CUR_SUB = CMD.split(' ')[1]
                OUT = SUB_LIST[list(i[0] for i in SUB_LIST).index(CUR_SUB)][1].CMD('Init', DTSYS())
            else:
                OUT[1] = '\033[38;2;255;;mInvalid\033[0m'
        elif CMD.split(' ')[0] == commands[1]:
            if len(CMD.split(' ')) == 2:
                try:
                    if int(CMD.split(' ')[1]) > 0:
                        SUB_PAGE = int(CMD.split(' ')[1])
                        OUT[1] = f'Scrolled to page {SUB_PAGE}'
                    else:
                        OUT[1] = '\033[38;2;255;;mNumber outside range\033[0m'
                except:
                    SUB_PAGE = 1
                    OUT[1] = '\033[38;2;255;;mNot a number\033[0m'
            else:
                OUT[1] = '\033[38;2;255;;mInvalid\033[0m'
        else:
            OUT = SUB_LIST[list(i[0] for i in SUB_LIST).index(CUR_SUB)][1].CMD(CMD, DTSYS())
        for j in assemble(): print(j)
    CMD = input('CMD: ')