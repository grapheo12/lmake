import os
import subprocess
import sys
import time

def trackFile(fpath, conf=None):
    name, extension = os.path.splitext(fpath)
    last_modified = os.path.getmtime(fpath)
    if conf is None:
        subprocess.call(["make", name])
        run = subprocess.Popen(["./{}".format(name)], stdout=sys.stdout, stdin=sys.stdin)
    else:
        conf['compile'] = conf['compile'].replace('?fpath?', fpath)
        conf['compile'] = conf['compile'].replace('?name?', name)
        conf['run'] = conf['run'].replace('?fpath?', fpath)
        conf['run'] = conf['run'].replace('?name?', name)

        
        subprocess.call(conf['compile'].split(" "))
        
        if 'input' in conf:
            fp = open(conf['input'], "r")
            run = subprocess.Popen(conf['run'].split(" "), stdout=sys.stdout, stdin=fp)
        else:    
            run = subprocess.Popen(conf['run'].split(" "), stdout=sys.stdout, stdin=sys.stdin)

    while True:
        try:
            new_last_modified = os.path.getmtime(fpath)
            if new_last_modified > last_modified:
                print("Change detected")
                last_modified = new_last_modified
                run.terminate()
                if conf is None:
                    subprocess.call(["make", name])
                    run = subprocess.Popen(["./{}".format(name)], stdout=sys.stdout, stdin=sys.stdin)
                else:
                    conf['compile'] = conf['compile'].replace('?fpath?', fpath)
                    conf['compile'] = conf['compile'].replace('?name?', name)
                    conf['run'] = conf['run'].replace('?fpath?', fpath)
                    conf['run'] = conf['run'].replace('?name?', name)

                    # print(conf['run'])
                    subprocess.call(conf['compile'].split(" "))
                    if 'input' in conf:
                        fp = open(conf['input'], "r")
                        run = subprocess.Popen(conf['run'].split(" "), stdout=sys.stdout, stdin=fp)
                    else:    
                        run = subprocess.Popen(conf['run'].split(" "), stdout=sys.stdout, stdin=sys.stdin)


            time.sleep(0.5)
        except KeyboardInterrupt:
            print("Bye")
            exit(0)