# Riley Ahlrichs        3-29-2025
# Lab Week 10: This program generates a list of random integers and calculates the mean and median of the list.
import random

def generateInput():
    # Generate a random length between 200 and 500
    length = random.randint(200, 500)
    # Generate a list of random integers between 1 and 2000
    random_list = [random.randint(1, 2000) for _ in range(length)]
    return random_list

def findMean(numbers):
    # The mean refers to the number you obtain when you sum up a given set of numbers and then divide this sum by the total number in the set
    # CITATION URL: https://www.wyzant.com/resources/lessons/math/statistics_and_probability/averages/
    total = 0
    count = len(numbers)
    for num in numbers:
        total += num  # Sum the values manually
    
    mean = total / count
    return mean

def findMedian(numbers):
    # the number in the middle of a given set of numbers arranged in order of increasing magnitude. When given a set of numbers, 
    # the median is the number positioned in the exact middle of the list when you arrange the numbers from
    # the lowest to the highest. The median is also a measure of average.
    # CITATION URL: https://www.wyzant.com/resources/lessons/math/statistics_and_probability/averages/
    
    numbers.sort()  # Sort the list first
    
    length = len(numbers)
    if length % 2 == 1:
        # Odd length: median is the middle element
        median = numbers[length // 2]
    else:
        # Even length: median is the average of the two middle elements
        middle1 = numbers[length // 2 - 1]
        middle2 = numbers[length // 2]
        median = (middle1 + middle2) / 2
    
    return median

def main():
    # Step 1: Generate the list of random numbers
    random_list = generateInput()
    
    # Step 2: Calculate the mean and median of the list
    mean = findMean(random_list)
    median = findMedian(random_list)
    
    # Step 3: Print the results
    print(f"Mean: {mean} Median: {median}")


if __name__ == "__main__":
    main()