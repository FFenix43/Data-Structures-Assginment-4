# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!
'''
3. Remove Duplicates (Keep Order)
Return the values in the order they first appeared, without duplicates.
Input: ["apple", "banana", "apple", "kiwi", "banana"]
Output: ["apple", "banana", "kiwi"]
'''

def remove_duplicates(values):
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result    

values = ["apple", "banana", "apple", "kiwi", "banana"]
print(f"This are the duplicate values {values}\n")
print("And this are the values without the duplicates:")
print(remove_duplicates(values))


'''
The structure I chose to answer this question was a combination of a “set” and  a “list”, since it seemed best for handling an input of various values and then iterating throught the list to create a new list without the previous seen values.
While maintaining the order of the values, considering that a set does not maintain an order for its values. Furthermore, it was the quickest and most efficient way to resolve the issue. The code iterates through the list, checks for duplicates, and removes any found. The time limit shaped my decision under the pressure of the clock, and it helped because, once I read the question, I knew the set's structure was what would be required to complete the task. 
As a trade off, I chose speed and clear code structure over memory efficiency, by maintaining both a set and a list in memory simultaneously. Storing the elements in both a set, for duplicates results, and a list, to maintain order in the values, consumes additional space, but under the pressure of the clock, I thought that is a trade off I was willing to make to have a working code.

'''