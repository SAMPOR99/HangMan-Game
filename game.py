from os import system
import random
with open("./DATA.txt","r" ) as f:
    words = [i for i in f]
#mystery = random.choice(words)
#mystery = normalize(mystery)
def create_mystery_obj(word):
    obj = []
    for n,v in enumerate(word):
        if v != "\n":
            obj.append(" _")
    return obj

def normalize(s): # It removes the accents of a string
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s



def output(mystery_object):
    out = ""
    for n in mystery_object:
        out += n
    return out    

def interface(mystery,obj,tries):
    system("clear")
    print("!Guess the word¡")
    print(f"{output(obj)}\n")
    print(f"tries: {tries}")

def user(mystery,obj,letter):
    #letter = input("Input a letter: ")
    for n,v in enumerate(mystery):
        if letter == v:
            obj[n] = f" {mystery[n]}"
    

def guessed(obj,state):
    if state:
        return False
    for n in obj:
        if n == " _":
            return False
    return True    

def results(state,mystery):
    if state == 0:
        system("clear")
        print(f"Ganaste la palabra es: {mystery}")
    elif state == 1:
        system("clear")
        print(f"Perdiste la palabra era: {mystery}")

def run():
    mystery = random.choice(words)
    mystery = normalize(mystery)
    obj = create_mystery_obj(mystery)
    tries = 30
    while (not guessed(obj,False) and tries > 0):
        interface(mystery, obj, tries)
        letter = input("Input a letter: ")
        user(mystery,obj,letter)
        tries -= 1
    if guessed(obj,False):
        results(0,mystery)
    elif tries == 0:
        results(1,mystery)

if __name__ == "__main__":
    run()
