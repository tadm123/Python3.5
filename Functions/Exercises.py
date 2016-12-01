# ThinkPy - Exercises
# http://greenteapress.com/thinkpython2/html/thinkpython2004.html

#Write a function called nested_sum that takes a list of lists of integers
#and adds up the elements from all of the nested lists. 

def nested_sum(t):
        sum=0
        for i in t:
                for j in i:
                        sum= sum+j
        return sum

t = [[1, 2], [3], [4, 5, 6]]
print(str(nested_sum(t)))


#Write a function called cumsum that takes a list of numbers and
#returns the cumulative sum; that is, a new list where the ith element
#is the sum of the first i+1 elements from the original list.

def cumsum(t):
        for i in range(1,len(t)):
                t[i]= t[i]+t[i-1]
	return t

t = [1, 2, 3]
print(str(cumsum(t))


#Write a function called middle that takes a list and returns a
#new list that contains all but the first and last elements.

def middle(t):
      return t[1:-1]

t = [1, 2, 3, 4]
print(middle(t))


#Write a function called chop that takes a list, modifies it by removing
#the first and last elements, and returns None.

def chop(t):
	del t[0]
	del t[-1]

type(chop(t))
print(t)


#Write a function called is_sorted that takes a list as a parameter and
#returns True if the list is sorted in ascending order and False otherwise.

def is_sorted(s):
      if s == sorted(s):                       #note you can't do s1== s1.sort() because s1.sort() returns None
              return True                       #type(s1) -> list    type(s1.sort()) -> None
      else:
              return False

#Two words are anagrams if you can rearrange the letters from one to spell the other.
#Write a function called is_anagram that takes two strings and returns True if they are
#anagrams.
      
def is_anagram(s1,s2):
      if s1 == s2[::-1]:
              return True
      return False


#Write a function called has_duplicates that takes a list and returns True if there is any
#element that appears more than once. It should not modify the original list.



s='Hello there'


def has_duplicates(s):
        count=0
        for letter in s:        #letter ='H'
                for i in range(len(s)):         #compares 'H' to  'H','e','l','l'...
                        if letter == s[i]:
                                count += 1      #increases counter
                        if count == 2:          #if two (word is repeated twice)
                                return True
                count=0
        return False
                      
        

  

