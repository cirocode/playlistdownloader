#!python3
# Maineira ezekuta -
# 1. Loke cmd
# 2. cd ba folder ou pasta ne'ebe file iha ba
# 3. ezekuta - python ytdown.py
# Hein skrip komesa lao


import os
import subprocess
from pytube import YouTube
import random
import requests
import re
import string

#funsaun imp


def foldertitle(url):

    try:
        res = requests.get(url)
    except:
        print('lai koneksaun internet')
        return False

    plain_text = res.text

    if 'list=' in url:
        eq = url.rfind('=') + 1
        cPL = url[eq:]

    else:
        print('Incorrect attempt.')
        return False

    return cPL



def link_snatcher(url):
    our_links = []
    try:
        res = requests.get(url)
    except:
        print('lai koneksaun internet')
        return False

    plain_text = res.text

    if 'list=' in url:
        eq = url.rfind('=') + 1
        cPL = url[eq:]
    else:
        print('Playlist lalos.')
        return False

    tmp_mat = re.compile(r'watch\?v=\S+?list=' + cPL)
    mat = re.findall(tmp_mat, plain_text)

    for m in mat:
        new_m = m.replace('&amp;', '&')
        work_m = 'https://youtube.com/' + new_m
        # print(work_m)
        if work_m not in our_links:
            our_links.append(work_m)

    return our_links


BASE_DIR = os.getcwd()

print(' Bemvindo my Playlist Downloader - https://github.com/cirocode')

url = str(input("\nspesifiku playlist URL\n"))

print('\nHili entre tipu kualidade video - TYPE 360P OR 720P\n')
user_res = str(input()).lower()


print('...Ita hili ' + user_res + ' kualidade video\n.')

our_links = link_snatcher(url)

os.chdir(BASE_DIR)

new_folder_name = foldertitle(url)
print(new_folder_name[:7])

try:
    os.mkdir(new_folder_name[:7])
except:
    print('pasta nee existe ona')
os.chdir(new_folder_name[:7])
SAVEPATH = os.getcwd()
print(f'\n fali sei guarda {SAVEPATH}')

x=[]
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        pathh = os.path.join(root, name)

        
        if os.path.getsize(pathh) < 1:
            os.remove(pathh)
        else:
            x.append(str(name))


print('\nkria hela koneksaun . . .\n')


print()

for link in our_links:
    try:
        yt = YouTube(link)
        main_title = yt.title
        main_title = main_title + '.mp4'
        main_title = main_title.replace('|', '')
        
    except:
        print('koneksaun ..problema hela hare didiak no koko fila fali')
        break

    
    if main_title not in x:

        
        if user_res == '360p' or user_res == '720p':
            vid = yt.streams.filter(progressive=True, file_extension='mp4', res=user_res).first()
            print('Hein oituan download hela. . . ' + vid.default_filename + ' and its file size -> ' + str(round(vid.filesize / (1024 * 1024), 2)) + ' MB.')
            vid.download(SAVEPATH)
            print('Video Download ona')
        else:
            print('Iha problema ruma..favor ezekuta fila fali script ne')


    else:
        print(f'\n skipping "{main_title}" video \n')


print(' download akaba')
print(f'\n video hotu rai ona --> {SAVEPATH}')
