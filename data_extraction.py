from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

driver = webdriver.Chrome(ChromeDriverManager().install())

def scroll(driver, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height
        
        
driver.maximize_window()
driver.get("https://www.iplt20.com/match/2020/60?tab=overview")
driver.implicitly_wait(10)

scroll(driver, 3)

# 13.2 J Pattinson to A Rayudu, no run, 135.7 km/h short length going down leg. 
# 0.4 D Chahar to Q de Kock, FOUR, 133.3 km/h full length on off stump.
# 14.4 M Stoinis to I Kishan, SIX, 105.1 km/h good length outside off stump.
# 18.3 A Nortje to H Pandya, WICKET!!! H Pandya is out c Ajinkya Rahane b Anrich Nortje, 
#     129.9 km/h short length just outside off stump.

# this function accepts '13.2 J Pattinson to A Rayudu' as input and returns over and ball
def calculate_over(commentary):
    commentary = commentary[0:4]
    commentary = commentary.split('.')
    over = commentary[0]
    ball = commentary[1]
    return int(over),int(ball)

# this function accepts '13.2 J Pattinson to A Rayudu' as input and returns bowler name and batsman name
def find_batsman_bowler(commentary):
    players = commentary[5:]
    players = players.split(" to ")
    bowler_name, batsman_name = players[0], players[1]
    return bowler_name,batsman_name

# this function accepts 'no run' as input and returns runs scored and wide run
def calculate_run(commentary):
    if '.' in commentary:
        commentary = commentary.replace('.','')
    commentary = commentary.split(' ')
    if(commentary[0] == 'no'):
        return 0,0
    elif(commentary[0] == 'one'):
        return 1,0
    elif(commentary[0] == 'two'):
        return 2,0
    elif(commentary[0] == 'three'):
        return 3,0
    elif(commentary[0] == 'FOUR'):
        return 4,0
    elif(commentary[0] == 'five'):
        return 5,0
    elif(commentary[0] == 'SIX'):
        return 6,0
    elif(commentary[0] == 'wide'):
        return 1,1
    else:
        return int(commentary[0]),0

# this function accepts '135.7 km/h short length going down leg.' as input and returns ballspeed
def calculate_ballspeed(commentary):
    commentary = commentary.split(' ')
    speed = float(commentary[0])
    return speed

# this function accepts '135.7 km/h short length going down leg.' as input and returns length
def find_length(commentary):
    commentary = commentary.split(' ')
    if 'toss' in commentary:
        length = commentary[2] + ' toss'
    else:    
        length = commentary[2]
    return length

# this function accepts '135.7 km/h short length going down leg.' as input and returns line 
def find_line(commentary):
    commentary = commentary.split(' ')
    if 'on' in commentary:
        commentary.remove('on')
    if 'just' in commentary:
        commentary.remove('just')
    if 'going' in commentary:
        commentary.remove('going')
    if 'length' in commentary:
        commentary = ' '.join(commentary)
        commentary = commentary.split(" length ")
    elif 'toss' in commentary:
        commentary = ' '.join(commentary)
        commentary = commentary.split(" toss ")
    line = commentary[1]
    line = line.replace('.','')
    return line


# innings 1

innings_1= [];

other_balls_1 = driver.find_elements_by_css_selector(".matchStream .streamContent .streamItems .item.ball.innings-1 .content p")

for a in other_balls_1:
    innings1=1
    wicket_1 = 0
    commentary_1 = a.text
    commentary_1 = commentary_1.split(', ')
    over_1,ball_1 = calculate_over(commentary_1[0])
    bowler_name_1, batsman_name_1 = find_batsman_bowler(commentary_1[0])
    run_scored_1,wide_1 = calculate_run(commentary_1[1])
    if(len(commentary_1)-1 == 2 and commentary_1[2]!='no-ball.'):
        ball_speed_1 = calculate_ballspeed(commentary_1[2])
        ball_length_1 = find_length(commentary_1[2])
        ball_line_1 = find_line(commentary_1[2])
    else:
        ball_speed_1 = float('NaN')
        ball_length_1 = None
        ball_line_1 = None
    innings_1.append([innings1,over_1,ball_1,bowler_name_1,batsman_name_1,run_scored_1,wide_1,ball_speed_1,ball_line_1,ball_length_1,wicket_1])
    innings_1.sort()

    
four_balls_1 = driver.find_elements_by_css_selector(".matchStream .streamContent .streamItems .item.four.innings-1 .content p")
for b in four_balls_1: 
    f_innings1=1
    f_wicket_1 = 0
    f_commentary_1 = b.text
    if(len(f_commentary_1)-1 >=1):
        f_commentary_1 = f_commentary_1.split(', ')
        f_over_1,f_ball_1 = calculate_over(f_commentary_1[0])
        f_bowler_name_1, f_batsman_name_1 = find_batsman_bowler(f_commentary_1[0])
        f_run_scored_1,f_wide_1 = calculate_run(f_commentary_1[1])
        if(len(f_commentary_1)-1 == 2 and f_commentary_1[2]!='no-ball.' ):
            f_ball_speed_1 = calculate_ballspeed(f_commentary_1[2])
            f_ball_length_1 = find_length(f_commentary_1[2])
            f_ball_line_1 = find_line(f_commentary_1[2])
        else:
            f_ball_speed_1 = float('NaN')
            f_ball_length_1 = None
            f_ball_line_1 = None
        innings_1.append([f_innings1,f_over_1,f_ball_1,f_bowler_name_1,f_batsman_name_1,f_run_scored_1,f_wide_1,f_ball_speed_1,f_ball_line_1,f_ball_length_1,f_wicket_1])
        innings_1.sort()


six_balls_1 = driver.find_elements_by_css_selector(".matchStream .streamContent .streamItems .item.six.innings-1 .content p")
for d in six_balls_1:    
    s_innings1 = 2
    s_wicket_1 = 0
    s_commentary_1 = d.text
    if(len(s_commentary_1)-1 >=1):
        s_commentary_1 = s_commentary_1.split(', ')
        s_over_1,s_ball_1 = calculate_over(s_commentary_1[0])
        s_bowler_name_1, s_batsman_name_1 = find_batsman_bowler(s_commentary_1[0])
        s_run_scored_1,s_wide_1 = calculate_run(s_commentary_1[1])
        if(len(s_commentary_1)-1 == 2 and s_commentary_1[2]!='no-ball.' ):
            s_ball_speed_1 = calculate_ballspeed(s_commentary_1[2])
            s_ball_length_1 = find_length(s_commentary_1[2])
            s_ball_line_1 = find_line(s_commentary_1[2])
        else:
            s_ball_speed_1 = float('NaN')
            s_ball_length_1 = None
            s_ball_line_1 = None
        innings_1.append([s_innings1,s_over_1,s_ball_1,s_bowler_name_1,s_batsman_name_1,s_run_scored_1,s_wide_1,s_ball_speed_1,s_ball_line_1,s_ball_length_1,s_wicket_1])
        innings_1.sort()

        
wicket_balls_1 = driver.find_elements_by_css_selector(".matchStream .streamContent .streamItems .item.wicket.innings-1 .content p")
for c in wicket_balls_1:    
    w_innings1=1
    w_commentary_1 = c.text
    if(len(w_commentary_1)-1 >=1):
        w_commentary_1 = w_commentary_1.split(', ')
        w_over_1,w_ball_1 = calculate_over(w_commentary_1[0])
        w_bowler_name_1, w_batsman_name_1 = find_batsman_bowler(w_commentary_1[0])
        temp_1 = commentary_1[1].split(' ')
        w_run_scored_1 = 0
        w_wide_1 = 0
        w_wicket_1 = 1
        if(len(w_commentary_1)-1 == 2 and w_commentary_1[2]!='no-ball.' ):
            w_ball_speed_1 = calculate_ballspeed(w_commentary_1[2])
            w_ball_length_1 = find_length(w_commentary_1[2])
            w_ball_line_1 = find_line(w_commentary_1[2])
        else:
            w_ball_speed_1 = float('NaN')
            w_ball_length_1 = None
            w_ball_line_1 = None
        innings_1.append([w_innings1,w_over_1,w_ball_1,w_bowler_name_1,w_batsman_name_1,0,0,w_ball_speed_1,w_ball_line_1,w_ball_length_1,w_wicket_1])
        innings_1.sort()






# innings 2

innings_2= [];

other_balls = driver.find_elements_by_css_selector(".matchStream .streamContent .streamItems .item.ball.innings-2 .content p")

for i in other_balls:
    innings=2
    wicket = 0
    commentary = i.text
    commentary = commentary.split(', ')
    over,ball = calculate_over(commentary[0])
    bowler_name, batsman_name = find_batsman_bowler(commentary[0])
    run_scored,wide = calculate_run(commentary[1])
    if(len(commentary)-1 == 2 and commentary[2]!='no-ball.'):
        ball_speed = calculate_ballspeed(commentary[2])
        ball_length = find_length(commentary[2])
        ball_line = find_line(commentary[2])
    else:
        ball_speed = float('NaN')
        ball_length = None
        ball_line = None
    innings_2.append([innings,over,ball,bowler_name,batsman_name,run_scored,wide,ball_speed,ball_line,ball_length,wicket])
    innings_2.sort()
    
four_balls = driver.find_elements_by_css_selector(".matchStream .streamContent .streamItems .item.four.innings-2 .content p")
for r in four_balls: 
    f_commentary = r.text
    f_innings = 2
    f_wicket = 0
    if(len(f_commentary)-1 >=1):
        f_commentary = f_commentary.split(', ')
        f_over,f_ball = calculate_over(f_commentary[0])
        f_bowler_name, f_batsman_name = find_batsman_bowler(f_commentary[0])
        f_run_scored,f_wide = calculate_run(f_commentary[1])
        if(len(f_commentary)-1 == 2 and f_commentary[2]!='no-ball.' ):
            f_ball_speed = calculate_ballspeed(f_commentary[2])
            f_ball_length = find_length(f_commentary[2])
            f_ball_line = find_line(f_commentary[2])
        else:
            f_ball_speed = float('NaN')
            f_ball_length = None
            f_ball_line = None
        innings_2.append([f_innings,f_over,f_ball,f_bowler_name,f_batsman_name,f_run_scored,f_wide,f_ball_speed,f_ball_line,f_ball_length,f_wicket])
        innings_2.sort()

        
six_balls = driver.find_elements_by_css_selector(".matchStream .streamContent .streamItems .item.six.innings-2 .content p")
for k in six_balls:    
    s_innings = 2
    s_wicket = 0
    s_commentary = k.text
    if(len(s_commentary)-1 >=1):
        s_commentary = s_commentary.split(', ')
        s_over,s_ball = calculate_over(s_commentary[0])
        s_bowler_name, s_batsman_name = find_batsman_bowler(s_commentary[0])
        s_run_scored,s_wide = calculate_run(s_commentary[1])
        if(len(s_commentary)-1 == 2 and s_commentary[2]!='no-ball.' ):
            s_ball_speed = calculate_ballspeed(s_commentary[2])
            s_ball_length = find_length(s_commentary[2])
            s_ball_line = find_line(s_commentary[2])
        else:
            s_ball_speed = float('NaN')
            s_ball_length = None
            s_ball_line = None
        innings_2.append([s_innings,s_over,s_ball,s_bowler_name,s_batsman_name,s_run_scored,s_wide,s_ball_speed,s_ball_line,s_ball_length,s_wicket])
        innings_2.sort()


# 18.3 A Nortje to H Pandya, WICKET!!! H Pandya is out c Ajinkya Rahane b Anrich Nortje, 29.9 km/h short length just outside off stump.

wicket_balls = driver.find_elements_by_css_selector(".matchStream .streamContent .streamItems .item.wicket.innings-2 .content p")
for l in wicket_balls:
       
    w_innings=2
    w_commentary = l.text
    if(len(w_commentary)-1 >=1):
        w_commentary = w_commentary.split(', ')
        w_over,w_ball = calculate_over(w_commentary[0])
        w_bowler_name, w_batsman_name = find_batsman_bowler(w_commentary[0])
        temp = commentary[1].split(' ')
        w_run_scored = 0
        w_wide = 0
        w_wicket = 1
        if(len(w_commentary)-1 == 2 and w_commentary[2]!='no-ball.' ):
            w_ball_speed = calculate_ballspeed(w_commentary[2])
            w_ball_length = find_length(w_commentary[2])
            w_ball_line = find_line(w_commentary[2])
        else:
            w_ball_speed = float('NaN')
            w_ball_length = None
            w_ball_line = None
        innings_2.append([w_innings,w_over,w_ball,w_bowler_name,w_batsman_name,0,0,w_ball_speed,w_ball_line,w_ball_length,w_wicket])
        innings_2.sort()


for z in innings_1:
    print(z)
        
for k in innings_2:
    print(k) 

t=['innings','over','ball','bowler_name','batsman_name','run_scored','is_wide','ball_speed','ball_line','ball_length','is_wicket']


with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(t)
    writer.writerows(innings_1)
    writer.writerows(innings_2)


print("Saved in excel")
    
driver.quit()
