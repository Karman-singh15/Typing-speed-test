import random
import time

#Sample word lists
subjects = ["The dog", "A cat", "The student", "My friend", "The teacher", "The programmer", "An artist", "The scientist", "A bird", "The musician"]
verbs = ["eats", "jumps over", "writes", "paints", "builds", "runs towards", "listens to", "reads", "catches", "throws"]
objects = ["an apple", "a book", "the car", "a picture", "a sandwich", "a melody", "the ball", "the code", "a story", "the lesson"]
adjectives = ["quickly", "slowly", "carefully", "beautifully", "happily", "sadly", "angrily", "excitedly", "quietly", "loudly"]
prepositional_phrases = ["in the park", "at the beach", "on the table", "under the tree", "in the classroom", "beside the river", "near the house", "during the night", "on the road", "under the stars"]

#Function to generate a meaningful sentence
def generate_sentence():
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    obj = random.choice(objects)
    adjective = random.choice(adjectives)
    prepositional_phrase = random.choice(prepositional_phrases)
    
    sentence = f"{subject} {verb} {obj} {adjective} {prepositional_phrase}"
    return sentence

def word_test():
    #Generate 100 meaningful sentences
    dummy_database = [generate_sentence() for _ in range(100)]

    #Giving the string to write
    ques=random.choice(dummy_database)
    print(ques) 
    updated=ques.split()

    start=input('Press Enter to start: ')

    #Taking input and timing
    start_time=time.time()
    ans=input()
    end_time=time.time()

    total_time=end_time-start_time
    ans_list=ans.split( )
    wpm=((len(ans_list)/total_time)*60)
    wpm=int(wpm)
    print('Your speed is: ',wpm,'wpm')

    #Accuracy
    right=0
    wrong=0
    for i in range (len(ans_list)):
        if updated[i]==ans_list[i]:
            right+=1
        else:
            wrong+=1
    acc=(right/(right+wrong))*100
    print('Your Accuracy is: ',acc,'%')
    replay()

def replay():
    start=input('Would you like to Continue? ').lower()
    if start=='yes':
        word_test()
    else:
        print('Byeeeee')

start=input('Would you like to Check your Speed? ').lower()
if start=='yes':
    word_test()
else:
    print('Byeeeee')