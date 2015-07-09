import random
import sys
import time

SPRITES = [ 'O', '1' , '2' , '3']


def runner():
  a = list("                     ")

  for i in range(1,101):
    time.sleep(0.1)
    print( ''.join(a) +  "{0:.2f}".format((i/100.0)*100 ) ,end='\n'),
    a[i//5] = '.'

#  Displays a section of the pad in the middle of the screen

runner()
