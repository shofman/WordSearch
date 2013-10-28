import sys, pygame, math, string, random, operator
pygame.init()

#TODO list
#Work on font choice
#Create autogenerator
#Create GUI interface for certain features (that would be useful)

#Bug list
#Top left part has error
#Does not win when user finishes list

class Grid:
    """A single letter of the word search"""
    def __init__(self, x, y, letter):
        self.letter = letter
        self.timesHit = 0
        self.position = self.x, self.y = (x,y)

    def getPixel(self):
        return (self.position[0]*32, self.position[1]*24)

def setWordAppearance(mode):
    if mode == 1:
        return ['Activities', 'Ages', 'Attend', 'Balls', 'Beach', 'Bell', 'Blocks', 'Bonds', 'Boxes', 'Brush', 'Bubbles', 'Build', 'Celebrate', 'Circle', 'Clay', 'Climb', 'Color', 'Copied', 'Crayons', 'Curriculum', 'Dance', 'Desks', 'Dressup', 'Easel', 'Easy', 'Elementary', 'Entrance', 'Explore', 'Film', 'Friends', 'Game', 'Half a Day', 'Imagination', 'Influence', 'Interactive', 'Involve', 'Juice', 'Junior', 'Language', 'Lead', 'Learn', 'Lessons', 'Life', 'Literacy', 'Lunch', 'Materials', 'Math', 'Milestones', 'Music', 'Nature', 'Paint', 'Photocopy', 'Pile', 'Plasticine', 'Playgrounds', 'Playing', 'Please', 'Pointer', 'Preschool', 'Programs', 'Reasoning', 'Safe', 'Scope', 'Senior', 'Session', 'Show', 'Sing', 'Skills', 'Sleep', 'Snack', 'Social', 'Speak', 'Teacher', 'Tests', 'Theme', 'Time', 'Trace', 'Week', 'Word']
    elif mode == 3:
        return ['Aisle', 'Announcement', 'Appointments', 'Bells', 'Blue', 'bold', 'Book', 'Budget', 'Buses', 'Cake', 'Centerpieces', 'Chairs', 'Checklist', 'Cheers', 'Chocolate', 'Choir', 'Colors', 'Confirm', 'Contact', 'Date', 'Deals', 'Decorate', 'Dinner', 'Documents', 'Dresses', 'Engaged', 'Entertainment', 'Event', 'Excited', 'Favors', 'Fittings', 'Florist', 'Garden', 'Gifts', 'Hire', 'Hotel', 'Invitations', 'Lesson', 'License', 'Love', 'Maid of Honor', 'Party', 'Payments', 'Pedicure', 'Petals', 'Photographer', 'Reception', 'Rehearsal', 'Rise', 'Rings', 'Schedule', 'Seating', 'Select', 'Service', 'Shoes', 'Show', 'Stag', 'Stationary', 'Symbol', 'Tailor', 'Tasting', 'Theme', 'Toast', 'Traditional', 'Transportation', 'Tuxedo', 'Veil', 'Venue', 'Vows', 'Wish']
    else: #mode == 2:
        return ['Adidas', 'Adjustable', 'Authentic', 'Baseball', 'Basketball', 'Bears', 'Bengals', 'Bills', 'Black', 'Blend', 'Blocks', 'Blue', 'Brand', 'Brim', 'Broncos', 'Buccaneers', 'Canvas', 'Caps', 'Cardinals', 'Casual', 'Cloth', 'Color', 'Colts', 'Common', 'Cool', 'Cotton', 'Custom', 'Eagles', 'Eyelets', 'Falcons', 'Flags', 'Flat', 'Foam', 'Game', 'Giants', 'Gold', 'Green', 'Grey', 'Hats', 'Head', 'Hockey', 'Hook', 'Leather', 'Letters', 'Lids', 'Lions', 'Logos', 'Looks', 'Mesh', 'Multi', 'Neon', 'Nets', 'Nike', 'Orange', 'Panthers', 'Peak', 'Plastic', 'Protect', 'Purple', 'Raiders', 'Ravens', 'Redskins', 'Reebok', 'Seahawks', 'Shade', 'Shield', 'Size', 'Snapbacks', 'Sports', 'Stars', 'Steelers', 'Strap', 'Style', 'Supra', 'Symbols', 'Team', 'Texans', 'Throwback', 'Tisa', 'Twill', 'View', 'Vikings', 'Wear', 'White', 'Wool', 'Yellow', 'Zephyr']

def setLetterList(mode):
    if mode == 1:
        return "kpeelsessionboxesegaarlskillssweleetestseiecmlifnoaedxcaleempsohaloohcserpnreigaslnbcyyshsnoolabmtarbaakcansooliworeeiugeityrlenionegrtlnvgocrucgcstctenaenetinrnerlirabekiccrecatapetesanorbnainvncrclluaupiieuorutlaloyaialmsgaccsnjuotedpyrtsfiayaiaoddvsselisoetnmfriendsnsaheneairiinteractivemagmdfnacdypocotohplscopeeecitllebmilcoelcrichsynisingoknnyadaflahtkemulucirrucdressupsaseselbbubljsenotselim"
    elif mode == 3:
        return "grebellseceipretnecptnemniatretneesriahcroineeeletohtstnpooharatnhsvenecggvattcedapsaitioaenaiyolaocinpttedsrlirtmgteslktnoasesserdaerchvtalioiteeasietnaabieitiounillronitptblrnnesnntouihvoshnmduetggtacmndccnieosaceshoesleeaeesercroisiaeietomnrhlcenoeddrtslsuebetycicovsedoetfssngmnsesewarpelfexcitedytrapvfikafohhruagvusfittingsetbocdateobmrifnocwohsengagedwodocumentscolorsgatsonoitatropsnartailork"
    else: #mode == 2
        return "sdbillscskaepsnlsatspnrurofoamkoohovnoenoeaecopmvipbioeiowxorlnpeclmnlliwtwkcoaitbdrbbaoaorangeillnlsdlogaoncdcardinalsacoltssckesiiisvgfetugreeneskoerdtdhslyasaipcmbrgspraaselashamtataaoeanrsesartgscelnnelurosrmrbdlsatslutwtlttseeetpurplegymhhbstkttheaglesfertoeorootitkcalbrimlestrccoehaseahawksaeyhsskllweauthenticrreiuheoelbatsujdacapslecaytisaaryhpezisutelidshbroncosymbolsetdbengalsniksderavens"

def setWordList(mode):
    return [s.replace(" ", "") for s in map(string.lower, setWordAppearance(mode))]


def compareDist((x,y)):
    column = int(round((x-10)/32))+1
    row = int(round((y-10)/24))+1
    if abs(((column*32)-5) - x) <= 16:
        if abs(((row*24) - y)) <= 16:
            return (column, row)
        else:
            #print "misclick row " + str(abs(((row*24) - y)))
            return (0,0)
    else:
        #print "misclick column " + str(abs(((column*32)-5) - x))
        return (0,0)

def dist((p1,p2),(q1,q2)):
    return math.sqrt(math.pow(p1-q1, 2) + math.pow(p2-q2,2))

def findMin(x, y):
    if x < y:
        return x
    else:
        return y

#Snaps the diagonal lines to either a pure diagonal line or along a vertical/horizontal line (depending on where the mousePosition is)    
def drawDiagonal(pos):
    columnDist = pos[0]
    rowDist = pos[1]
    #Figure out whether row or column is largest (and therefore has the greater impact)
    #Testvalue2 = the horizontal/vertical value
    largest = 0
    if(abs(columnDist) > abs(rowDist)):
        largest = columnDist
        testvalue2 = (largest,0)
    elif (abs(columnDist) < abs(rowDist)):
        largest = rowDist
        testvalue2 = (0, largest)
    else: #They are already on a diagonal
        return (columnDist, rowDist)

    #Find the pure diagonal of the largest of the two from before (depends on the quadrant the diagonal is one
    #Test value = pure diagonal value close to mouse position
    if (rowDist > 0 and columnDist > 0) or (rowDist < 0 and columnDist < 0):
        testvalue1 = (largest, largest)
    elif (rowDist > 0 and columnDist < 0):
        if largest > 0:
            testvalue1 = (-largest, largest)
        else:
            testvalue1 = (largest, -largest)
    else:
        if largest > 0:
            testvalue1 = (largest, -largest)
        else:
            testvalue1 = (-largest, largest)

    #Return either the pure diagonal or pure horizontal, depending on which is closest to the mouse
    result = findMin(dist(testvalue1, pos), dist(testvalue2, pos))
    if result == dist(testvalue1, pos):
        return testvalue1
    else:
        return (testvalue2[1], testvalue2[0])

#Gets the column row position of the diagonal value, relative to the origin
def getDiagonalValue(mousePos, origin, sameSign):
    
    #Get the suggested diagonal line depending on mouse position
    diagonal = drawDiagonal((mousePos[1] - origin[1], mousePos[0]-origin[0]))

    #Trim horiztonal/vertical value passed screen boundary to edge of puzzle
    if (diagonal[0] == 0 and (diagonal[1] + origin[1] > 20 or diagonal[1] + origin[1] < 1)):
        return trimSingleValue(origin)
    elif (diagonal[1] == 0 and (diagonal[0] + origin[0] > 20 or diagonal[0] + origin[0] < 1)):
        return trimSingleValue(origin)

    #If a pure diagonal, decrease/increase the diagonal values by 1 (keeping slope the same) until on the screen:
    elif diagonal[0] == diagonal[1]:
        while (diagonal[0] + origin[0] > 20 or diagonal[1] + origin[1] > 20):
            diagonal = (diagonal[0]-1, diagonal[1]-1)
            
        while (diagonal[0] + origin[0] < 1 or diagonal[1] + origin[1] < 1):
            diagonal = (diagonal[0]+1, diagonal[1]+1)
            
    elif abs(diagonal[0]) == abs(diagonal[1]):
        if (diagonal[0] > 0):
            while origin[0] - diagonal[0] < 1 or origin[1] - diagonal[1] > 20:
                diagonal = (diagonal[0]-1, diagonal[1]+1)
                
        else:
            while origin[0] - diagonal[0] > 20 or origin[1] - diagonal[1] < 1:
                diagonal = (diagonal[0]+1, diagonal[1]-1)
        
    #Return the position of the finished diagonal (dependant on quadrant)    
    if (sameSign):
        if diagonal[0] != 0 and diagonal[1] != 0:
            return (origin[0]-diagonal[0], origin[1]-diagonal[1])
    return (origin[0]+diagonal[0], origin[1]+diagonal[1])

#Adjusts the code to match the pixel values
def convertSingleValue(value):
    return ((value[0]*32)-5, value[1]*24)

#Adjusts a linear line to remain within the bounds
def trimSingleValue(value):
    if value[0] < 1:
        value = (1, value[1])
    elif value[0] > 20:
        value = (20, value[1])
        
    if value[1] < 1:        
        value = (value[0], 1)
    elif value[1] > 20:
        value = (value[0], 20)
    return value

#Returns the letter of puzzle given world Coordinates
def getLetter(puzzle, value):
    try:
        return puzzle[(value[0]-1)+((value[1]-1)*20)].letter
    except IndexError:
        print len(puzzle)
    

#Returns the lowest frequency letter between the two - used to speed up searches
def compareLetterFreq(letter1, letter2):
    wordFreq = {'a': 8.16, 'b': 1.49, 'c': 2.78,'d': 4.25,'e': 12.70, 'f': 2.22,'g': 2.01,'h': 6.09,'i': 6.96,'j': .153,'k': .77,'l': 4.02,'m': 2.40,'n': 6.75, 'o': 7.50, 'p': 1.92, 'q': .09, 'r': 5.98, 's': 6.32, 't': 9.05, 'u': 2.75, 'v': .97, 'w': 2.36, 'x': .15,'y': 1.97,'z': .07}
    if wordFreq[letter1] > wordFreq[letter2]:
        return letter2
    else:
        return letter1
    
#Method to automatically solve the puzzle, given a list of words
def autoSolve(wordList, puzzle, wordsToDraw):
    #List of words to remove
    toRemove = []

    #Iterate over words given to solve
    for x in wordList:

        #Figure out which word is quicker to find
        search = compareLetterFreq(x[0], x[-1])

        #Go through each letter and see if it matches the search
        for y in puzzle:
            if y.letter == search:
                value = checkEightValues(puzzle, y, x, (search != x[0]))

                #Check if value was returned (something was found) and add it to the list of words to remove
                if value[0]:
                    #Values need to be adjusted for display in game world
                    origin = (value[1][0][0]+1, value[1][0][1]+1)
                    final = (value[1][1][0]+1, value[1][1][1]+1)
                    wordsToDraw.append((origin, final))
                    betweenValues(origin, final, puzzle)
                    toRemove.append(x)
                    break
    return toRemove


#Checks the surrounding eight values (if they exist) to see if they match 
def checkEightValues(puzzle, letter, word, reverse):
    for x in range(-2, 1):
        for y in range(-2,1):

            #Ignore the value of the center one (since that's the original letter)
            if x != -1 or y != -1:

                #All possible letters
                possLetter = (letter.position[0]+x, letter.position[1]+y)

                #Check that it is within the bounds
                if possLetter[0] >= 0 and possLetter[0] <= 19 and possLetter[1] >= 0 and possLetter[1] <= 19:

                    #If searching backwards, index goes backwards (from the second back letter). Else go forward from the second letter
                    if reverse:
                        index = len(word)-2
                    else:
                        index = 1

                    #Check along in a straight line
                    found = checkLine(puzzle, (letter.position[0]-1, letter.position[1]-1), possLetter, word, index, reverse)

                    #If something is returned and the first value is true, something was found
                    if found is not None and found[0]:
                        return found
    return (False, False)

#Checks along the puzzle in a straight line until word is found or cannot be word
def checkLine(puzzle, origin, moveAlongLine, word, index, reverse):

    #Find the slope to move along 
    difference = (moveAlongLine[0] - (origin[0]), moveAlongLine[1] - (origin[1]))

    #While the values match
    while puzzle[moveAlongLine[0]+(moveAlongLine[1]*20)].letter == word[index]:

        #If we are searching in reverse, decrease the index. If we have matched until the index has gone beyond the word length, we have found the word
        if reverse:
            index -= 1
            if index < 0:
                return (True, (origin, moveAlongLine))

        #If we are searching forward, increase the index. If we match the length of the word, we have found the word
        else: 
            index += 1
            if index >= len(word):
                return (True, (origin, moveAlongLine))

        #Adjust current position to search and if exceeded puzzle size, finish    
        moveAlongLine = (moveAlongLine[0] + difference[0], moveAlongLine[1]+difference[1])
        if moveAlongLine[0] > 19 or moveAlongLine[0] < 0 or moveAlongLine[1] > 19 or moveAlongLine[1] < 0:
            return (False, False)

#Finds all the values between two points on the grid and increases the number of times hit
def betweenValues(origin, final, puzzle):
    slope = findSlope(origin, final)
    value = origin
    while (value != final):
        puzzle[value[0]-1+((value[1]-1)*20)].timesHit += 1
        value = (value[0] + slope[0], value[1] + slope[1])
    puzzle[final[0]-1+((final[1]-1)*20)].timesHit += 1

#Finds the slope necessary to move from one point to another
def findSlope(origin, final):
    if origin[0] == final[0]:
        if origin[1] > final[1]:
            return (0, -1)
        else:
            return (0, 1)
    elif origin[1] == final[1]:
        if origin[0] > final[0]:
            return (-1, 0)
        else:
            return (1, 0)
    else:
        if origin[1] > final[1] and origin[0] > final[0]:
            return (-1,-1)
        elif origin[1] > final[1] and origin[0] < final[0]:
            return (1, -1)
        elif origin[1] < final[1] and origin[0] > final[0]:
            return (-1, 1)
        else:
            return (1,1)

#Upon finishing a click, method checks if the selected word is an accepted word
def checkWords(puzzle, wordList, wordsToCross, wordsToDraw, word, mouseClick, endValue):
    try:
        chosenWord = ''.join(word)
        reverseWord = ''.join(word)[::-1]
        if chosenWord in wordList:
            wordsToDraw.append((mouseClick, endValue))
            betweenValues(mouseClick, endValue, puzzle)
            wordsToCross.append(wordList.index(chosenWord))
            wordList.remove(chosenWord)

            print chosenWord
        elif reverseWord in wordList:
            wordsToDraw.append((mouseClick, endValue))
            betweenValues(mouseClick, endValue, puzzle)
            wordsToCross.append(wordList.index(reverseWord))
            wordList.remove(reverseWord)
            print reverseWord
        mouseClick = (0,0)
    except TypeError:
        print "Misclick somewhere"
        

#Draws the letters on the screen (and makes them bold if typed)
def drawLettersOnScreen(puzzle, boldWords, screen, showRemaining):
    black = (0,0,0)
    white = (255, 255, 255)
    myfontBold = pygame.font.SysFont("arialblack", 15)
    myfont = pygame.font.SysFont("monospace", 15)
    for x in puzzle:
        try:
            if boldWords[x.letter] or (showRemaining and x.timesHit == 0):
                label = myfontBold.render(x.letter, 1, black, white)
            else:
                label = myfont.render(x.letter, 1, black, white)
            
        except KeyError:
            label = myfont.render(x.letter, 1, black, white)
        screen.blit(label, (x.getPixel()[0]-10, x.getPixel()[1]-10))    

def drawWordsOnScreen(puzzle, screen, wordList):
    black = (0,0,0)
    myfont = pygame.font.SysFont("calibri", 14)
    count = 0
    for y in range(calcWordColumns(wordList)):
        for x in range(20):
            if len(wordList) != 0:
                label = myfont.render(wordList[count], 1, black)
                screen.blit(label, (680+(90*y), 15+(24*x)))
                count += 1
                if count >= len(wordList):
                    return
            else:
                return
            
def calcWordColumns(wordList):
    adjustment = int(len(wordList)/20)
    if int(len(wordList)%20) != 0:
        adjustment += 1
    return adjustment

def setScreenSize(wordList):
    return (680 + (calcWordColumns(wordList) * 90), 500)

def drawLinesOnScreen(wordList, linedWords, screen):
    count = 0
    myfont = pygame.font.SysFont("calibri", 14)
    for x in linedWords:
        pygame.draw.line(screen, (0,0,0), (680+(90*int(x/20)), 20+(24*int(x%20))), (680+(90*int(x/20))+(myfont.size(wordList[x]))[0], 20+(24*int(x%20))))
        
def fillPuzzle(letterList):
    puzzle = []
    puzzleCount = 0 #Iterator for letterList    
    for x in range(1, 21):
        for y in range(1, 21):
            puzzle.append(Grid(y, x, letterList[puzzleCount]))
            puzzleCount += 1
    return puzzle

def findCrossovers(puzzle):
    count = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}
    for y in puzzle:
        count[str(y.timesHit)] += 1
    for x in count:
        print(str(x) + ": " + str(count[x])),
    print ""

def findLenWords(wordList):
    wordLen = {}
    for y in wordList:
        if len(y) in wordLen:
            wordLen[len(y)] += 1
        else:
            wordLen[len(y)] = 0
    for x in wordLen:
        print(str(x) + ": " + str(wordLen[x])),
    print ""

def showStats(puzzle, wordList):
    findCrossovers(puzzle)
    print ""
    findLenWords(wordList)


def filloutPuzzle(puzzle):
    fixed = []
    match = False
    if len(puzzle) != 400:
        for x in range(1,21):
            for y in range(1,21):
                for z in puzzle:
                    if z.x == x and z.y == y:
                        match = True
                        fixed.append(Grid(y,x, z.letter))
                if not match:
                    fixed.append(Grid(y,x, ' '))
                match = False
    return fixed

def checkHorizontal(puzzle, x, firstSection, secondSection):
    if x.x + len(secondSection) < 21 and x.x - len(firstSection) > 0:
        for pos in range(len(firstSection)):
            puzzle.append(Grid(x.y, x.x-len(firstSection)+pos, firstSection[pos]))
        for pos in range(len(secondSection)):
            puzzle.append(Grid(x.y, x.x+1+pos, secondSection[pos]))
        return True 


def placeWord(puzzle, ranking, index):
    for x in puzzle:
        if x.letter in ranking[index]:
            pos = ranking[index].index(x.letter)
            firstSection = ranking[index][:pos]
            secondSection = ranking[index][pos+1:]
            orient = random.randrange(3)
            for _ in xrange(3):
                print orient
                if orient == 0:
                    if firstSection == '' or secondSection == '':
                        print "Easy"
                        #TODO: deal with reverse the string as well
                    else:
                        forward = random.randrange(2)
                        print x.letter
                        if forward == 1:
                            if (checkHorizontal(puzzle, x, firstSection, secondSection)):
                                return True
                            print "Switching because forward = 1"
                            firstSection = firstSection[::-1]
                            secondSection = secondSection[::-1] 
                            if checkHorizontal(puzzle, x, secondSection, firstSection):
                                return True
                        else:
                            print "Switching because forward = 0"
                            firstSection = firstSection[::-1]
                            secondSection = secondSection[::-1]                             
                            if checkHorizontal(puzzle, x, secondSection, firstSection):
                                return True
                            print "Switching again because forward = 0"
                            firstSection = firstSection[::-1]
                            secondSection = secondSection[::-1]
                            if (checkHorizontal(puzzle, x, firstSection, secondSection)):
                                return True                            

                        """ if x.x + len(firstSection) < 21 and x.x - len(secondSection) > 0:
                            for pos in range(len(firstSection)):
                                puzzle.append(Grid(x.y, x.x+1+pos, firstSection[pos]))
                            for pos in range(len(secondSection)):
                                puzzle.append(Grid(x.y, x.x-len(secondSection)+pos, secondSection[pos]))
                            return True"""
                        
 

                            
                        #print x.x
                        #print x.y                    
                if orient == 1:
                    test = 1
                if orient  == 2:
                    test = 0
                
                orient += 1
                orient %= 3
    

def autoGenerate(wordList):
    puzzle = []
    possOrigin = []

    ranking = getWordRanking(wordList)
    
    orient = random.randrange(3)
    forward = random.randrange(2)
    index = 0
    word = ranking[index]
    index += 1

    #Temp debugging values
    index = 2
    orient = 2
    forward = 1
    
    if forward == 1:
        word = word[::-1]

    for x in range(len(word)):
        xvalue = 1
        yvalue = 1
        if orient == 0 or orient == 2:
            yvalue = x+1
        if orient == 1 or orient == 2:
            xvalue = x+1
        puzzle.append(Grid(xvalue, yvalue, word[x]))
    print ranking[index]

    placeWord(puzzle, ranking, index)
    
    return filloutPuzzle(puzzle)

def getWordRanking(wordList):
    
    #Ranking of the word is how difficult it is to place - its length, and the sum of each of the word frequency inverses
    wordFreq = {'a': 8.16, 'b': 1.49, 'c': 2.78,'d': 4.25,'e': 12.70, 'f': 2.22,'g': 2.01,'h': 6.09,'i': 6.96,'j': .153,'k': .77,'l': 4.02,'m': 2.40,'n': 6.75, 'o': 7.50, 'p': 1.92, 'q': .09, 'r': 5.98, 's': 6.32, 't': 9.05, 'u': 2.75, 'v': .97, 'w': 2.36, 'x': .15,'y': 1.97,'z': .07}
    ranking = {}
    for x in wordList:
        sumCount = 0
        for letter in x:
            sumCount += 1/wordFreq[letter]
        sumCount /= len(x)
        sumCount *= .3
        rank = .7 * len(x) + sumCount
        ranking[x] = rank
    sorted_rank = sorted(ranking.iteritems(), key=operator.itemgetter(1), reverse=True)
    returnrank = []
    for x in sorted_rank:
        returnrank.append(x[0])
        
    
    return returnrank
            



#Main run function
def run():
    mode = 1
    wordList = setWordList(mode)
    screen = pygame.display.set_mode(setScreenSize(wordList))
    letterList = setLetterList(mode)   

    boldWords = {}
    for x in string.lowercase[:26]:
        boldWords[x] = False

    puzzle = fillPuzzle(letterList)
    puzzle = autoGenerate(wordList)
    
    wordsToDraw = []
    wordsToCross = []
    clicked = False
    mouseClick = 0
    endValue = (0,0)
    word = []
    
    disableLines = False
    disableCircles = True
    hideLines = False
    autoWin = True
    showWinOnce = False
    showRemaining = False
    scratchLines = True


    while 1:
        screen.fill((255, 255, 255))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] < 15 or pygame.mouse.get_pos()[0] > 640:
                    print "Outside of x range"
                elif pygame.mouse.get_pos()[1] < 15 or pygame.mouse.get_pos()[1] > 482:
                    print "Outside of y range"
                else:
                    (column, row) = compareDist(pygame.mouse.get_pos())
                    if (column,row) != (0,0):
                        clicked = True
                        mouseClick = (column, row)
                        
            if event.type == pygame.MOUSEBUTTONUP:
                checkWords(puzzle, wordList, wordsToCross, wordsToDraw, word, mouseClick, endValue)
                clicked = False
                
            if event.type == pygame.KEYDOWN:
                if event.key > 96 and event.key < 123:
                    boldWords[string.lowercase[event.key-97]] = True
                if event.key == pygame.K_SPACE:
                    hideLines = True
                if event.key == pygame.K_LCTRL:
                    print wordList
                if event.key == pygame.K_RSHIFT:
                    scratchLines = not scratchLines
                    state = 'Enabled Scratch Lines' if scratchLines else 'Disabled Scratch Lines'
                    print state
                if event.key == pygame.K_RCTRL:
                    disableLines = not disableLines
                    state = 'Disabled Lines' if disableCircles else 'Enabled Lines'
                    print state
                if event.key == pygame.K_RALT:
                    disableCircles = not disableCircles
                    state = 'Disabled Circles' if disableCircles else 'Enabled Circles'
                    print state
                if event.key == pygame.K_LSHIFT:
                    showRemaining = True
                if event.key == pygame.K_TAB:
                    showStats(puzzle, wordList)
                if event.key == pygame.K_RETURN:
                    puzzle = autoGenerate(wordList)
                if event.key == pygame.K_LALT:
                    if autoWin:
                        autoWin = False
                        showWinOnce = False
                        remove = autoSolve(wordList, puzzle, wordsToDraw)
                        for x in remove:
                            wordsToCross.append(wordList.index(x))
                        for x in remove:
                            wordList.remove(x)
                    else:
                        autoWin = True
                        wordList = setWordList(mode)
                        wordsToDraw = []
                        wordsToCross = []
                        for y in puzzle:
                            y.timesHit = 0
                if event.key > 47 and event.key < 58:
                    #Num keys pressed
                    mode = event.key - 48
                    letterList = setLetterList(mode)
                    wordList = setWordList(mode)
                    puzzle = fillPuzzle(letterList)
                    screen = pygame.display.set_mode(setScreenSize(wordList))
                    wordsToCross = []
                    wordsToDraw = []
                    if not autoWin:
                        remove = autoSolve(wordList, puzzle, wordsToDraw)
                        for x in remove:
                            wordsToCross.append(wordList.index(x))
                        for x in remove:
                            wordList.remove(x)
                        
                           
            if event.type == pygame.KEYUP:
                if event.key > 96 and event.key < 123:
                    boldWords[string.lowercase[event.key-97]] = False
                if event.key == pygame.K_SPACE:
                    hideLines = False
                if event.key == pygame.K_LSHIFT:
                    showRemaining = False

        drawLettersOnScreen(puzzle, boldWords, screen, showRemaining)

        if scratchLines:
            drawWordsOnScreen(puzzle, screen, setWordAppearance(mode))
            drawLinesOnScreen(setWordAppearance(mode), wordsToCross, screen)
        else:
            drawWordsOnScreen(puzzle, screen, wordList)

        if(clicked):
            word = []
            pos = compareDist(pygame.mouse.get_pos())
            if pos != (0,0):
                endValue = (0,0)
                if pos[1] == mouseClick[1] or pos[0] == mouseClick[0]:
                    endValue = trimSingleValue(pos)
                elif pos[0] - mouseClick[0] < 0:
                    endValue = getDiagonalValue(pos, mouseClick, pos[1] - mouseClick[1] > 0)
                else:
                    endValue = getDiagonalValue(pos,mouseClick, pos[1] - mouseClick[1] < 0)
                
                index = mouseClick
                slope = findSlope(mouseClick, endValue)

                while index != endValue:
                    word.append(getLetter(puzzle, index))
                    index = (index[0] + slope[0], index[1] + slope[1])
                word.append(getLetter(puzzle, endValue))
                
                pygame.draw.line(screen, (0,0,255), convertSingleValue(mouseClick), convertSingleValue(endValue), 2)
                
        if not hideLines and not disableLines: 
            for x in wordsToDraw:
                pygame.draw.line(screen, (0,0,0), convertSingleValue(x[0]), convertSingleValue(x[1]), 1)
        if not disableCircles:
            for y in puzzle:
                if y.timesHit >= 2:
                    pygame.draw.circle(screen, (0, 0, 255), (((y.position[0]*32)-5), y.position[1]*24), 10, 1)
                if y.timesHit >= 3:
                    pygame.draw.circle(screen, (255,0, 0), (((y.position[0]*32)-5), y.position[1]*24), 12, 1)
                if y.timesHit >= 4:
                    pygame.draw.circle(screen, (0, 255, 0), (((y.position[0]*32)-5), y.position[1]*24), 15, 1)
            
        pygame.display.flip()
        if not wordList and not showWinOnce:
            print "You win!"
            showWinOnce = True
            
    

