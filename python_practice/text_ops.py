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

    #Method to get count of any word in the dictionary
    def get_count_of_occurance(self, data_dict, word):
        for key, value in data_dict.items():
            if key == word:
                return value
            else: 
                #If there is no occurance of specified word, return 0
                return 0
            
            
#Initialize file_ops object
f_inst1 = Text_data_ops()

#Method call to read file contents
data = f_inst1.read_file_contents_and_parse("motorcycle_bikers_data.txt")
print(data)

#Method call to get occurance of any word
number_of_occurances = f_inst1.get_count_of_occurance(data, "the")
print(number_of_occurances)
