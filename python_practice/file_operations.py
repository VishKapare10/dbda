import os
import subprocess

class File_ops:

    #init method
    def __init__(self):
        pass

    #Method to create file and write data to it
    def create_write_to_file(self, filename, f_no, itr):

            f_name = "%s.%d.txt" % (filename, f_no)
            with open(f_name, 'w+') as fh:
                for r in range(itr):
                        fh.write('\nUser:Vishwambhar, Date is :31/12/2020')
                        fh.write('\nAge:24')
                        os.fsync(fh)
                        fh.flush()
                        r = r + 1

    #Method to append uuid contents in a file
    def append_contents(self, filename, f_no):
        f_name = "%s.%d.txt" % (filename, f_no)
        process_uuid = subprocess.Popen(["uuid"], stdout=subprocess.PIPE)
        (stdout, err) = process_uuid.communicate()

        #remove the newline
        uuid_bytes = stdout.strip()
        uuid = uuid_bytes.decode('utf-8')
        with open(f_name, 'a+') as file:
            file.write('\nprocess_uuid = %s'%uuid)

    #Method to truncate file data
    def truncate_file(self,filename,no):
            f_name = "%s.%d.txt" % (filename, no)
            with open(f_name, 'w+') as file:
                file.truncate()

    #Method to delete file
    def delete_file(self,filename,no):
          f_name = "%s.%d.txt" % (filename, no)
          os.remove(f_name)

    #Method to read file contents
    def read_file_contents(self,filename,no):
            f_name = "%s.%d.txt" % (filename, no)
            with open(f_name, 'r') as file:
                file.read()