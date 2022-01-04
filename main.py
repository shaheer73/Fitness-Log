from time import sleep

print ("")
print ("Hello dear Judges of EngHack Quest-Stream. We Byte-Size, are exicted to present to you")
print ("our project called 'My Fitness log'. Our Python program allows you, the user,")
print ("to keep track of your personal fitness goals, by telling you the recommended calories")
print ("to eat in a day depending on if you want to lose, gain or maintain your weight.")
print ("You will have the opportunity to input what food you ate and how many calories")
print ("of that food you consumed. It also lets you track your workout for the day by inputting")
print ("what exercise you did and with what weight and how many sets and reps aswell.")
print ("This is the ultimate fitness tracking program and we hope you enjoy !")
print ("To begin, we need your help by answering some questions.")
print ("")
sleep(2)


#--------------------------------------------------------------------------------
import math

#Calorie Function 
 
#male or female 


while True:
    sex = input("What is your sex? (m)ale or (f)emale? ")

    if sex == "m":
        gender = 1
        break
    elif sex == "f":
        gender = 2
        break
    else:
        print("please enter m or f")



# body weight 

while True:
    weight = input("What is your weight (lbs)? ")
    try:
        val = int(weight)
        break
    except ValueError:
        print("Please enter a number")

bw = float(weight)
    
W = (bw/2.2)



#height 

while True:
    height = input("What is your height (cms)? ")
    try:
        val = int(height)
        break
    except ValueError:
        print("Please enter a number")

H = float(height)



#Age

while True:
    age = input("How old are you? ")
    try:
        val = int(age)
        break
    except ValueError:
        print("Please enter a number")

A = float(age) 



if gender == 1 :
    bmr = 88.362 + (13.397*W) + (4.799*H) - (5.677*A)

if gender == 2 :
    bmr = 447.593 + (9.247*W) + (3.098*H) - (4.330*A)

while True:
    activityLevel = input("What is your activity (none, light, moderate, or heavy): ")
    if activityLevel == "none":
        activityLevel = 1.2 * bmr
        break
    elif activityLevel == "light":
        activityLevel = 1.375 * bmr
        break
    elif activityLevel == "moderate":
        activityLevel = 1.55 * bmr
        break
    elif activityLevel == "heavy":
        activityLevel = 1.725 * bmr
        break
    else:
        print("please enter a valid answer")

while True:
    choice = input("Would you like to lose, gain or maintain your weight? ")

    dCal = ""
    sCal = ""
    mCal = ""

    if choice == "lose":
        goal = str('Deficit') 
        dCal = activityLevel - 500
        Recommended = dCal
        print("To lose weight you need to eat", round(dCal), "calories a day.")
        sleep(2)
        break

    if choice == "gain":
        goal = str('Surplus') 
        sCal = activityLevel + 750
        Recommended = sCal
        print("To gain weight you need to eat", round(sCal), "calories a day.")
        sleep(2)
        break

    if choice == "maintain":
        goal = str('Maintain') 
        mCal = activityLevel
        Recommended = mCal
        print("To maintain weight you need to eat", round(mCal), "calories a day.")
        sleep(2)
        break

    else:
        print("Please enter a valid answer")



#--------------------------------------------------------------------------------

print ("")
print ("Now, since we have collected your recommened calories for your goal today,")
print ("you must input what you have ate with the correct nutrition values, our")
print ("program will ask you how many food items you have ate and after the specific")
print ("name and number of calories. Please do this with all food items.")
print ("")
sleep(2)

foods = []
consumed = []

items = int(input("How many food items did you today: "))
num = items + 1
for i in range(1,num):
    food = input("What did you eat? ")
    calories = int(input("How many calories was in that? "))
    foods.append(food)
    consumed.append(calories)

TotalConsumed = sum(consumed)

print ("You have consumed:", TotalConsumed, "calories")
sleep(2)


#--------------------------------------------------------------------------------



sum = (Recommended - TotalConsumed)

if goal == "Deficit" :
    if sum > 0 :
        print ("You are on the path of losing weigth.")
        print ("You can also eat a total of", round(sum), "calories before you exceed your goal!")
    if sum < 0 :
        print ("You have exceeded your recommended calorie intake for your goal by:", round(sum * -1))
    if sum == 0 :
        print ("You have met your recommended calorie intake, meaning you are not losing or gaining weight.")

if goal == "Surplus" :
    if sum > 0 :
        print ("You have not met your recommended calorie intake for your goal.")
        print ("You still have:", round(sum), "calories to eat!")
    if sum < 0 :
        print ("You are on the path of gaining weigth. Goodjob")
    if sum == 0 :
        print ("You have met your recommended calorie intake, meaning you are not losing or gaining weight.")

if goal == "Maintain" :
    if sum > 0 :
        print ("You are on the path of losing weigth. This is not meeting your goal")
        print ("You must eat", round(sum), "more calories!")
    if sum < 0 :
        print ("You are on the path of gaining weight. This is not your goal")
        print ("You must burn", round(sum), "calories to meet your goal!")
    if sum == 0 :
        print ("You have met your recommended calorie intake, meaning you are not losing or gaining weight.")



#--------------------------------------------------------------------------------
sleep(2)
print ("")
print ("Now that we have dealt with everything that takes place in the kitchen,")
print ("we can now move on to the training. The program will now ask the user to")
print ("input details about today's workout.")
print ("")
sleep(2)

from tabulate import tabulate

class Excercise_Table:
    while True:
        workout_num = input('How many Exercises have you done today? \n')
        try:
            val = int(workout_num)
            break;
        except ValueError:
            print("Please enter a number")

    workout_table = [['Exercise', 'Sets', 'Reps', 'Weight(lbs)']]

    for i in range(val):
        print("---------------\nExercise", i+1,"\n---------------")

        excercise = input('Name of Exercise:\n')

        while True:
            sets = input('Number of Sets:\n')
            try:
                val = int(sets)
                break;
            except ValueError:
                print("Please enter a number")

        while True:
            reps = input('Number of Reps:\n')
            try:
                val = int(reps)
                break;
            except ValueError:
                print("Please enter a number")

        while True:
            weight = input('Weight used:\n')
            try:
                val = int(weight)
                break;
            except ValueError:
                print("Please enter a number")

        workout = [excercise, sets, reps, weight]

        workout_table.append(workout)

    print (tabulate(workout_table, headers='firstrow'))

sleep(2)
print ("")
print ("Thank you for using Team Byte-Size's 'My Fitness Log'! ")
print ("Have a Good Day! Keep staying healthy.")
print ("")
sleep(2)