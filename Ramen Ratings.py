"""
Bishal Nath
bishal.nath66@login.cuny.edu		
"""
import pandas as pd

fileName = input("Enter file name: ")
ratings = pd.read_csv(fileName)
group = input("Group by (Country or Style): ")

print(ratings.groupby(group)['Stars'].mean())