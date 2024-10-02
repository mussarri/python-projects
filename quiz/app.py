questions = {
    "question1":{
        "question": "What is the Capital of Turkey ?",
        "answer" : "ankara"
    },
    "question2":{
        "question": "What is the Capital of Germany ?",
        "answer" : "Berlin"
    },
    "question3":{
        "question": "What is the Capital of Italy ?",
        "answer" : "Roma"
    },
    "question4":{
        "question": "What is the Capital of Spain ?",
        "answer" : "Madrid"
    },
    "question5":{
        "question": "What is the Capital of France ?",
        "answer" : "Paris"
    },
    "question6":{
        "question": "What is the Capital of England ?",
        "answer" : "Londra"
    },
}

score = 0

for key, value in questions.items():
    print(key + " :")
    print(value["question"])
    answer = input("Answer: ")
    if(answer.lower() == value["answer"].lower()): 
        score=score+1
        print("True")
    else :
        print("Wrong Answer")

print("Your score is " + str(score)  + " in " + str(len(questions)))

