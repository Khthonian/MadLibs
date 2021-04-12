# Welcome the player to the game
# Ask the player if they want to begin playing
print("Hello and welcome to Mad Libs.")
playGame = input("Do you wish to begin (Yes / No): ")
# Create a while loop to manage validation of inputs
while playGame.upper() not in ['YES', 'NO']:
    playGame = input("Do you wish to begin (Yes / No): ")

# Write out the questions that will be asked to the player
university = input("Enter a university name: ")
adjOne = input("Enter an adjective: ")
adjTwo = input("Enter another adjective: ")
adjThree = input("Enter the last adjective: ")
year = input("Enter a year: ")
famousPerson = input("Enter the name of a famous person, real or fake: ")
number = input("Enter a number: ")
nounOne = input("Enter a noun: ")
plant = input("Enter a plant: ")
place = input("Enter a place: ")
adverb = input("Enter an adverb: ")
verbOne = input("Enter a verb: ")
verbTwo = input("Enter another verb: ")
name = input("Enter a name: ")

# Write out the story template that will be told in the Mad Libs game
# Interpolate the variables from the inputs to the story strings
# Allow for new lines and paragraphs as not to produce an ugly format in the console
print(f"Welcome to the University of {university}.")
print(f"Our $adjOne campus was founded by {famousPerson} and built in {year}.")
print(f"We begin at our {nounOne} building. This building houses {number} classrooms.")
print(f"To your left, the {adjTwo} dormitory is visible just beyond the {plant}.")
print(f"Our students come from all across the {place} because we {adverb} accept anyone who applies.")
print()
print(f"We will end the tour here at {name} Hall which houses the Admissions Office.")
print(f"Feel free to {verbOne} an application")
print(f"Hey folks, you're in for a treat!")
print(f"The marching band is practicing. Notice how they march in a {adjThree} formation.")
print()
print(f"More information is available on our website. Thank you for {verbTwo} with us today.")
  
   


    

