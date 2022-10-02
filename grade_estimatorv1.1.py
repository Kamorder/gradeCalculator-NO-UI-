# Kevin Parfien 3/27/22


#Holds the overall information of the grades

#main data structure holding
gradeholding = {} 

#Used to make sure overall total is not over 100%
total = 0

#Number of sections the class grade is broken into sections
classsections = 0

#initialization
def initalizationgradeholding(sections):
    '''Names the user sections also initializes the list [weight, dictionary of assignments)]'''
    count = 0
    
    while count < sections: 
        dictkey = input(f'Please enter the name of section: {count + 1}\n')
        yorn = input(f'Is {dictkey} correct? Type y or n\n')
        
        if yorn == 'y':
            print('You picked yes\n')
            gradeholding[dictkey] = [0,{}]
            count += 1
        
def enterweights():
    '''Allows the user to enter the different weights for the classes in int form'''
    global total

    for key, value in gradeholding.items():
        weight = int(input(f"Enter the weight of {key}, please put it as an int:\n"))
        value[0] = weight
        total += weight

#Add functions(grade, section, general add)
def addgrade(name): 
    '''Allows the user to add grades to the list'''
    tempint = int(input("Enter the amount of grades you would like to put in\n"))

    for i in range(tempint):
        lst = add(i)
        gradeholding[name][1][lst[0]] = [lst[1], lst[2]]

def addsection():
    '''adds a new section'''
    dictkey = input(f'Please enter the name of section you want to add:\n')
    weight = int(input('Enter the weight of this new section:\n'))
    gradeholding[dictkey] = [weight,{}]

def add(num):
    '''returns a score that will be entered'''
    tempname = input("Enter the name of the assignment\n")
    yourscore = float(input(f"Please enter the score you recieved the assignment {num + 1}:\n"))
    totalscore = float(input(f"Please enter the total score on assignement {num + 1}:\n"))
    
    return [tempname,yourscore,totalscore]

#Remove functions(grade, section)
def removegrade(name, name2):
    '''Removes an assignment from gradeholding'''
    del gradeholding[name][1][name2]

def removesection(name):
    '''removes a whole section'''
    del gradeholding[name]

#Change functions(Grade, Weight, Section, Grade name)
def changeassigngrade(name):
    assignmentname = input("Please enter the name of the assignment you would like to change:\n").strip()
    yourscore = float(input(f"Please enter the correct score you recieved the assignment:\n"))
    totalscore = float(input(f"Please enter the correct total score on assignement :\n"))
    gradeholding[name][1][assignmentname] = [yourscore, totalscore]

def changeweight(name):
    '''changes the wieght of the value'''
    gradeholding[name][0] = input('please put in a new weight value:\n')
    
def changesection():
    '''changes the name of the section'''
    section = input('Please enter the name of the section you want to change\n')
    newsectionname = input('Please enter the new name of the section\n')
    gradeholding[newsectionname] = gradeholding[section]
    removesection(section)

def changeassignname(name):
    '''Changes the assignment name'''
    assignname = input('Please enter the name of the assignment you want to change:\n')
    newname = input('Please enter the new name of the assignemnt:\n')
    gradeholding[name][1][newname] = gradeholding[name][1][assignname]
    removegrade(name, assignname)

#Grade Calculation
def sectionsum(lst):
    ''''''
    sum = 0
    weight = lst[0]
    score = 0
    totalscore = 0

    for grades in lst[1].values():
        score += grades[0]
        totalscore += grades[1]

    if not(totalscore == 0):
        sum += weight * (score / totalscore)

    return sum

def sumgrades():
    '''Accounts for the total grade in the class returns a float value which gives final grade out of weight'''
    sum = 0
    for lst in gradeholding.values():
        sum += sectionsum(lst)
    return sum

#Note do this later since you do not have the grade scale with you right now - Find out overall percentages 
def scale():
    ''''''
    pass   

#Menu Systems
def printgrades(): 
    ''''''
    print("Your grade:\n")
    print(f'total grade percentage: {sumgrades(): .02f}%\n')
    for key, value in gradeholding.items(): 
        print(f'\nFor {key} your current weight is {sectionsum(value):.02f} of {value[0]} possible points\n')
        
        for assignments, grades in value[1].items():
            print(f'  For {assignments} you scored a {grades[0]} / {grades[1]}')

def menu():
    print('\n\n+=+=< Menu/editor for Grades >=+=+')
    print('''
o = output grades
a(1-2) = add grades or sections(in that order)
r(1-2) = remove grades or sections 
c(1-4) = change weight, assignment grades, assignment names, or sections
s = save to a file
e = end program
   
Please type your desired output
''')



#File section(Anything that pertains to files will be written here to be consistent)
def readfile():
    '''First tested thing, checks if you already have a grade set up'''
    f = open('grades.txt')
    flines = f.readlines()
    for line in flines:
        l = line.split()
        if l[0] == '$':
            section = l[1]
            gradeholding[section] = []
        elif l[0] == 's':
            gradeholding[section].append(int(l[1]))
            gradeholding[section].append({})
        elif l[0] == '!':
            gradeholding[section][1][l[1]] = [float(l[2]), float(l[3])]
       
def savefile():
    '''Saves the files in this order
        $ {Section name} 
        s {scale}
        ! {assignment name} {your score} {total score} **goes through n assignments for the section
        ** Will repeat this for other sections identifiers are put in'''
    f = open('grades.txt', 'w')
    
    for key, value in gradeholding.items():
        f.write(f'$ {key} \n')
        f.write(f's {value[0]} \n')
        for dkey, dvalue in value[1].items():
            f.write(f'! {dkey} {dvalue[0]} {dvalue[1]} \n')
    f.close()

   
#Main part of the code
def main():
    usr = 1

    while not(usr == False):
        menu()
        usr = input()
        if usr == 'o': 
            printgrades()
        elif usr == 'a1': 
            addgrade(input('Enter the section you want to enter grades into\n')) 
        elif usr == 'a2': 
            addsection()
        elif usr == 'r1': 
            removegrade(input('Enter the section you want to remove a grade\n'), input('Enter the assignment you want to remove\n'))
        elif usr == 'r2': 
            removesection(input('Enter the name of the section you want to remove\n'))
        elif usr == 'c1': 
            changeweight(input('Enter the name of the section you want to change the weight of\n')),
        elif usr == 'c2': 
            changeassigngrade(input('Enter the name of the section you want to change a grade in\n')),
        elif usr == 'c3': 
            changeassignname(input('Enter the name of the section where you want to change an assignment name\n'))
        elif usr == 'c4': 
            changesection()
        elif usr == 's':
            print('saving...')
            savefile()
        elif usr == 'e': 
            usr = False



#Start of main part of code
print("\nWelcome to the grade estimator v1.1\n\n")
try: 
    readfile()
except:
    #Initialization if the grade section does not exist
    while classsections == 0:
        try:
            classsections = int(input("Please enter the number sections your grade breaks down into\n"))
        except:
            classsections = 0 
            print("Error is not an int")
    
    #Shows the user the amount of sections the user entered
    print(f"You entered {classsections} sections\n")
    initalizationgradeholding(classsections)
    enterweights()

main()


