

import sys

from subdb import Subdown


def main():
    name = sys.argv[1]
    down = Subdown(name)
    print("Searching Subtitle!!")
    res=down.down_load()
    if res.status_code == 200:
        print("Found!!downloading!!")
        sub=res.text
        exname=name.split('.',1)[0] + '.srt'
        with open(exname,'w') as f:
            f.write(sub)
        print("Completed!")
    else:
        print("Something went wrong! :/")



if __name__ == '__main__':
    if len(sys.argv) == 2:
        main()
    else:
        print('Provide the file as argument.')
