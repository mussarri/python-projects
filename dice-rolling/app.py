import random

def roll_dice():

    dice_drawing = {
        1: [
            "+-------+",
            "|       |",
            "|   o   |",
            "|       |",
            "+-------+"
        ],
        2:[ "+-------+",
            "| o     |",
            "|       |",
            "|     o |",
            "+-------+"
        ],
        3: [
            "+-------+",
            "| o     |",
            "|   o   |",
            "|     o |",
            "+-------+"
        ],
         4: [
            "+-------+",
            "| o   o |",
            "|       |",
            "| o   o |",
            "+-------+"
        ],
        5: [
            "+-------+",
            "| o   o |",
            "|   o   |",
            "| o   o |",
            "+-------+"
        ],
        6: [
            "+-------+",
            "| o   o |",
            "| o   o |",
            "| o   o |",
            "+-------+"
        ],
    }

    choice = input("Roll dice ? <Y>es or <N>o ")
    while(choice.lower().__contains__("y")):
        dice1= random.randint(1,6)
        dice2= random.randint(1,6)
        dice1 = "\n".join(dice_drawing[dice1])
        dice2 = "\n".join(dice_drawing[dice2])
        print(dice1 +"\n"+ dice2)
         
        choice = input("Roll again ? <Y>es or <N>o ")


roll_dice()