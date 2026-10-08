import os
os
import pickle
contacts={}
class contact:
    def __init__(self,number,firstname,lastname,address):
        self.number=number
        self.firstname=firstname
        self.lastname=lastname
        self.address=address
def displaymenu():
    print('welcome') 
    print('-------') 
    print("total contacts:(0)".format(len(contacts))) 
    print('1.add')
    print('2.remove')
    print('3.update')
    print('4.find')
    print('5.list')
    print('6.exit')
def savecontacts():
    with open('contact.dat','bw') as filehandler:
        pickle.dump(contacts,filehandler)
def addcontact():
    os.system('cls') 
    number=input("enter number:")   
    if number in contacts:
        input('this number is exist ,press enter to back menu')  
    else:
        firsname=input('fn:')
        lastname=input('ln:')
        address=input('ad:')
        contacts[number]=contact(number,firsname,lastname,address)
        input('contact created,press enter to back menu')
        savecontacts()
def removecontact():
    os.system('cls') 
    number=input("enter number:")  
    if number in contacts:
        del contacts[number]  
        savecontacts()
        input('successful')
    else:
        input('not exist,press enter')    
def updatecontact():
    os.system('cls')   
    number=input("enter number:")
    if number in contacts:
        firstname=input('firstname('+contacts[number].firstname+'):') 
        lastname=input('lastname('+contacts[number].lastname+'):')   
        address=input('address('+contacts[number].lastname+'):') 
        contacts[number].firstname=firstname
        contacts[number].lastname=lastname
        contacts[number].address=address
        savecontacts()
        input('successful')
    else:
        input('not exist,press enter')
def findcontact():
    os.system('cls')        
    number=input("enter number:")
    if number in contacts:
        contact=contacts[number]
        print("{0}: {1} {2} {3}:".format(contact.number,contact.firstname,contact.lastname,contact.address))
        input('back')
    else:
        input('not exist,press enter')   
def listcontact():
    for key in contacts:
        contact=contacts[key]    
        print("{0}: {1} {2} {3}:".format(contact.number,contact.firstname,contact.lastname,contact.address)) 
    input('press enter') 
if os.path.exists('contacts.dat'):
    with open('contacts.dat','br') as filehandler:
        contacts=pickle.load(filehandler) 
while True:
    os.system('cls')
    displaymenu()
    print()
    option=input("select number:")

    if option=='1':
        addcontact()   
    elif option=='2':
        removecontact()
    elif option=='3':
        updatecontact()
    elif option=='4':
        findcontact()
    elif option=='5':
        listcontact()
    elif option=='6':
        break                      