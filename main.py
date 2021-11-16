def compute_square_area(side_length):
    return pow(side_length, 2)

class Square:
    def __init__(self, side_length):
        self.side_length = side_length
        
        
    def compute_area(self):
        return pow(self, side_length, 2)

    
    
if __name__ == "__main__"
    example_square = Square(15)
    print(example_square.compute_area())

class Email:
    def __init__(self, to, subject, body):
        self.to = to
        self.subject = subject
        self.body = body

    def send(self):
        print("Sending email with subject: {self.subject} and body: {self.body} to: {self.to}")

        
        
if __name__ == "__main__":
    greeting_email = Email("bob@nasa.gov", "Welcome!", "Welcome to epicpython.io!")
    greeting_email.send()
    

#----------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
import numpy as np 
import textract
import os
import re
#import zipfile
import shutil

global key_words_and_symbols
key_words_and_symbols = ['as','distinct','cast','when','then','end','case','from','join','on','and','where','like','or','between','order','by','select','from','left', 'join', 'and','is', 'null', '=']


def tables_in_query(sql_str):
    
    # remove the /* */ comments
    q = re.sub(r"/\*[^*]*\*+(?:[^*/][^*]*\*+)*/", "", sql_str)

    # remove whole line -- and # comments
    lines = [line for line in q.splitlines() if not re.match("^\s*(--|#)", line)]

    # remove trailing -- and # comments
    q = " ".join([re.split("--|#", line)[0] for line in lines])
    #print(q)
    
    # split on blanks, parens and semicolons
    tokens = re.split(r"[\s)(;]+", q)
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    #print('TOKENS',tokens)

    # scan the tokens. if we see a FROM or JOIN, we set the get_next
    # flag, and grab the next one (unless it's SELECT).



    tables = list()
    get_next = False
    for tok in tokens:
        if get_next:
            if tok.lower() not in ["", "select"]:
                tables.append(tok)
                pos = tokens.index(tok)
                if tokens[pos +1] not in ["from", "join","where",""]:
                    tables.append(tokens[pos +1])
            get_next = False
        get_next = tok.lower() in ["from", "join"]
    print('TABLES', tables)
        #Extract aliases
    aliases = []
    table = []
    for index, element in enumerate(tables):
    	if index % 2 != 0:
            aliases.append(element)
    for index, element in enumerate(tables):
        if index % 2 == 0:
            table.append(element)

    db_name = []
    schema_name = []
    final_tables = []
    for ele in table:
        lst1 = ele.split('.')
        if len(lst1) == 3:
            db_name.append(lst1[0])
            schema_name.append(lst1[1])
            final_tables.append(lst1[2])
        elif len(lst1) == 2:
            db_name.append(lst1[0])
            final_tables.append(lst1[1])

    return aliases,  table, db_name, schema_name

#FIELDS in query -- DO NOT USE

def fields_in_query(sql_str,tables):
    # remove the /* */ comments
    q = re.sub(r"/\*[^*]*\*+(?:[^*/][^*]*\*+)*/", "", sql_str)

    # remove whole line -- and # comments
    lines = [line for line in q.splitlines() if not re.match("^\s*(--|#)", line)]

    # remove trailing -- and # comments
    q = " ".join([re.split("--|#", line)[0] for line in lines])
    #print(q)
    
    # split on blanks, parens and semicolons
    tokens = re.split(r"[\s)(;]+", q)
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()

            #get the list of values after 'As'
    value_after_as = list()
    get_next = False
    for tok in tokens:
        if get_next:
            if tok.lower() not in ["", "select"]:
                value_after_as.append(tok)
            get_next = False
        get_next = tok.lower() in ["as", "like" ]
    #print(value_after_as)
    

    
    fields_1 = list(set(tokens) - set(key_words_and_symbols))
    fields_2 = list(set(fields_1) - set(tables))
    final_fields_list = list(set(fields_2) - set(value_after_as))
    return(final_fields_list)

    #extract fields #2
def get_field_name(qry):
    print('QUERY',qry.lower())
    qry2 = qry.lower()
    name_list = []
    start = qry2.find('select') + 7
    end = qry2.find('from', start)
    skills = qry2[start:end]
    skills = skills.lower()
    #field_name = re.sub(r'/\*[^*]*\*+(?:[^*/][^*]*\*+)*/',"", skills)
    #tokens = re.split(r"[\t\n:]+", field_name)
    #tokens = re.split(r"[\t\n:]+", skills)
    name_list.append(skills)
    fields = ([s.replace('\t', '') for s in name_list])
    fields = ([s.replace('=', '') for s in fields])
    fields = ([s.replace('when', '') for s in fields])
    fields = ([s.replace('case', '') for s in fields])
    fields = ([s.replace('distinct', '') for s in fields])
    fields = ([s.replace('isnull', '') for s in fields])

    # names = pd.DataFrame(columns=['fields'])
    # for name in name_list:
    #     names = names.append(pd.DataFrame({'fields': name}, index=[0]), ignore_index=True)
    return fields




files_path_list = []
files_list = []

for filename in os.listdir(os.getcwd()):
        if filename.endswith(".txt"):
            file_path = os.path.join(os.getcwd(), filename)
            files_path_list.append(file_path)
            files_list.append(filename)


#print(files_path_list)
print(files_list)
#files_list = ['5ED25AF7.txt']

final_dict = {}
final_dict['Server'] = []
final_dict['DataBase'] = []
final_dict['Schema'] = []
final_dict['Tables'] = []
final_dict['Aliases'] = []
final_dict['Fields'] = []



for file in files_list:
    file = open(file)
    qry = file.read().replace("\n", " ")
    file.close()
    print(qry)
    print('\n')
    aliases,tables, db, schemas = tables_in_query(qry)
    #fields = fields_in_query(qry, tables)
    fields = get_field_name(qry)
    #tables_in_query(qry)
    final_dict['Server'].append(file.name)
    final_dict['DataBase'].append(db)
    final_dict['Schema'].append(schemas)
    final_dict['Tables'].append(tables)
    final_dict['Aliases'].append(aliases)
    final_dict['Fields'].append(fields)
    print(file.name)
    print(tables)
    #print(fields)
    #print(list(table))
    print('\n')
    print('\n')

print(final_dict)
final_df=pd.DataFrame(final_dict)
print(final_df)
final_df.to_csv('extracted_text.csv')


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------

import pandas as pd
import numpy as np 
import textract
import os
import re
#import zipfile
import shutil

global key_words_and_symbols
key_words_and_symbols = ['as','distinct','cast','when','then','end','case','from','join','on','and','where','like','or','between','order','by','select','from','left', 'join', 'and','is', 'null', '=']


def tables_in_query(sql_str):
    
    # remove the /* */ comments
    q = re.sub(r"/\*[^*]*\*+(?:[^*/][^*]*\*+)*/", "", sql_str)

    # remove whole line -- and # comments
    lines = [line for line in q.splitlines() if not re.match("^\s*(--|#)", line)]

    # remove trailing -- and # comments
    q = " ".join([re.split("--|#", line)[0] for line in lines])
    #print(q)
    
    # split on blanks, parens and semicolons
    tokens = re.split(r"[\s)(;]+", q)
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    #print('TOKENS',tokens)

    # scan the tokens. if we see a FROM or JOIN, we set the get_next
    # flag, and grab the next one (unless it's SELECT).



    tables = list()
    get_next = False
    for tok in tokens:
        if get_next:
            if tok.lower() not in ["", "select"]:
                tables.append(tok)
                pos = tokens.index(tok)
                if tokens[pos +1] not in ["from", "join","where",""]:
                    tables.append(tokens[pos +1])
            get_next = False
        get_next = tok.lower() in ["from", "join"]
    print('TABLES', tables)
        #Extract aliases
    aliases = []
    table = []
    for index, element in enumerate(tables):
    	if index % 2 != 0:
            aliases.append(element)
    for index, element in enumerate(tables):
        if index % 2 == 0:
            table.append(element)

    db_name = []
    schema_name = []
    final_tables = []
    for ele in table:
        lst1 = ele.split('.')
        if len(lst1) == 3:
            db_name.append(lst1[0])
            schema_name.append(lst1[1])
            final_tables.append(lst1[2])
        elif len(lst1) == 2:
            db_name.append(lst1[0])
            final_tables.append(lst1[1])

    return aliases,  table, db_name, schema_name


def get_field_name_3(qry): #qry is a string
    print('QUERY',qry.lower())
    qry = qry.lower()
    fields = re.findall('select(.+?)from', qry)

    # for each_item in fields:
    #     print('EACH_ITEM_TYPE',type(each_item))


    return fields




files_path_list = []
files_list = []

for filename in os.listdir(os.getcwd()):
        if filename.endswith(".txt"):
            file_path = os.path.join(os.getcwd(), filename)
            files_path_list.append(file_path)
            files_list.append(filename)


#print(files_path_list)
print(files_list)
#files_list = ['5ED25AF7.txt']

final_dict = {}
final_dict['Server'] = []
final_dict['DataBase'] = []
final_dict['Schema'] = []
final_dict['Tables'] = []
final_dict['Aliases'] = []
final_dict['Fields'] = []



for file in files_list:
    file = open(file)
    qry = file.read().replace("\n", " ")
    file.close()
    print(qry)
    print('\n')
    aliases,tables, db, schemas = tables_in_query(qry)
    #fields = fields_in_query(qry, tables)#1
    #fields = get_field_name(qry) #2
    fields = get_field_name_3(qry) #3
    # get_field_name_3(qry) #3
        #tables_in_query(qry)
    final_dict['Server'].append(file.name)
    final_dict['DataBase'].append(db)
    final_dict['Schema'].append(schemas)
    final_dict['Tables'].append(tables)
    final_dict['Aliases'].append(aliases)
    final_dict['Fields'].append(fields)
    #print(file.name)
    # print(tables)
    # #print(fields)
    # #print(list(table))
    # print('\n')
    # print('\n')

#print(final_dict)
final_df=pd.DataFrame(final_dict)
for col_name,col_data in final_df.iteritems():
    print(col_name,col_data.values )
final_df.to_csv('extracted_text.csv')


























