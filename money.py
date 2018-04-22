print("Welcome to the Rohan Salery Income Program!")
money= input("Did you make money?")
defaultnum= 0
defaultwhere= "School"
defaultwhen="01/02/2019"
if money ==("Yes"):
      newnum= input("How much money did you make?")
      newnum=defaultnum
      newwhere= input("Where did you make this money?")
      newwhere=defaultwhere
      newwhen=input("When did you make this money?")
      newwhen=defaultwhen
      print("This info has been saved.")
elif money == ("No"):
      print ("You made", defaultnum,"dollers at" ,defaultwhere,"on" ,defaultwhen,".")
else:
            print ("Thank you for using Rohan's Salery Income Program.")
            print("If you think this is error, try again.")
                
quit()
