# Project Title

## Motivation and Purpose
 
  
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

David is a sports enthusiast and he wants to find out the fun facts about the Olympic games based on historical data. He wants to know which country wins the most Olympic medals through out the history or for a certain period of time. He also wants to find out what types of sports his home country has advantages in regarding total counts of golden medals. Moreover, he is interested in learning what is the typical age of an athlete to win the golden medal for a certain type of sports. When David logs on to the "Who are in the Olympics app", he will see an overview of all golden metal winners throughout the history in terms of their heights, weights, ages, and representing countries in a world map. He could use the slider tool on the top left corner of the app to define the time period that he is interested in. He could also filter the results based on seasons and the type of sports. He will find out that United states is the country that won the most golden medals. He will also be surprised at the outstanding performance of his home country, Canada, especially in winter Olympic games. Finally, if he select Diving and Shortgun from the dropdown menu, he will discover that the average age of Diving athletes is younger than the average of Shortgun players.
