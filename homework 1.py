#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 18:06:23 2019

@author: heroname
"""
students = input("Please enter the number of students : ")
data = input("Please enter the data using 'CWID:__, FirstName:__, LastName:__, Gender:__, BirthDate:__, ClassID:__, ClassDate:__, Grade:__'\n\n")

# split data into sections
data_list = data.split(', ')
print(data_list)

#define names
student_list = {}
student_dict = {}
for e in data_list:
    # separate key and value from data sections
    key, value = e.split(':')
    print("\n***Current pair: ", key, value)
    print("***Adding key,", key, ", and value,", value, ", to dictionary***")
    # add key and value to student dictionary
    student_dict.update({key:value})
    print("***Dictionary status: ", student_dict)

"""
cwid
first_name
last_name
gender
birth_date
class_id
class_date
grade
"""