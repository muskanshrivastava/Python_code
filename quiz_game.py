import requests
import json
import random
import html

no_opt = ['n','no','quit','exit']
yes_opt = ['y','yes']
char = input("Do you want to play quiz : ")
score_correct = score_incorrect = 0

if char.lower() in yes_opt:
    while char.lower() in yes_opt:
        req = requests.get("https://opentdb.com/api.php?amount=1")
        if req.status_code != 200:
            char = input("Sorry!! There was a problem, press 'enter' to start again or type 'quit' to quit the game")
        else:
            number = 1
            data = json.loads(req.text)
            question = data['results'][0]['question']
            correct_ans = data['results'][0]['correct_answer']
            options = data['results'][0]['incorrect_answers']
            options.append(correct_ans)
            random.shuffle(options)

            # html.unescape() is used to avoid html quotes to print with output
            print(html.unescape(question))
            for i in options:
                print(number,html.unescape(i))
                number += 1
                       
            while True:        
                print("\nType the number of answer : ",end = "")
                try:
                    answer = int(input())
                    if answer > len(options) or answer <= 0:
                        print("INVALID INPUT.....Please enter correct answer")
                    else:
                        print("Valid Input")
                        break
                except:
                    print("INVALID INPUT.....")
                        
            if options[answer - 1].lower() == correct_ans.lower():
                print("\nCongratulations !! You have answered correctly. \nThe correct answer was : ",correct_ans)
                score_correct += 1

            else :
                print("\nSorry !!! Incorrect Answer")
                print("The correct answer is : ",  correct_ans.capitalize())
                score_incorrect += 1
                
            char = input("\nDo you want to play again ?? : ")
            if char.lower() in no_opt :
                print("Number of answers you have given correctly : ",score_correct)
                print("Number of answers you have given incorrectly : ",score_incorrect)
                print("\nThanks for playing ...!!\n")
                exit()
else :
    print("\nThank You ! for your response .... !!!\n")

            
            
            

            
    
    
            
                
            
            

            
            

            
            
            



