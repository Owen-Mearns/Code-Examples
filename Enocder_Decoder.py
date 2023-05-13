#Purpose: To make a program that can encode and decode messgaes
#Author:  Owen Mearns
#Date:    5/25/2022


#This is string is used in the fuctions to encode and decode the messages
tstString = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

'''
    Purpose of Function:  encode a given message
    @param: originalMsg(The message the user wants encoded), code(The file that has the code that determines how we encode the message)
    @return:  encodedMsg(reutrns the users message encoded)
'''

def encode(originalMsg, code):
    encodedMsg = ""
    for c in originalMsg:
        try:
            var = tstString.index(c)
            encodedMsg += code[var]
        except:
            encodedMsg += c
    return encodedMsg
    

'''
    Purpose of Function:  decode a given message in a file
    @param: codedMsg(The file thats has message the user wants decoded), code(The file that has the code that determines how we decode the message)
    @return:  decodedMsg(reutrns the users message decoded)
'''

def decode(codedMsg, code):
    decodedMsg = ""
    for c in codedMsg:
        try:
            var = code.index(c)
            decodedMsg += tstString[var]
        except:
            decodedMsg += c
    return decodedMsg


# the main routine goes here after the following line
if __name__ == "__main__" :
    
    #Variables I will use for the loops later
    valid = False
    txtValid = False
    
    #prints out header
    print("Enter E to encode a message.")
    print("Enter D to decode a message.")

    while not valid:
        
        #gets user choice for either D or E and makes it lower case
        userSelection = input("Enter your choice: ")
        userSelection = userSelection.lower()
        
        #branches that determine if the user put in E or D
        if(userSelection == "e"):
            while not valid:
                
                #asks for and verifys the users input
                try:
                    code = open(input("Enter name of the file that has the code: "))
                    originalMsg = input("Enter the message you want to encode: ")
                    print("")
                    valid = True
                    
                    #runs the function for encoding
                    encoded = (encode(originalMsg, code.read()))
                    
                    #writes the coded message into a file
                    outputFile = open("secret.txt", "w")
                    outputFile.write(encoded)
                    
                    #prints out the results
                    print("Encoded message:" , encoded)
                    print("Encoded message has been saved in secret.txt")                    
                    outputFile.close()
                    
                 #if there is an error with user input, this calls it out
                except:
                    print("Error: that file does not exist")
        
        #branches that determine if the user put in E or D           
        elif(userSelection == "d"):
            
            #asks for and verifys the users input
            while not valid:
                try:
                    code = open(input("Enter name of the file that has the code: "))
                    valid = True
                
                 #if there is an error with user input, this calls it out
                except:
                    print("Error: that file does not exist")
            
            #asks for and verifys the users input
            while not txtValid:                
                try:
                    codeMsg = open(input("Enter name of the file that has the message to decode: "))
                    txtValid = True
                
                 #if there is an error with user input, this calls it out
                except:
                    print("Error: that file does not exist") 
           
            print("")
            msg = codeMsg.read()
            
            
            #outputs the encoded and decoded message
            print("Encoded message:" , msg)
            print("Decoded message:" , decode(msg, code.read()))
        
        #if the users puts in anything besides E or D, makes them re-enter
        else:
            print("Error: You must enter E or D")
        