class Strace_data:

        # __init__ function
        def __init__(self):
            pass

        #Method to get datafrom strace log file and add the values to the dictionary
        def get_data(self):
            with open('file_ops.log') as f:
                Lines = f.readlines()
                #Creating instace of Dict_ops class
                log_dict = Dict_ops()
                for line in Lines:
                    ls = line.split()
                    if len(ls) == 5:
                        #Method call for adding dictinary values
                        log_dict.add(ls[4],ls[3])
                    else:
                        #Method call for adding dictinary values
                        log_dict.add(ls[5],ls[3])
            print(log_dict)
            for item in log_dict:
                print("{} : {}".format(item, log_dict[item]))

class Dict_ops(dict):

        # __init__ function
        def __init__(self):
                self = dict()

        #Method to add key:value
        def add(self, key, value):
                self[key] = value

#creating instace of strace class
inst2 = Strace_data()

#Method call to get data from log file
inst2.get_data()

#Commands to run
#strace -c -o file_ops.log python3 main.py
#python3 strace_ops.py
