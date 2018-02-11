Hours=float(input('Enter Hours: '))
Rate=float(input('Enter Rate: '))

if Hours > 40:
    Pay = Hours * Rate +(Hours - 40) * Rate *0.5
else:
    Pay = Hours * Rate
print('Pay: ', Pay)


try: 
    Hours=float(input('Enter Hours: '))
    Rate=float(input('Enter Rate: '))
except:
    print('Error, please enter numeric input')
    quit()
if Hours > 40:
            Pay = Hours * Rate +(Hours - 40) * Rate *0.5
else:
    Pay = Hours * Rate
print('Pay: ', Pay)


try:
    score = float(input('Enter a score between 0.0 and 1.0: '))
    if score >=0.0 and score <=1.0:
        pass
    else:
        print('Score out of range, enter a numerical value between 0.0 and 1.0')
        quit()
except:
    print('Please enter a numerical value')
    quit()
if score >=0.9:
    print('Grade: A')
elif score >= 0.8:
    print('Grade: B')
elif score >= 0.7:
    print('Grade: C')    
elif score >= 0.6:
    print('Grade: D')
elif score < 0.6:
    print('Grade: F')
    
    
def computepay(Hours,Rate):
if Hours > 40:
    Pay = Hours * Rate +(Hours - 40) * Rate *0.5
else:
    Pay = Hours * Rate
    return Pay

Hours=float(input('Enter Hours: '))
Rate=float(input('Enter Rate: '))

total = computepay(Hours,Rate)    
print(total)


def computegrade (score):
    if score >=0.9:
        print('Grade: A')
    elif score >= 0.8:
        print('Grade: B')
    elif score >= 0.7:
        print('Grade: C')    
    elif score >= 0.6:
        print('Grade: D')
    elif score < 0.6:
        print('Grade: F')
try:
    grade= float(input('Enter a score between 0.0 and 1.0: '))
    if grade >=0.0 and grade <=1.0:
        computegrade(grade)
    else:
        print('Bad Score')
except:
    print('Bad Score')
    quit()
    
    
count = 0
total = 0
while True:
    line = input('Enter a number: ')
    if line == 'done':
        break
    try:
        x = float(line)
    except:
        print('Enter a numerical value')
        continue
    count = count + 1
    total = total + x
print(total, count, total/count)


largest = None
smallest = None
while True:
    line = input('Enter a number: ')
    if line == 'done':
        break
    try:
        x = float(line)
    except:
        print('Enter a numerical value')
        continue
    if smallest is None or x < smallest:
        smallest = x
    if largest is None or x > largest:
        largest = x
print(largest, smallest)

fruit = 'kumquat'
index = len(fruit)-1
while index >= 0:
    letter = fruit[index]
    print(letter)
    index = index - 1
fruit = 'kumquat'



string = 'X-DSPAM-Confidence:0.8475'
colon = string.find(':')
number = float(string[colon+1:])
print(number)


fname = input('Enter the file name: ')
fhand = open(fname)
for line in fhand:
    line =line.strip()
    print(line.upper())
    
    
    
fname = input('Enter the file name: ')
fhand = open(fname)
total = 0.0
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        line = float(line[20:])
        total = total + line
        count = count + 1
print('Average spam confidence: ', total/count)

fname = input ('Enter the file name: ')
count = 0
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print('NA NA BOO BOO TO YOU - You have been punked!')
    else:
        print('File name cannot be opened: ', fname)
    quit()
for line in fhand:
    if line.startswith('Subject:'):
        count = count +1
print('There were' , count, 'subject lines in' , fname)




def count (w,l):
    total = 0
    for letter in w:
        if letter == 1:
            total = total + 1
    return total
    
word = input('Search words: ')
letter = input('Search letter: ')
answer = count(word,letter)
print(answer)

def chop(t):
    del t[0]
    del t[len(t)-1]

fruit = ['apple ', 'banana ', 'cucumber ', 'dragonfruit ']
chop(fruit)
print(fruit)


def middle(t):
    return t[1:len(t)-1]
    
fruit = ['apple ', 'banana ', 'cucumber ', 'dragonfruit ']
rest = middle(fruit)
print(rest)
print(fruit)


fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print('File not found')
    quit()
else:
    count = 0
    for line in fhand:
        words = line.split()
        if len(words) == 0 : continue
        if words[0] != 'From' : continue
        print(words[2])
        
        
        fname = 'mbox-short.txt'
try:
    fhand = open(fname)
except:
    print('File not found')
    quit()
else:
    count = 0
    for line in fhand:
        words = line.split()
        if not len(words) == 0 and words[0] == 'From' : print(words[2])
        
        
        fname = input('Enter a file name: ')
try:
    fhand = open(fname)
except:
    print('File not found')
    quit()
else:
    count = 0
    for line in fhand:
        words = line.split()
        if not len(words) == 0 and words[0] == 'From' : 
            print(words[1])
            count = count + 1
print('There were', count, 'lines in the file with From as the first word.')

list =[]
while True:
    line = input('Enter a number: ')
    if line == 'done':
        break
    try:
        x = float(line)
    except:
        print('Enter a numerical value')
        continue
    t = list.append(x)
print(list)
print('Maximum: ', max(list))
print('Minimum: ', min(list))