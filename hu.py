import sys 
import time
import random
from colorama import Fore
import json
from readchar import readkey,key
version_msg=f'Version {sys.version[0:6]} random number generator\n'
for n in version_msg:
  sys.stdout.flush()
  time.sleep(0.01)
  sys.stdout.write(n)
else:
 while True:
    def color_random():
      color_text=Fore.RED,Fore.BLUE,Fore.GREEN,Fore.LIGHTRED_EX,Fore.LIGHTYELLOW_EX
      print(random.choice(color_text))

    color_random()
    limit=[100,1000,20000]
    generator=(random.randint(0,random.choice(limit)))
    strgenerator=str(generator)
    print(generator)
    keys=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','[']
    dict_text={random.choice(keys):generator}
    convert_to_json=json.dumps(dict_text,indent=4)
    file_name='data.json'
    with open(file_name,'a')as a:
        a.write(convert_to_json)
        time.sleep(0.1)
        a.write('\n')
        a.close()
    with open('file.txt','a')as d:
      d.write(strgenerator)
      time.sleep(0.1)
      d.write('\n')
      d.close()
 else:
    print('hello world')