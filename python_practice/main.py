from file_operations import File_ops

#creating instace of file class
inst1 = File_ops()

for i in range(10):
    inst1.create_write_to_file("fops",i,80)

#method call truncate file fops1.txt
inst1.truncate_file("fops",1)

for i in range(10):
    inst1.append_contents("fops",i)
    inst1.read_file_contents("fops",i)
    inst1.delete_file("fops",i)
