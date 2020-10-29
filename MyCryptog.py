#alpha and key provided

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key =   "XPMGTDHLYONZBWEARKJUFSCIQV"

#define a function to encode text to encoded text
#create a variable and then make it upper case
#replace the spaces
#create a for loop
#for each of the letter in plain make a variable intpos (integer position)
#use index to generate a corresponding integer for the position
#create a new variable called coded(string)
#coded gets each value of key with that corresponding integer
#return coded

def encode(plain):
    plain = plain.upper()
    plain = plain.replace(" ", "")
    coded = ""
    for letter in plain:
        intpos = alpha.index(letter)
        coded = coded + key[intpos]
    return coded

#make a menu
#print Secret Decoder Menu and skip a line
#print the options for 0, 1 and 2
#get input for decision and call it response
#return response

def menu():
    print("Secret Decoder Menu\n")
    print("0 = Quit")
    print("1 = Encode")
    print("2 = Decode\n")
    response = input("What do you want to do?")
    return response

#create a function for decode
#make it uppercase and delete spaces
#create new string called result
#for loop
#for each value in coded assign the corresponding integer position with index
#result gets the letter from alpha corresponding to that integer position
#return result

def decode(coded):
    coded = coded.upper()
    coded = coded.replace(" ", "")
    result = ""
    for letter in coded:
        intpos = key.index(letter)
        result = result + alpha[intpos]
    return result

#new function main we gad to use
#use a while loop and continue while keepgoing is true
#if response is 1 get input for plain and do func encode with arg plain and print 
#if response is 2 get input for coded and do func decode with arg coded, print
#if response is 0 then display stop message
#and make keepgoing false
#else display message 

def main():
  keepGoing = True
  while keepGoing:
    response = menu()
    if response == "1":
      plain = input("text to be encoded: ")
      print(encode(plain))
    elif response == "2":
      coded = input("code to be decyphered: ")
      print (decode(coded))
    elif response == "0":
      print ("Thanks for doing secret spy stuff with me.")
      keepGoing = False
    else:
      print ("I don't know what you want to do...")

#run the main

main()
