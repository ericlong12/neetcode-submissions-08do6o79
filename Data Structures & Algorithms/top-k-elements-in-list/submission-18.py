class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # read the amount each integer shows up
        # 3 shows up three times
        # 2 shows up two times

        # dictionary. key: amount of times shown up. value: the number showing up

        # the dictionary will be size k, list dictionary

        # we make a dictionary of length nums
        count = {index: [] for index in range(len(nums) + 1)}


        # find out how we know 3 showed up 3 times
        dictionaryCounter = defaultdict(int)
        for number in nums:
            dictionaryCounter[number] += 1

        # the count is the value, the number is the amount of occurances.

        for number, freq in dictionaryCounter.items():
            count[freq].append(number)

        answer = []

        for index in range(len(nums), -1, -1):
            for number in count[index]:
                answer.append(number)

                if len(answer) == k:
                    return answer

        





