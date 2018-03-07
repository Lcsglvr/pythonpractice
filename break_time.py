#break_time.py
#by Dr lcsglvr 3-6-2018


import webbrowser
import time

def breaktime():
        print("This program started on "+time.ctime())
        
#defining variables
total_break=5
current_break=1

#every 2 hrs, a google window pops up with searches for "take a break"
while(current_break < total_break):
        time.sleep(60*60*2)
        webbrowser.open("https://www.google.com/search?tbm=isch&sa=1&ei=RX2fWsvfJou3ggfAgbr4Aw&q=take+a+break&oq=take+a+break&gs_l=psy-ab.3..0i67k1j0l4j0i67k1j0l4.11005.11877.0.12283.2.2.0.0.0.0.65.118.2.2.0....0...1c.1.64.psy-ab..0.2.117...0i30k1.0.nXJ2KX46tjw")
        current_break = current_break + 1

breaktime()
