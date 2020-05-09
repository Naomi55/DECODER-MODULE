
def split(word): 
    return [char for char in word]  

def decodes(code,advancekey):

	length_iterator = 0 
	decoded_string = ""
	code_upper = code.upper()
	decoded_list = split(code)
	d=0
 

	list_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", 
	"J", "K","L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
	
	list_number = ["0", "1" , "2", "3", "4", "5", "6", "7", "8", "9"]
	
	print ("original chain: " + code)
	
	while length_iterator < len(code_upper):
		
		char_to_explore = decoded_list[length_iterator]

		if char_to_explore.isalpha():

			index_list = list_alphabet.index(char_to_explore.upper())
			decode_index = index_list + int(advancekey)
			decoded_string = decoded_string + list_alphabet[decode_index]
		elif char_to_explore.isnumeric():
                    
													    d=int(char_to_explore)+int(advancekey)
                              
                             
													    if d> len(list_number):
													     d=decoded_string +list_number[d]
                              
                              

													    
		
		length_iterator = length_iterator + 1
  
	print ("decoded chain: " + decoded_string)

def main():
	
	print ("-------- RebelAllianceDecoderModule ---------")
	
	inputx = input ("R2 insert the key to decode: ")
	input_advance = input ("R2 insert the advance key to generate the decode result: ")
	decodes(inputx,input_advance)

if __name__ == "__main__":
	main()