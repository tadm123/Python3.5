# Program to send mails, type the content in the command line

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys, time

browser = webdriver.Chrome()
browser.get('''
https://sso.fau.edu/login?SAMLRequest=fVLJTsMwEL0j8Q%2BW79kqschqUhU
QohJL1AYO3Fxnklj1Ejx2C39PmoKAA70%2Bv3nLeKazd63IFhxKa3KaxSklYIStpWlz%
2BlzdRpd0VpyeTJFr1bN58J1ZwlsA9GSYNMjGh5wGZ5jlKJEZrgGZF2w1f7hnkzhlvbP
eCqsoWdzkdN1s%2BrXs%2BqbTDYDaqLo1slWbttMCTG%2Bhbmut7IaSl%2B9Yk32sBWKA
hUHPjR%2BgNDuPsjSaXFRpytKMnWWvlJRfTlfSHBoci7U%2BkJDdVVUZlU%2BrahTYyhrc
48DOaWttqyAWVu%2FtS44otwPccIVAyRwRnB8CXluDQYNbgdtKAc%2FL%2B5x23vfIkmS
328U%2FMglPGh5iqEPCBdJiXCsbm7lf%2Bzyem3%2F70uJHeZr8kiq%2BvmvfYnFTWiX
FB5krZXfXDrgfKngXhga31mnu%2F3fL4mxEZB01I5UFgz0I2UioKUmKg%2Bvfuxiu5RM
%3D&RelayState=https%3A%2F%2Fwww.google.com%2Fa%2Ffau.edu%2FServiceLogin
%3Fservice%3Dmail%26passive%3Dtrue%26rm%3Dfalse%26continue%3Dhttps%253A
%252F%252Fmail.google.com%252Fmail%252F%26ss%3D1%26ltmpl%3Ddefault%26ltmpl
cache%3D2%26emr%3D1%26osid%3D1''')

emailElem = browser.find_element_by_id('ContentPlaceHolder1_UsernameTextBox')
emailElem.send_keys('dramir19')
passElem = browser.find_element_by_id('ContentPlaceHolder1_PasswordTextBox')
passElem.send_keys('PartAway39')
passElem.submit()

#time.sleep(5)    #delays time for 5 secs

browser.find_element_by_class_name('T-I-KE').click()
'''delay = 15 # seconds
try:
    WebDriverWait(browser, delay).until(EC.presence_of_element_located(browser.find_element_by_class_name('T-I-KE')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")'''

email= browser.find_element_by_id(':re')
email.send_keys('dramir19@fau.edu')
email.send_keys(Keys.ENTER)
browser.find_element_by_id(':qy').send_keys('Hello')
browser.find_element_by_id(':s2').send_keys(' '.join(sys.argv[1:]))
browser.find_element_by_id(':qo').click()


    


