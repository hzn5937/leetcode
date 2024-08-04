# 424. Longest Repeating Character Replacement

# Description
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

def characterReplacement(string, k):
    # A dictionary to store the count of each character in the string
    count = {}
    # A variable to store the major character count in the string (used to calculate the number of minor character count in the window)
    majorCharacterCount = 0
    # A variable to keep track of the start of the window
    left = 0
    
    # Initially the window size is 0
    for right in range(len(string)):
        # Increment the count of the character at the right end of window
        count[string[right]] = count.get(string[right], 0) + 1
        # Update the major character count
        majorCharacterCount = max(majorCharacterCount, count[string[right]])
        
        # WindowSize = right - left + 1 (which will be increased by 1 in each iteration)
        windowSize = right - left + 1
        # minorCharacterCount = window size - major character count
        minorCharacterCount = windowSize - majorCharacterCount 
        
        # After expanding the window, if the minorCharacterCount is greater than k, shrink the left side of the window 
        # In short, window expansion can only be accepted if the minorCharacterCount is less than or equal to k
        if (minorCharacterCount > k):
            count[string[left]] -= 1
            left += 1
            
    return windowSize

""" 
Explaination:
    - Window Sliding technique always need an left index and right index to keep track of the size of the window
    - In this problem, the windowSize is the longest substring after k replacements
    - After expanding the windowSize:
        if (minorCharacterCount > k): shrink the left side of the window (this make the windowSize stay unchanged after an iteration, but the window slide to the right)
        else: windowSize expansion is accepted

"""