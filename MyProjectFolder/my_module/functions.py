class Alumni():
    
    def __init__(self, name, region, area, city, industry, company, 
                 professionaltitle):
        """Creates instances for Alumni
        Parameters
        ----------
        self : string
            Specify instance-specific attributes.
        name : string
            Instance sppecific attribute of alumni name (UniqueID).
        region : string 
            Instance sppecific attribute of alumni region.
        area : string 
            Instance sppecific attribute of alumni area.
        city : string 
            Instance sppecific attribute of alumni city.
        industry : string 
            Instance sppecific attribute of alumni industry.
        company : string 
            Instance sppecific attribute of alumni company.
        professionaltitle : string 
            Instance sppecific attribute of alumni professional title.
        """
        
        self.name = name
        self.region = region
        self.area = area
        self.city = city
        self.industry = industry
        self.company = company
        self.professionaltitle = professionaltitle
        
    def profile(self):
        """Class methods for objects of type Alumni
        Parameters
        ----------
        self : string
            Specify instance-specific attributes.
        -------
        print : 
            Print the current instance name, region, area, city, 
            industry, company, professionaltitle. 
        """
        
        print(self.name, self.region, self.area, self.city, self.industry, 
              self.company, self.professionaltitle) 

import csv
import string
import random
import webbrowser
"""A series of modules imported for this project, mainly referenced the A3 
    assignment and browed through GitHub Spring 2019 project example referenced 
    Byungkwon. Also, searched webbrowser documentation to open link.
    """

with open('Take_a_Triton_to_Work_Alumni_Sheet1.csv', encoding = 'cp850') as csv_file:
    """From external code to read csv file: 
    'https://realpython.com/python-csv/#parsing-csv-files-with-pythons-built
    -in-csv-library' and made adjustments to parse csv file of Alumni spreadsheet 
    received from advisor, added self-written code to create master 
    list of class type Alumni objects.
    """
    
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    Master_list = []
    
    for row in csv_reader:
        if line_count == 0:
            print(f'Sorting categories include {", ".join(row[5:10])}')
            line_count += 1
        else:
            alumni = Alumni(row[5], row[6], row[7], row[8], row[9], row[10], row[11])      
            line_count += 1
            Master_list.append(alumni)          
    
    for item in Master_list:
        (item.profile())   
                         
#Creates list to reference Alumni UniqueID count, reflects total number of alumni
AlumniID_list = {}

for item in Master_list:
    if item.name in AlumniID_list:
        AlumniID_list[item.name] += 1
    else:
        AlumniID_list[item.name] = 1                  
                  
#Creates list to reference Alumni region, reflects number of alumni in each region
Region_list = {}

for item in Master_list:
    if item.region in Region_list:
        Region_list[item.region] += 1
    else:
        Region_list[item.region] = 1

#Creates list to reference Alumni area, reflects number of alumni in each area
Area_list = {}

for item in Master_list:
    if item.area in Area_list:
        Area_list[item.area] += 1
    else:
        Area_list[item.area] = 1                  

#Creates list to reference Alumni city, reflects number of alumni in each city
City_list = {}

for item in Master_list:
    if item.city in City_list:
        City_list[item.city] += 1
    else:
        City_list[item.city] = 1
                  
#Creates list to reference Alumni industry, reflects number of alumni in each industry
Industry_list = {}

for item in Master_list:
    if item.industry in Industry_list:
        Industry_list[item.industry] += 1
    else:
        Industry_list[item.industry] = 1
                  
#From the A3 Chatbot assignment, made some adjustments.
def remove_punctuation(input_string):
    """Gets rid of all punctuation if input is a question."""
    
    out_string = ''
    
    for character in input_string:
        if character not in string.punctuation:
            out_string += character
            
    return out_string                  

def prepare_text(input_string):
    """Prepares text inputs for processing."""
    
    temp_string = input_string
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    
    return out_list                  
                  
def string_concatenator(string1, string2, separator):
    """Concatenates two strings, combining them with a specified separator."""
    
    output = string1 + separator + string2
    
    return output                  
                  
def list_to_string(input_list, separator):
    """Turns a list of strings back into one single concatenated string."""
    
    output = input_list[0]
    
    for element in input_list[1:]:
        output = string_concatenator(output, element, separator)
        
    return output                  
                  
def end_chat(input_list):
    """Ends the conversation if the word 'quit' appears."""
    
    for item in input_list:
        if item.lower() == 'quit':
            output = True
        else:
            output = False
        
    return output                  
                  
#Self-written for the AlumniBot
def begin_chat():
    """Prints starting messages for AlumniBot."""
    
    print('Welcome to Take a Triton to Work!')
    print('Type "link" to open the Take a Triton to Work website ' + \
          'to learn more about the program.')
    print('What do you want to know about the available alumni? Please ' + \
          'choose between "Region", "Area", "City", and "Industry".')
    print('Input is susceptible to case sensitivity.')                  

def check_link(user_input):
    """Check if input is 'link'"""
    
    output = ''
    output = list_to_string(user_input,' ')
    if output.lower() == 'link':
        return True
    return False                  
                  
def check_region(user_input):
    """Check if input is 'region'"""
    
    output = ''
    output = list_to_string(user_input,' ')
    if output.lower() == 'region':
        return True
    return False                  
                  
def check_area(user_input):
    """Check if input is 'area'"""
    
    output = ''
    output = list_to_string(user_input,' ')
    if output.lower() == 'area':
        return True
    return False                  
                  
def check_city(user_input):
    """Check if input is 'city'"""
    
    output = ''
    output = list_to_string(user_input,' ')
    if output.lower() == 'city':
        return True
    return False
                  
def check_industry(user_input):
    """Check if input is 'industry'"""
    
    output = ''
    output = list_to_string(user_input,' ')
    if output.lower() == 'industry':
        return True
    return False
                  
def check_back(user_input):
    """Checks if the input is 'back'"""
    
    output = ''
    output = list_to_string(user_input,' ')
    if output.lower() == 'back':
        return True
    return False                  
                  
def check_alumni_region(user_input):
    """Returns profile of the alumni of a specific region"""
    
    for item in Master_list:
        if user_input in item.region:
            (item.profile())                  
                  
def check_alumni_area(user_input):
    """Returns profile of the alumni of a specific area"""
    
    for item in Master_list:
        if user_input in item.area:
            (item.profile())                  
                  
def check_alumni_city(user_input):
    """Returns profile of the alumni of a specific city"""

    for item in Master_list:
        if user_input in item.city:
            (item.profile())                  
                  
def check_alumni_industry(user_input):
    """Returns profile of the alumni of a specific industry"""

    for item in Master_list:
        if user_input in item.industry:
            (item.profile())                  
                  
def start_chatbot():
    """Main function to run the AlumniBot"""
    
    #Setup
    begin_chat()
    chat = True
    
    while chat:
        
        #Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None
        
        #Prepare the input message
        msg = prepare_text(msg)
        
        #Check for an end msg
        if end_chat(msg):
            out_msg = 'Thank you for using the AlumniBot, goodbye!'
            chat = False
       
        #Check if the input is 'region' and return a dictionary of all alumni regions
        elif check_region(msg):
            print('Number of Region(s):', len(Region_list), '--->', Region_list, '<---', 
                  'Type the specific region to view the corresponding alumni ' + \
                  'profile(s) or type "back" if you would like to return to the menu.')
            msg = input('INPUT :\t')
            #Check if the input is one of the alumni regions 
            if msg != 'back':
                (check_alumni_region(msg))
                out_msg = 'Type "back" if you would like to return to the menu ' + \
                'or "quit" to end chat.'
            elif msg == 'back':
                out_msg = 'What do you want to know about the available alumni? ' + \
                'Please choose between Region, Area, City, and Industry.'
        
        #Check if the input is 'area' and return a dictionary of all alumni areas
        elif check_area(msg):
            print('Number of Area(s):', len(Area_list), '--->', Area_list, '<---', 
                  'Type the specific area to view the corresponding alumni ' + \
                  'profile(s) or type "back" if you would like to return to the menu.')
            msg = input('INPUT :\t')
            #Check if the input is one of the alumni areas 
            if msg != 'back':
                (check_alumni_area(msg))
                out_msg = 'Type "back" if you would like to return to the menu ' + \
                'or "quit" to end chat.'
            elif msg == 'back':
                out_msg = 'What do you want to know about the available alumni? ' + \
                'Please choose between Region, Area, City, and Industry.'

        #Check if the input is 'city' and return a dictionary of all alumni cities
        elif check_city(msg):
            print('Number of City(ies):', len(City_list), '--->', City_list, '<---', 
                  'Type the specific city to view the corresponding alumni ' + \
                  'profile(s) or type "back" if you would like to return to the menu.')
            msg = input('INPUT :\t')
            #Check if the input is one of the alumni cities
            if msg != 'back':
                (check_alumni_city(msg))
                out_msg = 'Type "back" if you would like to return to the menu ' + \
                'or "quit" to end chat.'
            elif msg == 'back':
                out_msg = 'What do you want to know about the available alumni? ' + \
                'Please choose between Region, Area, City, and Industry.'
        
        #Check if the input is 'city' and return a dictionary of all alumni industries
        elif check_industry(msg):
            print('Number of Industry(ies):', len(Industry_list), '--->', Industry_list, 
                  '<---', 'Type the specific industry to view the corresponding ' + \
                  'alumni profile(s) or type "back" if you would like to return ' + \
                  'to the menu.')
            msg = input('INPUT :\t')
            #Check if the input is one of the alumni industries
            if msg != 'back':
                (check_alumni_industry(msg))
                out_msg = 'Type "back" if you would like to return to the menu ' + \
                'or "quit" to end chat.'
            elif msg == 'back':
                out_msg = 'What do you want to know about the available alumni? ' + \
                'Please choose between Region, Area, City, and Industry.'
        
        #Check if the input is 'back' and return to menu
        elif check_back(msg):
            out_msg = 'What do you want to know about the available alumni? ' + \
            'Please choose between Region, Area, City, and Industry.'                
        
        #Check if the input is 'link' and open link
        elif check_link(msg):
            webbrowser.open('https://www.alumni.ucsd.edu/s/1170/rd18/wide.aspx? ' + \
                            'sid=1170&gid=1&pgid=9962&content_id=15167',
                            new = 1, autoraise = True)
            out_msg = 'Type "back" if you would like to return to the menu ' + \
            'or "quit" to end chat.'
            
        #Check if input is not valid
        else:
            out_msg = 'Invalid input, try again.'
        
        print(out_msg)                  
                  