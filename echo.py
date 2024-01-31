#text only takes str and 3 is the number of times we want to repeat... echo returns a str
def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a fading echo."""
    #print original input
    print(text)
    #empty str to hold each echo effect
    echoing = ""
    #starts with number of repetitions and counts down to 1 
    for i in range(repetitions, 0, -1):
        #substring of original text, starting from the end of str, decreases with each iteration
        fading = text[-i:] 
        #adds each fade to each and appends new line 
        echoing += fading + "\n"
    return echoing

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
