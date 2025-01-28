from googletrans import Translator
from datetime import datetime
import calendar as cal
from httpcore._exceptions import ConnectError

import time
import sys

start_time = time.time()

translator = Translator()

# to convert date as our intrest
m = datetime.now().month
day = datetime.now().day
month = cal.month_abbr[m]

# name_of_file
name = f"{month}-{day}"   

words_list = []
dictionary = {}
english_word = ''
i = 0

print("* Add Your English Words *\n")

while english_word != "ex":
    english_word = input('>> ').lower()
    
    if english_word != "ex":
        words_list.append(english_word)
        
def simple_loading_bar(total_steps=len(words_list), bar_length=18, fill_char='=', empty_char=' '):
    for step in range(total_steps + 1):
        # Calculate the number of filled and empty characters
        filled_length = int(bar_length * step // total_steps)
        empty_length = bar_length - filled_length

        # Create the bar string
        bar = fill_char * filled_length + empty_char * empty_length

        # Print the bar with a percentage
        percent = (step / total_steps) * 100
        print(f'\r[{bar}] {int(percent)}%', end='')

        time.sleep(0.475)

    print()
    

total_steps = 100
simple_loading_bar(total_steps)

try:
    for word in words_list:
        mean = translator.translate(word, src='en', dest='fa').text
        dictionary[word] = mean
        
except ConnectError as ce:
    print('Unable to Connect the Internet !')   

    
for key, value in dictionary.items():
    content = f"{key} : {value}"
    with open(f'{name}.md', 'a+', encoding='utf-8') as file:
        file.write(f"{content.strip()}\n")










# print("--- %s seconds ---" % (time.time() - start_time))
