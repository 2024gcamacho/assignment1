#echo.py
#Guadalupe Camacho - CS:3980 SPR24

def echo(text: str, repetitions: int = 3) -> str:
    #text only takes str and 3 is the number of times we want to repeat... echo returns a str
    """Imitate a fading echo."""
    #print original input
    print(text)
    #empty str to hold each echo effect
    echoing = ""
    #starts with number of repetitions, subtracts 1 each iteration until 0
    for i in range(repetitions, 0, -1):
        #last 3 of text decreases with each iteration
        echoing += text[-i:] + "\n"
    return echoing

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
