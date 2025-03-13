import os
import sys
def run(project):
    active_bugs = False
    path = os.path.join('.','matrixes',project)
    a= os.listdir(path)
    print(a)
    for file in a:
        if 'tracer_info' in file:
            p = os.path.join(path,file)
            old = os.path.join(p,f"matrix_{file.split('_')[2]}_full.json")
            new = os.path.join('.',"matrixes_before_change",f"{file.split('_')[2]}.json")
            if os.path.exists(old):
                os.rename(old,new)
            if not active_bugs:
                active_bugs = True
                os.rename(os.path.join(path, "active-bugs.csv"),os.path.join('.',"matrixes_before_change","active-bugs.csv"))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        run(sys.argv[1])
    else:
        run("Codec")
