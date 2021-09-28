from os import system
import random
with open("./DATA.txt","r" ) as f:
    words = [i for i in f]
mystery = random.choice(words)

def create_mystery_obj(word):
    obj = []
    for n,v in enumerate(word):
        if v != "\n":
            obj.append(" _")
    return obj
    
def output(mystery_object):
    out = ""
    for n in mystery_object:
        out += n
    return out    

def interface(mystery,obj,tries):
    system("clear")
    print("!Guess the word¡")
    print(f"{mystery} {output(obj)}\n")
    print(tries)
    print(mystery, obj, checker(obj))

def user(mystery,obj):
    letter = input("Input a letter: ")
    for n,v in enumerate(mystery):
        if letter == v:
            obj[n] = f" {mystery[n]}"

def checker(obj):
    for n in obj:
        if n == " _":
            return False
    return True    


def run():
    obj = create_mystery_obj(mystery)
    tries = 10
    while checker(obj) ^ tries > 0:
        interface(mystery, obj, tries)
        user(mystery,obj)
        tries -= 1
        

if __name__ == "__main__":
    run()
