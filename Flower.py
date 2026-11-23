"""
Bishal Nath
bishal.nath66@login.cuny.edu		
"""
num = int(input("Give me a number: "))
print(num, "in binary is ", dec2bin(num))

def dec2bin(dec_num):
  bin_str = "".
  while dec_num != 0:
      rem = (dec_num)%2
      bin_str = bin_str + rem
      dec_num = int((dec_num)/2)
  return bin_str
