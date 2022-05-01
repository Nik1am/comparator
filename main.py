import os
import colorama
colorama.init()
#CONSTS
STRING_LENGTH = 52
#CONSTS


print(""" ___ _____ ________  _________  ___  ______  ___ _____ ___________ ___ 
|  _/  __ \  _  |  \/  || ___ \/ _ \ | ___ \/ _ \_   _|  _  | ___ \_  |
| | | /  \/ | | | .  . || |_/ / /_\ \| |_/ / /_\ \| | | | | | |_/ / | |
| | | |   | | | | |\/| ||  __/|  _  ||    /|  _  || | | | | |    /  | |
| | | \__/\ \_/ / |  | || |   | | | || |\ \| | | || | \ \_/ / |\ \  | |
| |_ \____/\___/\_|  |_/\_|   \_| |_/\_| \_\_| |_/\_/  \___/\_| \_|_| |
|___|                                                             |___|
                                                                       
(type h for help)""")
def term():
    ti = input('$ ')
    if ti == 'h':
        print("""[h]: Help command
[i]: Enter 2 compared directories
[c]: Compare directories
[a]: Afrerpath""")
    
    elif ti == 'i':
        init()
    elif ti == 'c':
        print_compared_dirs(listed_dir_old,listed_dir_new)
    elif ti == 'a':
        init_atp()
    elif ti == 'f':
        compare_file()
    
    term()

def init():
    global dir_old 
    global listed_dir_old
    global dir_new 
    global listed_dir_new
    global in1
    global in2
    in1 = input('Old dir: ')
    in2 = input('New dir: ')
    atp = input('Afterpath: ')
    dir_old = in1+atp
    listed_dir_old = os.listdir(dir_old)
    dir_new = in2+atp
    listed_dir_new = os.listdir(dir_new)
    
def init_atp():
    global dir_old 
    global listed_dir_old
    global dir_new 
    global listed_dir_new
    atp = input('Afterpath: ')
    dir_old = in1+atp
    listed_dir_old = os.listdir(dir_old)
    dir_new = in2+atp
    listed_dir_new = os.listdir(dir_new)

def compare_file():
    offset_old = 0
    offset_new = 0
    name = input('File name: ')
    f1 = open(dir_old+name,'r').readlines()
    f2 = open(dir_new+name,'r').readlines()
    for string in range(0,max(len(f1),len(f2))):
        strnum = f'[{string:03d}]'
        old_elem = f1[string-offset_old]
        new_elem = f2[string-offset_new]
        
        try:
            file1_str = "{:>52}".format(old_elem)
        except:
            file1_str = ' '*STRING_LENGTH
        try:
            file2_str = "{:>52}".format(new_elem)
        except:
            file2_str = ' '*STRING_LENGTH
            
        if new_elem not in f1:
            print(colorama.Back.GREEN,strnum,' '*STRING_LENGTH,file2_str,colorama.Back.BLACK)
            offset_old = offset_old + 1
        elif old_elem not in f2:
            print(colorama.Back.RED , strnum,file1_str,' '*STRING_LENGTH,colorama.Back.BLACK)
            offset_new = offset_new + 1
        elif old_elem == new_elem:
            print(colorama.Back.BLACK ,strnum,file1_str,file2_str)

def print_compared_dirs(listed_dir_old,listed_dir_new):
    offset_old = 0
    offset_new = 0
    for element in range(0,max(len(listed_dir_old),len(listed_dir_new))):
        strnum = f'[{element:03d}]'
        old_elem = listed_dir_old[element-offset_old]
        new_elem = listed_dir_new[element-offset_new]
        try:
            str_from_old_dir = "{:>52}".format(old_elem)
        except:
            str_from_old_dir = ' '*STRING_LENGTH
        try:
            str_from_new_dir = "{:>52}".format(new_elem)
        except:
            str_from_new_dir = ' '*STRING_LENGTH
            
        if new_elem not in listed_dir_old:
            print(colorama.Back.GREEN,strnum,' '*STRING_LENGTH,str_from_new_dir,colorama.Back.BLACK)
            offset_old = offset_old + 1
        elif old_elem not in listed_dir_new:
            print(colorama.Back.RED , strnum,str_from_old_dir,' '*STRING_LENGTH,colorama.Back.BLACK)
            offset_new = offset_new + 1
        elif old_elem == new_elem:
            try:
                f1 = open(dir_old+old_elem,'rb').read()
                f1h = hash(f1)
                f1.close()
            except:
                pass
            try:
                f2 = open(dir_new+new_elem,'rb').read()
                f2h = hash(f2)
                f2.close()
            except:
                pass
            if f1h == f2h:
                print(colorama.Back.BLACK ,strnum,str_from_old_dir,str_from_new_dir ,'\033[39m')
            else:
                print(colorama.Back.YELLOW,strnum,str_from_old_dir,str_from_new_dir ,colorama.Back.BLACK)

term()