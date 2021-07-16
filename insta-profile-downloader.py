# import required modules
import instaloader
from PIL import *
import os,time,sys,platform
from colorama import Fore,init
init()
def clear():
    if platform.uname()[0] == "Linux" :
        os.system("clear")
    else:
        os.system("cls")
#banner
def banner():
    print(Fore.RED+'''
    XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
    XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
    XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
    XX   MMMMMy''                                                    ''yMMMMM   XX
    XX   MMMy'                                                          'yMMM   XX
    XX   Mh'                                                              'hM   XX
    XX   -                                                                  -   XX
    XX                                                                          XX
    XX   ::                                                                ::   XX
    XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
    XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
    XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
    XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
    XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
    XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
    XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
    XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
    XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
    XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX
    XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
    XX                                oo      oo                                XX
    XX           oM                 oo          oo                 Mo           XX
    XX         oMMo                M              M                oMMo         XX
    XX       +MMMM                 s              s                 MMMM+       XX
    XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
    XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
    XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
    XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
    XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
    XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
    XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
    XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
    XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
    XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
    XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
    XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
    XX   MMMMMMMM-                                                  -MMMMMMMM   XX
    XX   MMMMMMMMM                                                  MMMMMMMMM   XX
    XX   MMMMMMMMMy                                                yMMMMMMMMM   XX
    XX   MMMMMMMMMMy.                                            .yMMMMMMMMMM   XX
    XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
    XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
    XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
    XX   MMMMMMMMMMMMMMMMMMss.           ....           .ssMMMMMMMMMMMMMMMMMM   XX
    XX   MMMMMMMMMMMMMMMMMMMMNo         oNNNNo         oNMMMMMMMMMMMMMMMMMMMM   XX
    ''')
time.sleep(0.1)
print(Fore.GREEN+('CODED BY ARIIAN=)'))

print(Fore.GREEN+'CODED BY ARIIAN')
time.sleep(0.1)
def liststart():
    print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"1"+Fore.CYAN+"] "+Fore.RED+" Start ")
    time.sleep(0.1)
    print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"2"+Fore.CYAN+"] "+Fore.RED+" Developer ")
    time.sleep(0.1)
    print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"3"+Fore.CYAN+"] "+Fore.RED+" Exit \n")
    

def devloper():
    try:
        print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"1"+Fore.CYAN+"]  "+Fore.RED+" instagram : "+Fore.LIGHTCYAN_EX+"@arii.iann")
        time.sleep(0.1)
        print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"1"+Fore.CYAN+"]  "+Fore.RED+" github : "+Fore.LIGHTCYAN_EX+"https://github.com/ariian")
        time.sleep(0.1)
        print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"2"+Fore.CYAN+"]  "+Fore.RED+" Developer : "+Fore.LIGHTCYAN_EX+"arian")
        time.sleep(0.1)
        print(Fore.CYAN+"  ["+Fore.LIGHTCYAN_EX+"3"+Fore.CYAN+"]  "+Fore.RED+" telegram: "+Fore.LIGHTCYAN_EX+"https://t.me/a0_0in")
        
        try:
            input(Fore.CYAN+"\n   Back To Menu (Press Enter...) ")
        except:
            sys.exit()
    except KeyboardInterrupt:
        sys.exit()
def username():
    # Create instance
    loader = instaloader.Instaloader()
    # get username 
    user = input(Fore.GREEN+"ENTER THE USERNAME(EX:cristiano): ")
    time.sleep(0.1)
    # download profie
    loader.download_profile(user, profile_pic_only = True)
    # get list of image from folder
    img = [x for x in os.listdir(f'{os.getcwd()}/{user}') if x.endswith('jpg')]
    # read image from list
    img = Image.open(f'{os.getcwd()}/{user}/{img[0]}')
    # Display image
    img.show()
def main():
  try:
        clear()
        banner()
        liststart()
        start = input(Fore.LIGHTCYAN_EX+"  C://INSTAGRAM profile downloader=> "+Fore.RED)
        if start == '1':
            try:
                clear()
                banner()
                username()
            except KeyboardInterrupt:
                clear()
                banner()
                sys.exit()
        elif start == '2':
            try:
                clear()
                banner()
                devloper()
            except KeyboardInterrupt:
                clear()
                banner()
                sys.exit()
        elif start == '3':
            clear()
            print(Fore.RED+"Century Breaker ;)"+Fore.WHITE)
            sys.exit()
        elif start == '':
            input(Fore.RED+'\n    Enter Data |: ')
            main()
  except KeyboardInterrupt:
            clear()
            banner()
            sys.exit()

while True:
    main()                
