#Text Operations class
class Text_data_ops:

    #init method
    def __init__(self):
        pass

    #Method to read file contents, parse and returns dictionary
    def read_file_contents_and_parse(self,filename):
            with open(filename, 'r') as file:
                #Initialize an empty dictionary
                parse_data = dict()

                #Iterate through each line of the file
                for line in file:
                    # Remove the leading spaces and newline character
                    line = line.strip()

                    # Convert the characters in a line to lowercase
                    line = line.lower()

                    #Split the line into words
                    words = line.split(" ")

                    # Iterate through each word in line
                    for word in words:
                        # Check if the word is already in dictionary
                        if word in parse_data:
                            # Increment count of word by 1
                            parse_data[word] = parse_data[word] + 1
                        else:
                            # Add the word to dictionary with count 1
                            parse_data[word] = 1

                #return dictionary containing key as word and count as value
                return parse_data

    #Method to append another file contents in a file
    #This method reads file contents of file 1 and append in file 2 line by line
    def append_contents(self, file1, file2):
        with open(file2, 'a+') as file:
            with open(file1, 'r', encoding='utf-8')as fp:
                for line in fp:
                    file.write(line)

    #Method to get count of any word in the dictionary
    def get_count_of_occurance(self, data_dict, word):
        for i in data.items():
                   lst = list(i)
                   if lst[0] == word:
                        return [word,lst[1]]


#Initialize file_ops object
f_inst1 = Text_data_ops()

'''
#before appending data
data = f_inst1.read_file_contents_and_parse("motorcycle_bikers_data.txt")
#print(data)
no_of_occurances = f_inst1.get_count_of_occurance(data, 'is')
print(no_of_occurances)
'''

#Infinite loop for appending file contents, reading and parsing and getting no of occurances of any perticular word
while(1):
    f_inst1.append_contents("road_data.txt", "motorcycle_bikers_data.txt")
    data = f_inst1.read_file_contents_and_parse("motorcycle_bikers_data.txt")
    #print(data)
    no_of_occurances = f_inst1.get_count_of_occurance(data, 'is')
    if no_of_occurances != None:
        print("No of occurances of word '{}' are {}".format( no_of_occurances[0],no_of_occurances[1]))
    else:
        print("No occurance found, returntype: {}".format(no_of_occurances))
