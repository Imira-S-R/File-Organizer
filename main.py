import os

print('Enter path you want to organize files: ')
path = input('> ')

for filename in os.listdir(path):
    if filename.endswith(".txt") or filename.endswith(".docx"): 
        doesExist = os.path.isdir(f'{path}\Documents')
        if doesExist:
            print(f'{path}\{filename}')
            os.replace(f"{path}\{filename}", f"{path}\Documents\{filename}")
        else:
            os.mkdir(f'{path}\Documents')
            os.replace(f"{path}\{filename}", f"{path}\Documents\{filename}")
    elif filename.endswith('.pdf'):
        doesExist = os.path.isdir(f'{path}\PDF')
        if doesExist:
            print(f'{path}\{filename}')
            os.replace(f"{path}\{filename}", f"{path}\PDF\{filename}")
        else:
            os.mkdir(f'{path}\PDF')
            os.replace(f"{path}\{filename}", f"{path}\PDF\{filename}")
    elif filename.endswith('.png') or filename.endswith('.jpg'):
        doesExist = os.path.isdir(f'{path}\Pictures')
        if doesExist:
            print(f'{path}\{filename}')
            os.replace(f"{path}\{filename}", f"{path}\Pictures\{filename}")
        else:
            os.mkdir(f'{path}\Pictures')
            os.replace(f"{path}\{filename}", f"{path}\Pictures\{filename}")
    elif filename.endswith('.exe') or filename.endswith('.msi'):
        doesExist = os.path.isdir(f'{path}\Executables')
        if doesExist:
            print(f'{path}\{filename}')
            os.replace(f"{path}\{filename}", f"{path}\Executable\{filename}")
        else:
            os.mkdir(f'{path}\Executable')
            os.replace(f"{path}\{filename}", f"{path}\Executable\{filename}")
    elif filename.endswith('.zip'):
        doesExist = os.path.isdir(f'{path}\Zip Files')
        if doesExist:
            print(f'{path}\{filename}')
            os.replace(f"{path}\{filename}", f"{path}\Zip Files\{filename}")
        else:
            os.mkdir(f'{path}\Zip Files')
            os.replace(f"{path}\{filename}", f"{path}\Zip Files\{filename}")
    elif filename.endswith('.xlsx'):
        doesExist = os.path.isdir(f'{path}\XLSX Worksheets')
        if doesExist:
            print(f'{path}\{filename}')
            os.replace(f"{path}\{filename}", f"{path}\XLSX Worksheets\{filename}")
        else:
            os.mkdir(f'{path}\XLSX Worksheets')
            os.replace(f"{path}\{filename}", f"{path}\XLSX Worksheets\{filename}")
    elif filename.endswith('.rtf'):
        doesExist = os.path.isdir(f'{path}\RTF Text')
        if doesExist:
            print(f'{path}\{filename}')
            os.replace(f"{path}\{filename}", f"{path}\RTF Text\{filename}")
        else:
            os.mkdir(f'{path}\RTF Text')
            os.replace(f"{path}\{filename}", f"{path}\RTF Text\{filename}")
    elif filename.endswith('.mp4'):
        doesExist = os.path.isdir(f'{path}\Videos')
        if doesExist:
            print(f'{path}\{filename}')
            os.replace(f"{path}\{filename}", f"{path}\Videos\{filename}")
        else:
            os.mkdir(f'{path}\Videos')
            os.replace(f"{path}\{filename}", f"{path}\Videos\{filename}")
    elif filename.endswith('.mp3'):
        doesExist = os.path.isdir(f'{path}\Music')
        if doesExist:
            print(f'{path}\{filename}')
            os.replace(f"{path}\{filename}", f"{path}\Music\{filename}")
        else:
            os.mkdir(f'{path}\Music')
            os.replace(f"{path}\{filename}", f"{path}\Music\{filename}")
    else:
        continue