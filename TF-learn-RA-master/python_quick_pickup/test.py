import json

def ifStatementPractice():
    cars = ["audi", "mazada", "nissan"]
    for car in cars:
        if car == "mazada":
            print("A nice "+str(car))
        else:
            print("...")


def adminPractice(userInput):
    userNames = ("admin", "haomin", "laurie", "bob", "selfie")
    #if the user name is admin, print special greet, else, print gereric greet
    for userName in userNames:
        if userInput == userName and userInput == userNames[0]:
            print("ADMIN login " + str(userName))
            break
        elif userInput in userNames:
            print("Welcome " + str(userInput))
            break
        elif userInput not in userNames:
            print("please contact admin for more info")
            break

def loopThroughDict():
    myDict = {"A":"alpha", "B":"beta", "Z":"zelta"}
    for i, y in myDict.items():
        print ("Key is: " + str(i) + "\n" + "Value is: " + str(y))
    for j in myDict.values(): #testing looping through all the values; .keys() vice versa
        print (str(j))

    sorted(myDict,reverse=True)
    print (myDict)
    # an example of looping through the dictionary

def loopThroughUnique():
    print("loop Through Unique")
    myDict = {"A": "alpha", "B": "beta", "Z": "zelta", "D": "beta"}
    for i in set(myDict.values()):
        print (i)
    print("loop through normal")
    for i in myDict.values():
        print (i)

def nestingDict():
    aliens = {"Alien_1":"","Alien_2":{"Color":"Green","Height":"172 cm", "Alien_3":""}}
    print(aliens)
    aliens["Alien_1"] = {"Color": "Blue", "Height": "99cm"}
    aliens["Alien_3"] = {"Color":"","Height":""}
    aliens["Alien_3"]["Color"] = "Red"
    aliens["Alien_3"]["Height"] = "101 cm"
    print(aliens)
    list_inDict = {"List 1" : [1,2,3,4,5]}
    print(list_inDict)
    print(list_inDict["List 1"][0])

def list_of_dict():
    aliens = [""]
    aliens[0] = {"Color": "Green", "Height": "172 cm"}
    aliens.append({"Color": "Purple", "Height": "171 cm"})
    print (aliens)
    print (aliens[1])

def nestingPractice():
    students = {"Student 1":{"Name":"Alice","ID":"3123", "Gender":"F"},"Student 2":{"Name":"Bob", "ID":"31211","Gender":"M"}}
    for student, student_info in students.items():
        print (str(student))
        print ("\t"+student_info["Name"] + "\n"
                + "\t"+student_info["ID"] + "\n"
                + "\t"+ student_info["Gender"] + "\n")

def functionReturn (string1, string2 = ""):
    if string2 == "":
        return string1.title()
    else:
        return string1.title() + string2.title()

def functionParameter(first, last, **moreInfo):
    """building a dictionary based on the info user provided"""
    profile = {}
    profile["First Nmae"] = first; profile["Last Name"] = last
    for key, value in moreInfo.items():
        profile[key] = value
    print (profile)  

def whileLoopPractice():
    loop_counter = 0
    while loop_counter < 10:
        print (loop_counter)
        loop_counter+=1
    # continue example
    print("second loop")
    loop_counter_1 = 0
    while loop_counter_1 < 10:
        loop_counter_1 +=1
        if (loop_counter_1 % 2 == 0):
            continue
            print ("This will never be executed")
        print(loop_counter_1)
    #this loop only print out the odd numbers, what the continue does, is if the "continue" is hit
    #then it will jump back to the beginning of the loop instead of running the code after the continue

# -------------------------------------------------------------------------------
class Dog():
    """a simple class called Dog, and it is to simulate a dog"""

    def __init__(self, name, age):
        """initialize name and age for the dog"""
        self.name = name
        self.age = age
        self.habbit = "need info" #this is a defalut value, "need info"

    def sit(self):
        print(self.name.title() + " is now sited")

    def roll_over(self):
        print(self.name.title() + " rolled over!")
    
    def rename_doggo(self, name): # setter
        self.name = name
    
    def doggos_name(self): # getter
        return self.name

class Super_Dog(Dog): #notice this line here, you need to pass the super class obj into the sub class
    """this is a class that inherit the class dog"""
    def __init__(self, name, age):
        super().__init__(name,age)
        self.powerLevel = 100

    #override demo
    #in python, to override a method that is in the super class, you just create a method
    #that has the same name, and put the code you want in the one you just created, and
    #python will run this instead of the method that is in the super class
    def roll_over(self):
        print(self.name.title() + "rolled over 9000 times! impressive")
        
    def getPowerReadings(self):
        print("The power reading is off the chart!!! it is: " + str(self.powerLevel))

class Cute_dog(Dog):
    """this is a demo of an instance as an attribute"""
    def __init__(self, name, age):
        super().__init__(name, age)
        self.cutness = Cuteness()
    
class Cuteness():
    def __init__(self):
        self.cuteLevel = "super unbelieve, crazy, impressively cute, so cute, turns out its a cat..."
    def howCute(self):
        print(self.cuteLevel)

# ---------------------------------------------------------------------------------

# everything about reading a file:
def fileOpen():
    """"it is also possible to implemnet the file path and open the file path as the file"""
    # file_path = '/home/haominshi/files/filename.txt'
    # with open(file_path) as pi_number

    file_location = "pi.txt"

    with open(file_location) as pi_number:
        contents = pi_number.read()
        print(contents)
        print(contents.lstrip())
    
    """it is also possible to read the file line by line"""
    with open(file_location) as pi_number:
        for line in pi_number:
            print(line)
    # for reading line by line, notice there are is a empty line after line. it is because when you press
    # enter in the file, there is a new line break at the end. what you need to do is to implement rstrip()
    # to remove the line breaker
    with open(file_location) as pi_number:
        for line in pi_number:
            print(line.rstrip()) # now the new line break has been cleared

    # Making a list of lines from a file
    with open(file_location) as pi_number:
        lines = pi_number.readlines() # this will return the lines in the file as a LIST
    print (lines)

def workingWithFileContent():
    file_loc = "pi.txt"
    with open(file_loc) as file:
        lines = file.readlines()
    pi_string = ""
    pi_string_2 = ""
    for line in lines:
        pi_string += line.rstrip() # white space on the left is included
    for line in lines:
        pi_string_2 += line.strip() #this one take away all the white spaces
    
    print (pi_string)
    print (str(len(pi_string))) # basically what this did is that reading lines; from file (pi.txt)
                                # and append the pi_string, like a string builder
    print (pi_string_2)

def writeOnFiles():
    # flags in this one:
        # 'r' read || no flag = read only
        # 'w' write
        # 'a' append    
    file_loc = "pi.txt"
    with open(file_loc,'a') as file:
        file.write("JAVAVAVAVAVAVAVA #1 \n")


def exceptionPractice(a,b):
    try:
        ans = a/b
    except ZeroDivisionError:
        print (" you cant divid by zero ")
    else:
        print(ans) # everything in the else will be execute if try block gose through without the exception
    
def jsonEdit(usname):
    # to deal with JSON python need to import json
    userName = usname
    with open("user_name.json", 'w') as f_obj:
        json.dump(userName, f_obj)
    print("dumped")


def toUpperCase4testing(someString):
    return someString.upper()
            
def main():
    """this is the practice function"""
    dimensions = (200, 50)
    print (dimensions[0], dimensions[1])
    print ("\n")
    #this is a example of tuples; the main different of this
    #compare to the list, the tuples cannot be modified once it is created
    """now a practice to loop through all the element in a tuple"""
    for i in dimensions:
        print (str(i) + " This is the same thing as list")
    ifStatementPractice()
    adminPractice("laurie")
    # adminPractice(input("for adminPractice method: "))
    loopThroughDict()
    loopThroughUnique()
    nestingDict()
    list_of_dict()
    nestingPractice()
    whileLoopPractice()
    print(functionReturn("haha"))
    functionParameter("Jimmy","Johns",Location = "Chicago",Grade = "Bad")
    #now a demo to how to use class in python
    my_dog = Dog("Dengdeng", 13)
    print('The name of my dog is: ' + str(my_dog.name) + ' and he is: ' + str(my_dog.age) + ' years old!')
    my_dog.sit();my_dog.roll_over();
    print(my_dog.habbit)
    my_dog.habbit = "like to go outside"
    print(my_dog.habbit)
    my_dog.rename_doggo("Huihui")
    print(my_dog.name)
    print(my_dog.doggos_name())
    my_super_dog = Super_Dog("DengDeng", 13)
    my_super_dog.getPowerReadings()

    my_cute_dog = Cute_dog("MiMi", 15)
    my_cute_dog.cutness.howCute()
    my_cute_dog.cutness.cuteLevel = "Uber CUTE"
    my_cute_dog.cutness.howCute()

    fileOpen();workingWithFileContent()
    writeOnFiles()

    exceptionPractice (0,0)

    jsonEdit('hahaMyName')

# correct way to run main in Python
if __name__ == "__main__":
    main()



    
