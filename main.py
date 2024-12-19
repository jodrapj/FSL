import os, sys, shutil

class Ev:
    
    def ev(self, l:str):

        lines = [x for x in l.split("\n") if x.strip != ""]
        pc = 0
        while pc < len(lines):
            line = lines[pc]
            args = line.split(maxsplit=3)
            match line.split(maxsplit=1)[0]:   

                case 'CREATE':
                    if args[1] == "FILE":
                        open(args[2], "w")
                    elif args[1] == "DIR":
                        if not os.path.exists(args[2]):
                                os.mkdir(args[2])
                    pc += 1

                case 'DELETE':
                    if args[1] == "FILE":
                        os.remove(args[2])
                    elif args[1] == "DIR":
                        shutil.rmtree(args[2])
                    else:
                        print("file does not exist")
                    pc += 1

                case 'OPEN':
                    os.chdir(args[1])
                    pc += 1

                case 'WRITE':
                    f = open(args[1], 'a')
                    pc += 1
                    while lines[pc].split(maxsplit=1)[0] != 'STOP':
                        f.write(lines[pc].split(maxsplit=1)[0])
                        pc += 1

                case 'STOP':
                    pc += 1
                
                case 'COPY':
                    if args[1] == "FILE":
                        shutil.copy2(args[2], args[3])
                    pc += 1
                    
    
Ev().ev(open("./test.fsl").read())