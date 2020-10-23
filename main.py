'''

    - The program finds suitable time slots
    if the desired meting time provided.

    - It can took 2 lists which contains
    available times of persons.

    - !! Lists are created manually.

    Usage:

    Think that 2 lists which already shown below are holds persons available time space.

    Person1 = [["09:00", "22:00"]]
    Person2 = [["09:00","11:00"], ["12:30", "14:30"], ["14:30","15:30"], ["16:00", "17:00"]]
    
    Person1 is available between 9:00 and 22:00
    Person2 is available between 9:00 and 11:00, 12:30 and 14:30, ...

    The program will return this:
    [['09:00', '11:00'], ['12:30', '14:30'], ['14:30', '15:30'], ['16:00', '17:00']]
    Person1 and Person2 can meet between these times.

'''

# type should be minute
desiredMinimumMeetingTime = 30


def GetBiggerOne(minute1, minute2):

    if (minute1 > minute2): return minute1
    else: return minute2

def GetLowerOne(minute1, minute2):
    
    if (minute1 < minute2): return minute1
    else: return minute2

def EnsureDesiredMeetingTime(time1, time2):

    # example format for time1 = ["10:00", "12:00"]
    # example format for time2 = ["10:30", "11:45"]
    a = 5

def CompareValue(value, value2):

    if (value > value2): return 1
    elif (value < value2): return -1
    else: return 0


# A function that created for pleasure.
# When the hour returns as a digit
# the function adds zero in front of the <string>.
# otherwise (non a digit) return string.
# example usage:
# input = '9', output = '09'
def handsomeHour(value):

    DivisionFirst = str(int(int(value[0]) / 60))
    ReminderFirst = str(int(int(value[0]) % 60))

    DivisionSecond = str(int(int(value[1]) / 60))
    RemainderSecond = str(int(int(value[1]) % 60))

    if (len(DivisionFirst) < 2): DivisionFirst = ''.join('0' + DivisionFirst)
    if (len(ReminderFirst) < 2): ReminderFirst = ''.join('0' + ReminderFirst)

    if (len(DivisionSecond) < 2): DivisionSecond = ''.join('0' + DivisionSecond)
    if (len(RemainderSecond) < 2): RemainderSecond = ''.join('0' + RemainderSecond)

    return [DivisionFirst + ":" + ReminderFirst, DivisionSecond + ":" + RemainderSecond]

def ConvertMinuteToHour(value):

    lenVal = len(value)
    indexVal = 0

    while (indexVal < lenVal):

        value[indexVal] = handsomeHour(value[indexVal])
        indexVal += 1
    return value

def ConvertHourToMinute(P1, P2):

    indexP1 = 0
    indexP2 = 0

    lenP1 = len(P1)
    lenP2 = len(P2)

    while ((indexP1 < lenP1) or (indexP2 < lenP2)):

        if (indexP1 < lenP1):
            butterfly = P1[indexP1][0].split(":")
            P1[indexP1][0] = int(butterfly[0]) * 60 + int(butterfly[1])

            butterfly = P1[indexP1][1].split(":")
            P1[indexP1][1] = int(butterfly[0]) * 60 + int(butterfly[1])
            indexP1 += 1

        if (indexP2 < lenP2):
            butterfly = P2[indexP2][0].split(":")
            P2[indexP2][0] = int(butterfly[0]) * 60 + int(butterfly[1])

            butterfly = P2[indexP2][1].split(":")
            P2[indexP2][1] = int(butterfly[0]) * 60 + int(butterfly[1])
            indexP2 += 1
    return P1, P2

def AvailableTime(P1, P2):


    returnIndexP1 = 0
    indexP1 = 0
    indexP2 = 0
    bookedTime = list()
    lenP1 = len(P1)
    lenP2 = len(P2)

    while (indexP1 < lenP1 and indexP2 < lenP2):

        startMinute1, endMinute1 = P1[indexP1][0], P1[indexP1][1]
        startMinute2, endMinute2 = P2[indexP2][0], P2[indexP2][1]

        answerCompareValue = CompareValue(startMinute1, startMinute2)
        #print("firstCompare: {} - {}" .format(startMinute1, startMinute2))

        #print("WHILE")
        if (answerCompareValue == 1):

            #print("FIRST - FIRST IF YES")

            #print("secondCompare: {} - {}" .format(startMinute1, endMinute2))
            if (CompareValue(startMinute1, endMinute2) <= 0):

                #print("FIRST - SECOND IF YES")
                # HERE WE GO.
                # PERSON1 AVAILABLE MINUTE START MUST BE BETWEEN
                # PERSON2 AVAILABLE MINUTE START AND END.
                startTime = GetBiggerOne(startMinute1, startMinute2)
                endTime = GetLowerOne(endMinute1, endMinute2)

                if (endTime - startTime >= desiredMinimumMeetingTime):
                    bookedTime.append([startTime, endTime])
                    
                    returnIndexP1 = indexP1


                    #print("FIRST - THIRD IF YES\n\n")
        elif (answerCompareValue == -1):
            #print("SECOND - FIRST IF YES")
            
            #print("secondCompare: {} - {}" .format(endMinute1, startMinute2))
            if (CompareValue(endMinute1, startMinute2) >= 0):
                #print("SECOND - SECOND IF YES")

                # HERE WE GO.
                # PERSON1 AVAILABLE MINUTE START MUST BE BETWEEN
                # PERSON2 AVAILABLE MINUTE START AND END.
                startTime = GetBiggerOne(startMinute1, startMinute2)
                endTime = GetLowerOne(endMinute1, endMinute2)

                if (endTime - startTime >= desiredMinimumMeetingTime):
                    bookedTime.append([startTime, endTime])

                    returnIndexP1 = indexP1


                    #print("SECOND - THIRD IF YES\n\n")
        else:

            #print("LAST ELSE EQUALS")
            # the available begining time of both person must be same
            if (abs(endMinute1 - endMinute2) >= desiredMinimumMeetingTime):

                #print("DONE")
                startTime = GetBiggerOne(startMinute1, startMinute2)
                endTime = GetLowerOne(endMinute1, endMinute2)

                bookedTime.append([startTime, endTime])
        
        indexP1 += 1

        if (indexP1 >= lenP1 and indexP2 < lenP2):

            #print("\n\nENTERED INDEX DEGREASE IF\n\n")
            indexP1 = returnIndexP1
            indexP2 += 1

    return bookedTime


# two schedule should be created. (Schedules can takes as input)
def createSchedule():

    Person1 = [["9:00","10:30"],["12:00", "13:00"], ["16:00", "18:00"]]
    #Person1 = [["09:00", "22:00"]]
    Person2 = [["10:00","11:30"], ["12:30", "14:30"], ["14:30","15:30"], ["16:00", "17:00"]]
    return Person1,Person2

# managing of main function
def handleMain():

    Person1, Person2 = createSchedule()
    Person1, Person2 = ConvertHourToMinute(Person1, Person2)
    
    availableMeetingTimes = AvailableTime(Person1, Person2)
    ConvertMinuteToHour(availableMeetingTimes)
    print(availableMeetingTimes)


def main():

    handleMain()


if __name__ == "__main__":
    main()