import sys #imports a function that allows the code to end
def job_interview(): #defines a function
    x = "The following questions are for a job interview"
    print(x)

job_interview() #runs the function


class applicant: #creates a class
  def __init__(self, name, college):
    self.name = name
    self.college = college

  def myfunc(self): #impliments inheritance
    print("Your name is " + self.name)
    print("And you are from " + self.college)
    print("Correct?")


app = applicant("Viktor", "Stanford") #prints info in the class
app.myfunc()




t = input() #prompts the user for info
if t == "yes": #uses a if else loop to change the outcome of the code based on the users input
	print("Hi Viktor, welcome to this interview")
else:
	print("Leave")
	sys.exit() #terminates the code
	


print("what made you want to be a programmer")
Reason = input() #prompts for a input

print("The estimated income if your application is accepted is 60,000 dollars a year")

income = 60000 #sets a variable as a numeric value

print("your estimated bonus would be 3,600 dollars")

income += 3600 #uses operators to add to a value

print(income)
print("are you okay with this?")
answer = input()#asks for a input

if answer == "yes": #uses a if or else loop to change the outcome of the code based on the input
	answer1 = True #boolean variable
else:
	answer1 = False #boolean variable

print("do you want to sign this contract?")
answer2 = input()#prompts for info from the user
if answer2 == "yes": #uses a if or else loop to change the outcome of the code based on the input
	answer2 = True #boolean variable
else:
	answer2 = False #boolean variable

if answer1 and answer2: #uses and to check if the booleans are true
	print("Good")
else:
	print("okay, then you're not getting the job")
	sys.exit() #exits the system
	

print("One last question is are you prepared to work for this company?")
answer3 = input() #prompts for input
if answer3 == "yes":
  answer3 = True
else:
  print("Leave")
  sys.exit() #exits code
  
	

while answer3: #while loop occurs when a variable is true
  print("Okay you're hired")
  break #stops the loop from repeating

print("new list of employees")
Newlistofemployees = ["Viktor", "Chad", "Melissa"] #string variable
for g in Newlistofemployees: #for loop
	print(g)



Fileinvariable = open("Midterm4.txt", "a") #opens, reads, and writes from a file
Fileinvariable.write("60000, 65000, 55000")
Fileinvariable.close()

Fileinvariable = open("Midterm4.txt", "r")
print(Fileinvariable.read())  #reads the file
