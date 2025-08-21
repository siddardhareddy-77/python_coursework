import os
import shutil

if not os.path.exists('python files'):
    os.mkdir('python files')

os.rmdir('python files')

shutil.rmtree('python files')

print(os.getcwd())
print(os.listdir())

os.chdir('..')