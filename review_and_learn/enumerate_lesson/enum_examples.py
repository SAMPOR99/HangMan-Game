from os import system

LISTA = ["dog","Cart","Phoenix",5,8,7,True,False,{"nose":"???","creer":"fe"},("hola",True,False)]

def go(state):
    try:
        if state == 0:
            word = "next"
        else:
            word = "finish" 
        next = input(f"write {word} to continue: ")
        next = next.strip()
        next = next.lower()
        assert next == word, f"escribe {word}"
    except AssertionError:
        go()
    if next == word:
        system("clear")    

def run():
    system("clear")
    print("welcome here you will find how enumerate function works ")
    print("so let's start with how we can enumerate an iterable ")
    print("without using the enumerate function")
    print("we have a list with many items in it, but we dont know")
    print("how many items there are, with this code we can see:")
    print("for n in range(0,len(LISTA)):")
    print("    print(n,LISTA[n])")
    print("this is the output:")
    for n in range(0,len(LISTA)):
        print(n,LISTA[n])
    go(0)
    print("now we are going to use the same list with enumerate function")
    print("the code is the following:")
    print("for index, value in enumerate(LISTA):")
    print("    print(index,value)")
    print("and this is the output:")
    for index, value in enumerate(LISTA):
        print(index,value)
    go(1)    

if __name__ == "__main__":
    run()
