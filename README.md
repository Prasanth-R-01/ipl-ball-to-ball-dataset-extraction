# ipl-ball-to-ball-dataset-extraction

You can modify the match number and season in the url part of the code. After running the code, output of the extracted data will be displayed along with the downloaded .csv file. 
This version supports extracting data only for IPL. 
The fields that will be available in the .csv file are:
  1. Innings
  2. Over
  3. Ball
  4. Bowler Name
  5. Batsman Name
  6. Runs Scored
  7. Wide Ball or not(1 for wide delivery and 0 for correct delivery)
  8. Ball Speed
  9. Ball Line
  10. Ball Length
  11. Wicket or not(1 for wicket and 0 for non wicket deliveries)

To change the match number and season :

driver.get("https://www.iplt20.com/match/2020/60?tab=overview")

Here 2020 represents the year and 60 represents the match number.

if you want the data for 1st match in 2021 IPL then,

driver.get("https://www.iplt20.com/match/2021/01?tab=overview")
