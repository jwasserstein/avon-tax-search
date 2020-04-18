from bs4 import BeautifulSoup
import os


os.chdir('html/A/')

with open('A.html', 'r') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')
    a = soup.find_all('a')
    for i in a:
        ihref = i.get('href')
        if ihref is None or ihref == '/index.html':
            continue
        print('running: ' + 'wget http://www.avonassessor.com' + ihref)
        os.system('wget http://www.avonassessor.com' + ihref)
