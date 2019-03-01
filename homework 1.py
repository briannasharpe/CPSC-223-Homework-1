#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 18:06:23 2019

@author: heroname
"""
# title
border = '====={0:^50}====='
title = border.format('Student Academic Records')
print(title)
print("This program creates a file that contains a table for inputted student academic records.")

students = int(input("Please enter the number of students : "))
print("Please enter the data of the students using 'CWID:__, FirstName:__, LastName:__, Gender:__, BirthDate:__, ClassID:__, ClassDate:__, Grade:__'\n")


# define variables
student_list = list() # list for student dictionary objects
count = 0 # loop counter

# write output file, reset file if necessary
f = open('results.txt', mode='w')
# add table heading
f = open('results.txt', mode='a')
f.writelines('{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}'.format("CWID", "First Name", "Last Name", "Gender", "Birth Date", "Class ID", "Class Date", "Grade"))
f.close()

# student data input
while count < students:
    # define variables
    student_dict = {}
    
    print("Student ", count + 1, "/", students)
    data = input("Enter data : ")

    # split data into sections
    data_list = data.split(', ')
    
    for e in data_list:
        # separate key and value from data sections
        key, value = e.split(':')
        # add key and value to student dictionary
        student_dict.update({key:value})
        # add data to table in output file
        f = open('results.txt', mode='a')
        # create new line if at beginning
        if key == "CWID":
            f.writelines("\n")
        f.writelines('{:15s}'.format(value))
        
        f.close()
    # ---------- end for loop ----------
    
    # add current student to the list of all students
    student_list.append(student_dict)
    # update loop count
    count += 1
# ---------- end while loop ----------