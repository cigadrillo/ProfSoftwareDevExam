import random

#First commit
#Second commit

class randoms:

    def randomNumbers(amount, minRange, maxRange):
        amountFunc = amount
        randList = []

        assert minRange > 0, "Only positive numbers accepted."
        assert maxRange > minRange, "The maximum must be higher than the minimum."

        while amountFunc:
            randomNumber = random.randint(minRange, maxRange)
            randList.append(randomNumber)
            amountFunc -= 1


        assert len(randList) == amount, "The function did not return the amount of numbers requested."

        return randList


randoms1 = randoms
randoms1 = randoms1.randomNumbers(3, 5, 300)
print(randoms1)




