# Olympics Athelete Dashboard

## Motivation and Purpose

**Our Role:** Data science consultancy firm <br/>
**Target Audience:** National Olympics committee, sports enthusiasts in the general public

The olympics involve a large number of athletes from a variety of backgrounds, as well as personal attributes (height, weight, age). Olympic committees have an interest in identifying talented individuals for various sports at an early point in order to bolster their olympic teams. To address this, we propose building a data dashboard which allows olympic committees to explore historical trends in various athletes across all years and sports. Our dashboard will display distribution of athlete attributes, which can be filtered by medals won, country, olympic years, and sport, such that users can make quick comparisons and understand long-term trends in the data. 

The dashboard can also be utilised by members of the general public who are enthusiastic about olympic sports, and want to learn more about the history of the sports and their respective athletes. 

  
<br/><br/>
 
  
## Dataset Description

We will be visualizing a dataset of approximately 270,000 Olympic Athletes, spanning from all Olympic Games between 1896 and 2016.
Each athlete has 15 associated variables that describe them. The features are categorized and described below:
 - personal identification
    - `id` : athlete id number
    - `name`  : athlete name
 - physical characteristics 
    - `sex` : athlete sex
    - `age` : athlete age at time of Olympic Games
    - `weight` : athlete weight at time of Olympic Games
    - `height`: athlete height at time of Olympic Games
 - country they competed for 
    - `team` : country name
    - `noc` : country code
  - the Games they competed in 
    - `games` : year and season
    - `year`  : year of Games
    - `season` : summer or winter
    - `city`  : location of Games
  - the sport they competed in 
     - `sport`  : category of Olympic sport 
     - `event` : specific event within the sport
 - achievement 
    - `medal` : Gold, Silver, Bronze, or None

The data is sourced from Tidy Tuesday [here](https://github.com/rfordatascience/tidytuesday/blob/master/data/2021/2021-07-27/readme.md), 
and the raw data can be found [here](https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-07-27/olympics.csv)


## Research questions and usage scenarios

David is a sports enthusiast and he wants to find out some fun facts about the Olympic games based on historical data. He wants to know which country wins the most Olympic medals through out history or for a certain period of time. He also wants to find out what types of sports his home country has advantages in regarding total counts of gold medals. Moreover, he is interested in learning what the typical age of an athlete is to win the gold medal for a certain type of sport. When David opens the Olympic Athlete Dashboard, he will see an overview of all gold medal winners throughout history in terms of their heights, weights, ages, and representing countries in a world map. He could use the slider tool on the top left corner of the app to define the time period that he is interested in. He could also filter the results based on season and the type of sports. He will find out that United states is the country that won the most gold medals. He will also be surprised at the outstanding performance of his home country, Canada, especially in winter Olympic games. Finally, if he selects the sports Diving and Shotgun from the dropdown menu, he will discover that the average age of Diving athletes is younger than the average of Shotgun players.
