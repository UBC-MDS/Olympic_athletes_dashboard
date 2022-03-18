# Olympic Athletes Dashboard
## Welcome!

Welcome to the Olympic Athletes Dashboard app project repository! Based on a dataset of approximately 270,000 Olympic Athletes, spanning from all Olympic Games between 1896 and 2016, this app aims to help you get some insight into Olympic Athletes.

This document (the README file) is a hub to give you some information about the project. Jump straight to one of the sections below, or just scroll down to find out more.

- [Olympic Athletes Dashboard](#olympic-athletes-dashboard)
  - [Welcome!](#welcome)
  - [Demonstration](#demonstration)
  - [What are we doing?](#what-are-we-doing)
    - [The problem](#the-problem)
    - [The solution](#the-solution)
  - [Who are we?](#who-are-we)
  - [What do we need?](#what-do-we-need)
  - [Installation](#installation)
  - [Get involved](#get-involved)
  - [Contact us](#contact-us)
  - [License](#license)
  - [Thank you](#thank-you)

## Demonstration

Our [Olympics Athlete Dashboard](https://olympic-athletes-dash.herokuapp.com/) currently consists of:
* 4 plots: 3 histograms for athletes' `Age`, `Weight`, and `Height` distribution that can zoom in or out with two colors to distinguish genders, and a map for number of athlete per country.
* 6 filters on the left side bar: a slider for `year` range selection, two drop-down menus for `sports` and `countries`, and three radio buttons to select `medal` and `season`, and whether or not we can animate the world map by year. All filters have tooltips to explain how to use them.
* 1 help button: to briefly explain what this dashboard does and guide users.
* All the plots are on the "Plots" tab, the "Data Table" tab shows the clean data based on the selected filters. 
* When users select some specific combination with no available data, such as Alpine Skiing in Summer Olympics, there will be a message "No Available Data For Search Parameters" on the left side bar.

<p align="center">
  <img src="docs/dashboard.gif" width=400/>
</p>

## What are we doing?

### The problem

* For Olympic committees: the Olympics involve a large number of athletes from a variety of backgrounds with different personal attributes (heights, weights, ages). Olympic committees often need an objective reference tool to help in identifying talented individuals with regards to their heights, weights, and ages for various sports and selecting the individuals with great potential at an early point in order to bolster their Olympic teams.
* For national sports authorities: it is not easy for decision-makers to figure out which countries they should turn to when hiring the best possible coach or instructors to train their teams of different types of sports. 
* For athelets themselves: young athletes often do not have a clear vision about their own strengths and weaknesses and the most suitable type of sports that fits their personal attributes.
* For the public: members of the general public, who are enthusiastic about olympic sports, are often less accessible to the historical Olympic athletes data in an interactive way.

All in all, different groups of people have different needs and usage scenarios when it comes to the Olympic athletes' data, and they currently lack a well-designed interactive dashboard to explore the data and find the information.

### The solution

The [Olympic Athletes Dashboard app](https://olympic-athletes-dash.herokuapp.com/) will:

* For Olympic committees: present the distributions of Olympic athletes' personal attributes, namely, ages, weights, and heights, as an objective referencing tool for the Olympic committees to identify the potential individuals with suitable heights and weights.
* For national sports authorities: highlight the counts of athletes per country on an interactive world map based on the applied criteria to initiated the visual comparisons between global countries so that decision-makers can identify the advantageous country to hire instructors for different sports.
* For athletes themselves: allow users to customize diverse filters such as years, sports, seasons, and medals on the original dataset, which can help young athletes to select the suitable type of sports that fits their personal attributes.
* For the public: provide an interactive tool that makes Olympic athletes' data accessible and visible to the general public or any sports enthusiast.

So, corresponding to the different problems, users have the options to customize diverse filters and obtain insights from the Olympic Athletes data. And the overall goal is to answer the personal attributes (ages, weights and heights) and the gloabl ditributions of the Olympic atheltes based on customized criteria. 

## Who are we?

The founders of the Olympic Athletes Dashboard app - [Xiaohan Chen][link_xiaohan], [Cuthbert Chow][link_cuthbert], [Jessie Wong][link_jessie] and [Luming Yang][link_luming] - are teammates from the Data Science graduate school at the University of British Columbia. 

The development of this app is mentored by the teaching team from the MDS program at the University of British Columbia. Check out the awesome program and teaching team on the [homepage][link_ubc_mds].

## What do we need?

**You**! In whatever way you can help.

We need expertise in data visualization, user experience design, and dashboard maintenance.

We'd love your feedback along the way either from a developer view or from a user experience perspective.

Our ultimate goal is to mitigate the misconceptions of the Olympic athletes and promote involvement from the general public in Olympic sports.

## Installation

To run this app locally using Docker, please run the following commands after cloning the repo:

```bash
cd Olympic_athletes_dashboard
docker-compose build
docker-compose up
```

You could view the webpage locally by navigating to the address http://localhost:8000/ in your browser.

## Get involved

If you think you can help in any of the areas listed above (and we bet you can) or in any of the many areas that we haven't yet thought of (and here we're *sure* you can) then please check out our [contributors' guidelines](CONTRIBUTING.md) and our [roadmap](../../issues/1).

Please note that it's very important to us that we maintain a positive and supportive environment for everyone who wants to participate. When you join us we ask that you follow our [code of conduct](CODE_OF_CONDUCT.md) in all interactions both on and offline.

## Contact us

If you want to report a problem or suggest an enhancement we'd love for you to [open an issue](../../issues) at this github repository because then we can get right on it.

## License

The product is provided based on [this License](LICENSE).

## Thank you

Thank you so much for visiting the Olympic Athletes Dashboard and we hope that you enjoy the journay of exploring the Olympic Athletes data.


[link_xiaohan]: https://github.com/Anthea98
[link_cuthbert]: https://github.com/cuthchow
[link_jessie]: https://github.com/jessie14
[link_luming]: https://github.com/Luming-ubc
[link_ubc_mds]: https://masterdatascience.ubc.ca/
