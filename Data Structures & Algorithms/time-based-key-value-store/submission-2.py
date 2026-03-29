class TimeMap:

    def __init__(self):
        self.nameToMood = {} # key: name, value: [mood,timeStamp]

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # this function will set the name to mood
        if key not in self.nameToMood:
            self.nameToMood[key] = []

        self.nameToMood[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        # we have to get the the most recent value
        # get the value which is on that timestamp.
        # if value not there, get the most recent

        #if there is no value, "" return empty string

        if key not in self.nameToMood:
            return ""

        else:
            leftPointer = 0
            # mood is a list [mood, timestamp]
            moods = self.nameToMood[key]
            rightPointer = len(moods) - 1
            result = ""
            while leftPointer <= rightPointer:
                middle = (leftPointer + rightPointer) // 2

                if timestamp == moods[middle][1]:
                    return moods[middle][0]

                elif moods[middle][1] > timestamp:
                    rightPointer = middle - 1
                
                elif moods[middle][1] < timestamp:
                    result = moods[middle][0]
                    leftPointer = middle + 1
            
            return result

        
