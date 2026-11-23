"""
Bishal Nath
bishal.nath66@login.cuny.edu		
"""
def dec2bin(dec_num):
  bin_str = ""
  while dec_num != 0:
    rem = (dec_num)%2
    bin_str = str(rem) + bin_str
    dec_num = int((dec_num)/2)
  return bin_str
