from my_module.functions import *
"""Test for functions used in functions.py for AlumniBot.
    Referenced asserts from A3 chatbot assignment, others
    are self-written. Also generated a master assert 
    function to test all asserts.
"""

def test_remove_punctuation():
    """Tests remove_punctuation function"""
    
    assert isinstance(remove_punctuation('z'), str)
    assert callable(remove_punctuation)
    assert remove_punctuation("Hello! It's Ringo!") == "Hello Its Ringo"
    
def test_prepare_text():
    """Tests prepare_text function"""
   
    assert isinstance(prepare_text('Three two one.'), list)
    assert callable(prepare_text)

def test_string_concatenator():
    """Tests string_concatenator function"""
    
    assert isinstance(string_concatenator('good', 'morning', ' '), str)
    assert callable(string_concatenator)
    
def test_list_to_string():
    """Tests list_to_string function"""
    
    assert isinstance(list_to_string(['c', 'd'], '-'), str)
    assert callable(list_to_string)
    
def test_end_chat():
    """Tests end_chat function"""
    
    assert isinstance(end_chat(['x', 'y']), bool)
    assert callable(end_chat)
    assert end_chat(['quit']) == True
    
def test_check_link():
    """Tests check_link function"""
    
    assert isinstance(check_link(['link']), bool)
    assert callable(check_link)
    assert check_link(['link']) == True
    
def test_check_region():
    """Tests check_region function"""
    
    assert isinstance(check_region(['region']), bool)
    assert callable(check_region)
    assert check_region(['region']) == True
    
def test_check_area():
    """Tests check_area function"""
    
    assert isinstance(check_area(['area']), bool)
    assert callable(check_area)
    assert check_area(['area']) == True

def test_check_city():
    """Tests check_city function"""
    
    assert isinstance(check_city(['city']), bool)
    assert callable(check_city)
    assert check_city(['city']) == True
    
def test_check_industry():
    """Tests check_industry function"""
    
    assert isinstance(check_industry(['industry']), bool)
    assert callable(check_industry)
    assert check_industry(['industry']) == True
    
def test_check_back():
    """Tests check_back function"""
    
    assert isinstance(check_back(['back']), bool)
    assert callable(check_back)
    assert check_back(['back']) == True
    
def test_check_alumni_region():
    """Tests check_alumni_region function"""
    
    assert callable(check_alumni_region)
    
def test_check_alumni_area():
    """Tests check_alumni_area function"""
    
    assert callable(check_alumni_area)
    
def test_check_alumni_city():
    """Tests check_alumni_city function"""
    
    assert callable(check_alumni_city)
    
def test_check_alumni_industry():
    """Tests check_alumni_industry function"""
    
    assert callable(check_alumni_industry)
    
def test_all_asserts():
    """Tests all test functions"""
    
    test_remove_punctuation()
    test_prepare_text()
    test_string_concatenator()
    test_list_to_string()
    test_end_chat()
    test_check_link()
    test_check_region()
    test_check_area()
    test_check_city()
    test_check_industry()
    test_check_back()
    test_check_alumni_region()
    test_check_alumni_area()
    test_check_alumni_city()
    test_check_alumni_industry()        
