class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        sortCar = []
        answer = 0

        for index in range(len(position)):
            sortCar.append([position[index], speed[index]])

        sortCar.sort(key=lambda x: x[0], reverse=True)

        stack = []

        for car in sortCar:
            distanceLeft = target - car[0]
            targetDist = distanceLeft / car[1]

            if not stack or targetDist > stack[-1]:
                answer += 1
                stack.append(targetDist)

        return answer