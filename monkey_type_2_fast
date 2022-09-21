#this is a python program that uses the safari webdriver that is built-in on Mac to automate the typing tests on monkeytype.com

#required package: selenium

#imports
import selenium.common.exceptions
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#opening safari window and getting to monkeytype
driver = webdriver.Safari()
driver.set_window_size(1200, 700)
driver.get("https://monkeytype.com")

#pressing accept on the accept/decline cookies prompt
time.sleep(1)
accept_cookies = driver.find_element(by = By.XPATH, value = '//*[@id="cookiePopup"]/div[2]/div[2]/div[1]')
accept_cookies.click()
time.sleep(1)

#getting the typing test element
typing_test = driver.find_element(by = By.XPATH, value = '//*[@id="typingTest"]')

#function to load a new section of words after the first one has been completed and return the words as a list
def load_new_words(old_word_list):
    word_elems = driver.find_elements(by = By.CLASS_NAME, value = "word") #getting next section of words as elements from the webpage

    #adding items from the word_elems as strings to a new word list
    new_word_list = []
    for word in word_elems:
        new_word_list.append(word.text)

    #if the old word list was not empty this removes parts of the new list that have been loaded in parts of the old list. it does so by reversing the lists and checking if 4 consecutive words from the new word list are equal to the last 4 words of the old word list. if such consecutives words are found, then the program decides that a part of the old word list has been loaded and returns the new word list without the items of the old one that were loaded
    if old_word_list != []:
        for index, word in enumerate(reversed(new_word_list)):
            if word == list(reversed(old_word_list))[0]:
                for i in range(1, 5):
                    if i == 4:
                        return new_word_list[len(new_word_list) - index:]
                    if list(reversed(new_word_list))[index + i] == list(reversed(old_word_list))[i]:
                        continue
                    else:
                        break
    return new_word_list

#function for typing words taking a list of words as a parameter
def type_words(word_list):
    section = " ".join(word_list) #joining all the words from a list together to create a large string for the whole section of words

    #try/except statement so that if the typing test is over, the error of not being able to type any more is caught and the program stops running
    try:
        typing_test.send_keys(section)
        typing_test.send_keys(" ")
    except selenium.common.exceptions.ElementNotInteractableException:
        exit()

old_word_list = [] #keeping track of the last section of words to help with ensuring no parts of it are loaded again

#while loop that constantly loads and types out new sections of words
while True:
    word_list = load_new_words(old_word_list)

    #printing a list of each word in a section
    for w in word_list:
        print(w)
    print("======================\nNew Section\n======================")

    type_words(word_list) #typing a list of words in a section
    old_word_list = word_list #setting the current old section of words as the old one after typing it all
