# from django.core.mail import send_mail
# from django.template.loader import render_to_string
# context = {'user': "individualName"}
# html_message = render_to_string('shareafric_app/info.html', context)
# send_mail('Welcome to shareafric',
#  '', 'wisteen.technology@shareafric.com', 
#  ["wisdomisaacI=168@gmail.com"], html_message=html_message, auth_user='wisteen.technology@shareafric.com', auth_password='royrex123%%')

# from pytube import YouTube
# yt = YouTube("https://www.youtube.com/watch?v=2aogxVYGX_I&pp=ygUQMzAgc2Vjb25kcyB0aW1lcg%3D%3D")
# vedio = yt.streams.get_highest_resolution()
# vedio.download()

# import pywhatkit
# from datetime import datetime
# pywhatkit.sendwhatmsg("+2349125442676", "I love you", datetime.now().hour, datetime.now().minute + 2)

# import time
# import pyautogui

# # Set the initial position of the dinosaur
# dinosaur_x = 100
# dinosaur_y = 300

# # Start the game by pressing the spacebar
# pyautogui.press('space')

# # Game loop
# while True:
#     # Check for obstacles by checking the color of a specific pixel
#     if pyautogui.pixel(dinosaur_x + 60, dinosaur_y - 10)[0] < 100:
#         pyautogui.press('space')
    
#     # Adjust the position of the dinosaur
#     if pyautogui.pixel(dinosaur_x + 80, dinosaur_y + 10)[0] < 100:
#         pyautogui.keyDown('down')
#         time.sleep(0.05)
#         pyautogui.keyUp('down')
    
#     # Increase the speed of the game (optional)
#     if pyautogui.pixel(400, dinosaur_y - 50)[0] < 100:
#         pyautogui.keyDown('up')
#         time.sleep(0.05)
#         pyautogui.keyUp('up')
    
#     # Delay between each iteration
#     time.sleep(0.01)


# Runner.prototype.gameOver = () =>{}
# Runner.instance_.setSpeed(6000)


import re
# Using beautiful soap would have been  better but no time to istall and import just trying to use what comes with python by default
html = """
<html>
<head>
<title>Our Python Class exam</title>

<style type="text/css">
    /* CSS styles omitted for brevity */
</style>

</head>
<body>
<h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
<table>
    <thead>
        <th>DAY</th><th>COLOURS</th>
    </thead>
    <tbody>
    <tr>
        <td>MONDAY</td>
        <td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
    </tr>
    <tr>
        <td>TUESDAY</td>
        <td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
    </tr>
    <tr>
        <td>WEDNESDAY</td>
        <td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
    </tr>
    <tr>
        <td>THURSDAY</td>
        <td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
    </tr>
    <tr>
        <td>FRIDAY</td>
        <td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
    </tr>
    </tbody>
</table>

<p>Examine the sequence below very well, you will discover that for every 1s that appear 3 times, the output will be one, otherwise the output will be 0.</p>
<p>0101101011101011011101101000111 <span style="color:orange;">Input</span></p>
<p>0000000000100000000100000000001 <span style="color:orange;">Output</span></p>
<p>
</body>
</html>
"""

# Define the pattern to match colors
pattern = r'\b[A-Z]+\b'

# Find all matches of the pattern in the HTML
matches = re.findall(pattern, html)

# Filter out the days of the week from the matches
days_of_week = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY','CSS', 'TABLE', 'SHOWING', 'COLOURS', 'OF', 'DRESS', 'BY', 'WORKERS', 'AT', 'BINCOM', 'ICT', 'FOR', 'THE', 'WEEK', 'DAY', 'COLOURS']
colors = [match for match in matches if match not in days_of_week]

# print(colors)

# colors = [color for color in colors if color.isalpha()]

# Calculate the mean color [That is the color that appear the most like frequency or mode in mathematicas]
mean_color = max(set(colors), key=colors.count)

# Calculate the color that is worn the most still the same as the mean color
most_common_color = max(set(colors), key=colors.count)

# Calculate the median color
sorted_colors = sorted(colors) # to calculate the median we arrange in acending order 
n = len(sorted_colors) # this return the total length of the list
if n % 2 == 0: # this is to check if the total length is an odd  or even number then we decide on the formular to use
    median_color = sorted_colors[n // 2]
else:
    median_color = sorted_colors[(n + 1) // 2] #this other line of code is to ensure that median_color is even an not odd

# Calculate the variance of colors using the formular variance = (1/n-1) * Σ(color - mean)²
# https://www.youtube.com/watch?v=deIQeQzPK08 my hint
# color_counts = {color: colors.count(color) for color in set(colors)} #get the frequency of each color of each color
color_counts = {}
for color in set(colors):
    color_counts[color] = colors.count(color)

# print(color_counts)
# print(colors)
total_count = len(colors)
# print(total_count)  my Σ(xi) = 95
n_x = len(color_counts)
# and my n = 12

# my mean is mean= 95/12
mean = (total_count/n_x)
sum_of_top = 0;
for count in color_counts.values():
    top_equation = (count - mean)**2 #(color - mean)²
    sum_of_top +=  top_equation #Σ(color - mean)²
# print(sum_of_top)
sum_of_bottom = (n_x - 1) #(1/n-1) 
# print(sum_of_bottom)
variance = sum_of_top/sum_of_bottom
# print(variance)

# variance = sum((count / total_count) * ((count / total_count) - 1) for count in color_counts.values())

# Calculate the probability of choosing red
red_count = colors.count('RED')
probability_red = red_count / total_count

# Print the results
print("1. The mean color of the shirts is:", mean_color)
print("2. The color mostly worn throughout the week is:", most_common_color)
print("3. The median color is:", median_color)
print("4. The variance of the colors is:", variance)
print("5. The probability of choosing a red color is:", probability_red)

# to do number 6 I will run the command `pip install psycopg2`

import psycopg2

# Establish a connection to the database (make u change this I dont use it actually but a bit similar to mySQL) 
conn = psycopg2.connect(
    host="localhost",
    port="8000",
    database="postgres",
    user="postgres",
    password="royrex123"
)

# Create a cursor object
cursor = conn.cursor()

# Execute a CREATE TABLE statement
cursor.execute("""
    CREATE TABLE color_frequencies (
        color VARCHAR(50) PRIMARY KEY,
        frequency INTEGER
    )
""")

# # Commit the changes to the database
# conn.commit()
for color, fre in color_counts.items():
    # Execute an INSERT statement for each color and frequency
    cursor.execute("""
        INSERT INTO color_frequencies (color, frequency)
        VALUES (%s, %s)
    """, (color, fre))
    print(f'{color} - {fre} added to database inside color_frequencies table')

#in my list I got BLEW i dont know if that is part of the colors
#I did not want to alter anything so I left it like that

# Commit the changes to the database
conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()
print("6. run this command to check if it has been stored to the daTAbase table ")
print(f'psql -h localhost -p 8000 -d postgres -U postgres -c "SELECT * FROM color_frequencies"')

# run this command to check if it has been stored to the daTA base table 
# psql -h localhost -p 8000 -d postgres -U postgres -c "SELECT * FROM color_frequencies"



