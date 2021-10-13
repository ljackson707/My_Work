## How to use the Gathi Resume Analyzer

Download the necessary packages in terminal: 

pip install pandas 
pip install numpy
pip install textract
pip install os
pip install re

(may need to use pip3 instead of pip to install packages.)

To import file with all necessary functions use:
from si_final import *

Run the get_dir() function first to get a list of the files within your assigned directory.

# In order for this program to work you must copy the list of files returned by the get_dir() function and paste them into the si_final.py file under the variable asignment named files, then save the si_final.py file and restart your terminal/notebook and continue to run all other functions.

# list of functions available: 
get_names() 
get_roles()
get_skills()
get_education()
get_certification()
get_tech_exp() 
get_nontech_exp()
get_skill_inventory() "This function takes in all the above functions and concats each padnas data frame into a single data frame that is exportes as an .xlsx file to a new directory on your computer. 

