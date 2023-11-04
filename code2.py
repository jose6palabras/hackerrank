def minion_game(string):
    # your code goes here    
    kevin_score = 0
    stuart_score = 0
    leng = len(string)
    for i in range(leng):
        if string[i] in 'AEIOU':
            kevin_score = kevin_score + leng - i
        else:
            stuart_score = stuart_score + leng - i        
    if kevin_score < stuart_score:
        print("Stuart" + " " + str(stuart_score))
    elif stuart_score < kevin_score:
        print("Kevin" + " " + str(kevin_score))
    else:
        print("Draw")

minion_game("EUCALIPTO")