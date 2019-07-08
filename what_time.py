'''
[Hard] – What Time is It? (3 points)

Given the time in numbers, output the time in text. This is using 24 hour time (0:00 – 23:59). Input: string, output: string.

Test Cases:

timeString("00:00") => "It's twelve am"
timeString("01:30") => "It's one thirty am"
timeString("12:05") => "It's twelve o five pm"
timeString("14:01") => "It's two o one pm"
timeString("20:29") => "It's eight twenty nine pm"
timeString("21:00") => "It's nine pm"

'''

# global variables
hour = ''
minute = ''
ampm = ''

hour_times = {
    '00': 'twelve',
    '01': 'one',
    '02': 'two',
    '03': 'three',
    '04': 'four',
    '05': 'five',
    '06': 'six',
    '07': 'seven',
    '08': 'eight',
    '09': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'one',
    '14': 'two',
    '15': 'three',
    '16': 'four',
    '17': 'five',
    '18': 'six',
    '19': 'seven',
    '20': 'eight',
    '21': 'nine',
    '22': 'ten',
    '23': 'eleven',

}

less_than_twenty = {
        '00': '',
        '01': 'one',
        '02': 'two',
        '03': 'three',
        '04': 'four',
        '05': 'five',
        '06': 'six',
        '07': 'seven',
        '08': 'eight',
        '09': 'nine',
        '10': 'ten',
        '11': 'eleven',
        '12': 'twelve',
        '13': 'thirteen',
        '14': 'fourteen',
        '15': 'fifteen',
        '16': 'sixteen',
        '17': 'seventeen',
        '18': 'eighteen',
        '19': 'nineteen',
        
    } 
   
   # The first two strings are blank to make indexing easy  
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'] 


def buildTimeString():
    print('It\'s ' + str(hour) + ' ' + str(minute) + str(ampm))

def setHourAMPM(first_half):
    global hour
    global ampm
    #sets hour to string equivalent
    for key in hour_times:
        if first_half == key:
            hour = hour_times.get(key)

            #sets am/pm whether before or after noon
            if (int(first_half) > 11):
                ampm = 'pm'
            else:
                ampm = 'am'
            break

    

def setMinute(second_half):
    global minute

    #sets minute value for minutes less than 20
    #if less than 10 adds 'o' before the singles number
    for key in less_than_twenty:
        if second_half == key:
            if second_half[0] == '0' and second_half[1] != '0':
                minute = 'o ' + less_than_twenty.get(key) +' '
                break
            else:
                minute = less_than_twenty.get(key)
                break
    

    #adds tens string with singles string for value greater than 19
    if second_half not in less_than_twenty:
        minute = str(tens[int(second_half[0])]) + ' ' + str(less_than_twenty.get('0' + second_half[1]) + ' ')
        
    
#repeats until 'exit' is typed
while True:
    time_string = input('Type time string here (XX:XX) or \'exit\' to stop: ')

    if time_string == 'exit':
        break

    hour = ''
    minute = ''
    ampm = ''

    setHourAMPM(time_string[:2])
    setMinute(time_string[3:])
    buildTimeString()



    

    


