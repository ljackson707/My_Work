import pandas as pd
import numpy as np 
import textract
import os
import re
#------------------------------------------------------------------
def get_dir():
    """
    ** USE THIS FUNCTION FIRST TO FILL OUT THE FILES **
    
    This function will ask the user for a directory path
    Uses for loop to iterate through the .docx files withint the
    specified directory.
    If the files end in .docx then it will return the directory
    in list format for each file.
    """
    global files_list 
    files_list = []
    # assign directory
    directory = input("Please enter a directory: ")
    # iterate over files in that directory
    for filename in os.listdir(directory):
        if filename.endswith(".docx"):
            file = os.path.join(directory, filename)
            files_list.append(file)
    return(files_list)

#------------------------------------------------------------------

def get_names():
    """
    This function finda all the names within each resume
    within the directory.
    Uses empty list called name_list then uses for loop to 
    iterate through each .docx file within the directory.
    Decodes the each reusme into a UTF-8 (str) format.
    Uses regex to find all capitalized full names.
    Captures the first occurance of the match with regex
    appends the each full name to the empty list name_list
    uses for loop to turn the list into a pandas dataframe
    returns pandas data frame named names.
    
    """
    name_list = []
    for f in files_list:
        res = textract.process(f)
        resume = res.decode('UTF-8')
        fn = re.findall(r'[A-Z]+\s\w[A-Z]+', resume)
        full_name = fn[0]
        name_list.append(full_name)
        names = pd.DataFrame(columns=['employee_name'])
        for name in name_list: 
            names = names.append(pd.DataFrame({'employee_name': name}, index=[0]), ignore_index=True)
    return names

#------------------------------------------------------------------

def get_skills():
    """
    This function creates two empty lists, skill_list and skills_list
    uses a for loop to convert the resumes into str format
    then finds all words after the word SKILLS
    set end position to be 3 newline charecters and a capital C.
    appends the captured text into the skill list
    uses another forloop on the new list to splitlines between each newline
    joins on ' ' for each element witin the skills
    appends new list to skills_list
    creates pandas data frame from skills_list
    returns skills as a pd dataframe
    
    """
    skill_list = []
    skills_list = []
    for f in files_list:
        res = textract.process(f)
        resume = res.decode('UTF-8')
        start = resume.find('SKILLS') + 6
        end = resume.find('\n\n\nC', start)
        skills = resume[start:end]
        skill_list.append(skills)

        for string in skill_list:
            skills = string.splitlines()
            skills = ' '.join([str(elem) for elem in skills])
        skills_list.append(skills)
        skills = pd.DataFrame(columns=['primary_skill_set'])
        for strings in skills_list: 
            skills = skills.append(pd.DataFrame({'primary_skill_set': strings}, index=[0]), ignore_index=True)
    return skills

#------------------------------------------------------------------

def get_education():
    """
    This function creates two empty lists, education_list and educ_list
    uses a for loop to convert the resumes into str format
    then finds all words after the the charecters EDU
    set end position to be 2 newline charecters and a TECH.
    appends the captured text into the education_list
    uses another forloop on the new list to splitlines between each newline
    joins on ' ' for each element witin the educ
    appends new list to educ_list
    creates pandas data frame from educ_list
    returns education as a pd dataframe

    """
    education_list = []
    educ_list = []
    for f in files_list:
        res = textract.process(f)
        resume = res.decode('UTF-8')
        start = resume.find('EDU') + 9
        end = resume.find('\n\nTECH', start)
        edu= resume[start:end]
        education_list.append(edu)

        for string in education_list:
            educ = string.splitlines()
            educ = ' '.join([str(elem) for elem in educ])
        educ_list.append(educ)
        education = pd.DataFrame(columns=['education_qualification'])
        for strings in educ_list: 
            education = education.append(pd.DataFrame({'education_qualification': strings}, index=[0]), ignore_index=True)
    return education

#------------------------------------------------------------------

def get_certification(): 
    """
    This function creates two empty lists, Cert_list and Certs_list
    uses a for loop to convert the resumes into str format
    then finds all words after the the charecters CERTIFICATIONS
    set end position to be 5 newline charecters
    appends the captured text into the Cert_list
    uses another for loop on the new list to splitlines between each newline
    joins on ' ' for each element witin the certifications
    appends new list to Certs_list
    creates pandas data frame from Certs_list
    returns certifications as a pd dataframe
    
    """
    Cert_list = []
    Certs_list = []
    for f in files_list:
        res = textract.process(f)
        resume = res.decode('UTF-8')
        start = resume.find('CERTIFICATIONS') + 16
        end = resume.find('\n\n\n\n\n', start)
        Certs = resume[start:end]
        Cert_list.append(Certs)

        for string in Cert_list:
            Certification = string.splitlines()
            Certification = ' '.join([str(elem) for elem in Certification])
        Certs_list.append(Certification)
        certifications = pd.DataFrame(columns=['certifications'])
        for strings in Certs_list: 
            certifications = certifications.append(pd.DataFrame({'certifications': strings}, index=[0]), ignore_index=True)
    return certifications

#------------------------------------------------------------------

def get_roles():  
    """
    This function creates two empty lists, role_list and roles_list
    uses a for loop to convert the resumes into str format
    then finds all words after the the charecters TITLE
    set end position to be 3 newline charecters
    appends the captured text into the role_list
    uses another forloop on the new list to splitlines between each newline
    joins on ' ' for each element witin the roles
    appends new list to roles_list
    creates pandas data frame from roles_list
    returns roles as a pd dataframe
    
    """
    role_list = []
    roles_list = []
    for f in files_list:
        res = textract.process(f)
        resume = res.decode('UTF-8')
        start = resume.find('TITLE') + 7
        end = resume.find('\n\n\n', start)
        role = resume[start:end]
        role_list.append(role)

        for string in role_list:
            roles = string.splitlines()
            roles = ' '.join([str(elem) for elem in roles])
        roles_list.append(roles)
        roles = pd.DataFrame(columns=['role/designation'])
        for strings in role_list: 
            roles = roles.append(pd.DataFrame({'role/designation': strings}, index=[0]), ignore_index=True)
    return roles

#------------------------------------------------------------------

def get_tech_exp(): 
    """
    This function creates two empty lists, tech_exp_list and tech_experience_list
    uses a for loop to convert the resumes into str format
    then finds all words after the the charecters TECH EXP
    set end position to be 4 newline charecters
    appends the captured text into the tech_exp_list
    uses another forloop on the new list to splitlines between each newline
    joins on ' ' for each element witin the tech_experience
    appends new list to tech_experience_list
    creates pandas data frame from tech_experience_list
    returns tech_exp_years as a pd dataframe
    
    """
    tech_exp_list = []
    tech_experience_list = []
    for f in files_list:
        res = textract.process(f)
        resume = res.decode('UTF-8')
        start = resume.find('TECH EXP') + 19
        end = resume.find('\n\n\n\n', start)
        tech_exp = resume[start:end]
        tech_exp_list.append(tech_exp)

        for string in tech_exp_list:
            tech_experience = string.splitlines()
            tech_experience = ' '.join([str(elem) for elem in tech_experience])
        tech_experience_list.append(tech_experience)
        tech_exp_years = pd.DataFrame(columns=['tech_experience_years'])
        for strings in tech_experience_list: 
            tech_exp_years = tech_exp_years.append(pd.DataFrame({'tech_experience_years': strings}, index=[0]), ignore_index=True)
    return tech_exp_years

#------------------------------------------------------------------

def get_nontech_exp():
    """
    This function creates two empty lists, nontech_exp_list and nontech_experience_list
    uses a for loop to convert the resumes into str format
    then finds all words after the the charecters NON-TECH
    set end position to be 4 newline charecters
    appends the captured text into the nontech_exp_list
    uses another forloop on the new list to splitlines between each newline
    joins on ' ' for each element witin the nontech_experience
    appends new list to nontech_experience_list
    creates pandas data frame from nontech_experience_list
    returns nontech_exp_years as a pd dataframe
    
    """
    nontech_exp_list = []
    nontech_experience_list = []
    for f in files_list:
        res = textract.process(f)
        resume = res.decode('UTF-8')
        start = resume.find('NON-TECH') + 22
        end = resume.find('\n\n\n\n', start)
        nontech_exp = resume[start:end]
        nontech_exp_list.append(nontech_exp)

        for string in nontech_exp_list:
            nontech_experience = string.splitlines()
            nontech_experience = ' '.join([str(elem) for elem in nontech_experience])
        nontech_experience_list.append(nontech_experience)
        nontech_exp_years = pd.DataFrame(columns=['nontech_experience_years'])
        for strings in nontech_experience_list: 
            nontech_exp_years = nontech_exp_years.append(pd.DataFrame({'nontech_experience_years': strings}, index=[0]), ignore_index=True)
    return nontech_exp_years

#------------------------------------------------------------------

def get_skill_inventory():
    """
    This fucntion will concat each of the pandas dataframes 
    generated by the above fucntions inorder to create a final
    panmdas data frame. 
    This fucntion will ask the user to input a directory path
    to be used to store the newly converted ecel file.
    returns skill_inventory as a pandas data frame with max cowidth
    
    """
    frames = [get_names(), get_roles(), get_skills(), get_education(), get_certification(), get_tech_exp(), get_nontech_exp()]
    skill_inventory = pd.concat(frames, axis = 1)
    pd.set_option("display.max_colwidth", -1)
    directory_excel = input("Please enter a directory to save excel file: " "Example: /User/name/Desktop/foldername/nameofexcelfile.xlsx")
    skill_inventory.to_excel (directory_excel, index = False, header=True)
    return skill_inventory

#------------------------------------------------------------------

# Look for exception for dups.

'''

# Find a duplicate rows

duplicateDFRow = skill_inventory[skill_inventory.duplicated(['Name'])]
print(duplicateDFRow)
'''


'''
def get_skill_inventory1():

    global files_list 
    files_list = []
    # assign directory
    directory = input("Please enter a directory: ")
    # iterate over files in that directory
    for filename in os.listdir(directory):
        if filename.endswith(".docx"):
            file = os.path.join(directory, filename)
            files_list.append(file)

        frames = [get_names(), get_roles(), get_skills(), get_education(), get_certification(), get_tech_exp(), get_nontech_exp()]
        skill_inventory = pd.concat(frames, axis = 1)
        pd.set_option("display.max_colwidth", -1)
        directory_excel = input("Please enter a directory to save excel file: " "Example: /User/name/Desktop/foldername/nameofexcelfile.xlsx")
        skill_inventory.to_excel (directory_excel, index = False, header=True)
    return skill_inventory   
'''