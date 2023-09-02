import os
from shutil import  move
from pathlib import Path
import platform

if platform.system() == 'Linux':
    root_dir =  str(Path.home()) + '\Downloads'
    video_dir = str(Path.home()) + '/Videos'
    pic_dir = str(Path.home()) + '/Pictures'
    doc_dir = str(Path.home()) + '/Documents'
    app_dir = str(Path.home()) + '/Apps'
    other_dir = str(Path.home()) + '/Others'
    sub_dir = str(Path.home()) + '/Videos/Subtitle'
    music_dir = str(Path.home()) + '/Music'
    zip_dir = str(Path.home()) + '/Zip'
else:
    root_dir =  str(Path.home()) + '\Downloads'
    video_dir = str(Path.home()) + '\Videos'
    pic_dir = str(Path.home()) + '\Pictures'
    doc_dir = str(Path.home()) + '\Documents'
    app_dir = str(Path.home()) + '\Apps'
    other_dir = str(Path.home()) + '\Others'
    sub_dir = str(Path.home()) + '\Videos\Subtitle'
    music_dir = str(Path.home()) + '\Music'
    zip_dir = str(Path.home()) + '\CompressedFiles'

for folder in [video_dir,pic_dir,doc_dir,app_dir,other_dir,sub_dir,music_dir,zip_dir]:
    if not os.path.exists(folder):
        print(f'{folder} does not exist, creating folder...\n')
        os.mkdir(folder)

vid = ('.mp4','.mkv','.mov','.webm','.MP4')
pic = ('.jpg','.jpeg','.png','.svg','.gif','.tif','.tiff')
doc = ('.docx','.doc','.txt','.pdf','.xls','.ppt','.xlsx','.pptx','.html')
app = ('.exe','.dmg','.pkg')
srt = ('.srt')
aud = ('.mp3','.aud','.wav','.wax','.m4a','.aac')
comp = ('.zip','.7z','.zipx','.rar','.tar')

files = []

for f in os.listdir(root_dir):
    if not f.startswith('.') and not f.__eq__(__file__):
        files.append(f)
vidLen = 0
picLen = 0
docLen = 0
appLen = 0
srtLen = 0
audLen = 0
compLen = 0
otherLen = 0
for file in files:
    
    if file.endswith(vid):
        vidLen+=1
        move(root_dir+'\\'+ file,video_dir)
    elif file.endswith(pic):
        picLen += 1
        move(root_dir+'\\'+ file,pic_dir)
        
    elif file.endswith(doc):
        docLen += 1
        move(root_dir+'\\'+ file,doc_dir)
    elif file.endswith(app):
        appLen += 1
        move(root_dir+'\\'+ file,app_dir)
    elif file.endswith(srt):
        srtLen += 1
        move(root_dir+'\\'+ file,sub_dir)
    elif file.endswith(aud):
        audLen += 1
        move(root_dir+'\\'+ file,music_dir)
    elif file.endswith(comp):
        compLen += 1
        move(root_dir+'\\'+ file,zip_dir)
    else:
        otherLen += 1
        move(root_dir+'\\'+file,other_dir)
if not vidLen == 0:
    print('Successfully moved '+str(vidLen)+' video(s)!')
if not picLen == 0:
    print('Successfully moved '+str(picLen)+' photo(s)!')
if not docLen == 0:
    print('Successfully moved '+str(docLen)+' document(s)!')
if not appLen == 0:
    print('Successfully moved '+str(appLen)+' executable(s)!')
if not srtLen == 0:
    print('Successfully moved '+ str(srtLen)+' subtitle(s)!')
if not audLen == 0:
    print('Successfully moved '+ str(audLen)+' music file(s)!')
if not audLen == 0:
    print('Successfully moved '+ str(audLen)+' music file(s)!')
if not compLen == 0:
    print('Successfully moved '+ str(compLen)+' compressed file(s)!')
if not otherLen == 0:
    print('Successfully moved '+ str(otherLen)+' other file(s)!')
totalMoved = vidLen + picLen + docLen + appLen + srtLen + audLen +otherLen
print('\nMoved total of ' + str(totalMoved) + ' files')
