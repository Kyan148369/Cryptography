#basically make a function with a index shifting the string by cipher encoding and dedcoding it



def string_to_number(string): 
    '''Function ends up converting the letters to lowercase and then their ASCII versions 
    returns an array'''
    arr = []
    for i in range(len(string)):
        #Converting all to lowercase cause theyre encoded in python
        string_lower = string.lower()
        arr.append(ord(string_lower[i]))
    print(arr)
    return arr

#idea is to take string_to_number func and return the final string post some transformation
def caesar_cipher_encoder_decoder(string, shift):
    #Calling the earlier modular function we had used to make sure its lower case
    #due to ordinal values vary for capital and smallcase letters
    caesar_cipher_arr = string_to_number(string)
    #iterate over the range of the array character
    for i in range(len(caesar_cipher_arr)):
        #Chr converts the ordinal number back to its alphabet and did some manipulation 
        #to make it compatible with the shift for ease of user convenience
        caesar_cipher_arr[i] = chr((((caesar_cipher_arr[i]+ shift -96) % 26)) + 96)
    transformed_arr = ''.join(caesar_cipher_arr)
    return transformed_arr



def main():
   final = caesar_cipher_encoder_decoder('lol what',5)
   print(final)
   test = caesar_cipher_encoder_decoder(final, -5)
   print(test)

if __name__ == "__main__": 
    main()