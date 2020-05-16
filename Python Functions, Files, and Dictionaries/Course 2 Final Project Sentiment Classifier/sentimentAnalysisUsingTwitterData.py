
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
projectTwitterDataFile = open("project_twitter_data.csv","r")
resultingDataFile = open("resulting_data.csv","w")

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_pos(strSentence): 
    sentence = strip_punctuation(strSentence.lower())
    words = sentence.split(" ")
    count=0
    for word in words:
        if word in positive_words:
            count+=1
    return count            
            
            
def get_neg(strSentence):
    sentence = strip_punctuation(strSentence.lower())
    words = sentence.split(" ")
    count=0
    for word in words:
        if word in negative_words:
            count+=1
    return count
            
def strip_punctuation(strWord):
    for charPunct in punctuation_chars:
        strWord = strWord.replace(charPunct, "")
    return strWord            
            
def writeInDataFile(resultingDataFile):
    resultingDataFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")

    linesPTDF =  projectTwitterDataFile.readlines()
    headerDontUsed= linesPTDF.pop(0)
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(',')
        resultingDataFile.write("{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]), (get_pos(listTD[0])-get_neg(listTD[0]))))    
        resultingDataFile.write("\n")

        

writeInDataFile(resultingDataFile)
projectTwitterDataFile.close()
resultingDataFile.close()