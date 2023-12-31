# Visualization Analysis System for Movie Data
The visualization analysis includes the following components:
1. Analyze categorical data using techniques such as TreeMap.
2. Analyze high-dimensional data using methods such as parallel category graph, one way anova test.
3. Visualization system (website): Utilize technologies like Dash, plotly.express, HTML, and JavaScript to implement dynamic data analysis visulisations
4. The complete data report is available for access in the file named <strong>'report.pdf'</strong>.
5. Author: The whole project, included codes, report writing, analysis, data storytelling, etc., is completed by Ruoshui Chen

# Manual
git clone the repository, open the working directory and run python main.py, then accesss the website by http://127.0.0.1:8050/

# Project Objective
Our objective is to analyze movie data and provide insights for global movie makers, including movie directors, producers, etc., regarding financial success. To achieve this, we have defined a series of subtasks that progress from simple to complex, allowing for a step-by-step and in-depth analysis. Each subtask aims to tell a data story through aesthetic and intuitive visualizations.

# Data Set
The original full data set I choose to use is [Top 100 popular movies from 2003 to 2022 (iMDB)](https://www.kaggle.com/datasets/georgescutelnicu/top-100-popular-movies-from-2003-to-2022-imdb). 
After data cleaning, some samples are dropped, and we add 2 new columns which are called Income_million and Budget_million, for visualising 2 original attributes in numerical types and consistent units.   
The new dataset (extracted subsets) contains 13 attributes as follows and our analysis only relate 9 attributes and 396 samples (can be found in folder <strong>data</strong>)
- Title: The movie name
- Rating: The rating of the movie according to IMDB users
- Year: The release year of the movie
- Runtime: The length of the movie in minutes
- Director/s: The person/people who directed the movie
- Stars: Actors playing in the movie
- Genre/s: The genre/s of the movie
- Budget_million: The money spent on the movie
- Income_million: The money earned by the movie

# Analysis Results
A common theme observed through our visual analysis system is the prominence of Intellectual Properties (IPs). The high-income movies mentioned in the top rankings are predominantly well-known series movies that have gained international recognition. These movies have transcended the realm of mere entertainment and have become iconic properties that captivate audiences with their unique storylines and immersive worlds. For example, the magical and enchanting universe of the Harry Potter movies has resonated with people worldwide, appealing to their emotions and captivating their hearts.  

The impact of the COVID-19 pandemic on the global market has been significant. Data analysis plays a crucial role in helping movie directors and producers navigate these uncertain times by providing insights into the latest market demands and trends. The ability to analyse data empowers the movie industry to anticipate and respond to market shifts, enabling a more efficient recovery process, and we expect the blooming of excellent movies around the world in the future years.

# Implementation
We develop a multipage website to display all visualisations. The Python dash package is used to establish a website and enable a combination of backend and frontend, so we can deal with the data and display the result in a single file. For navigation, we use register_page to register each page and navigate by adding dcc.Link in main.py. Moreover, we embed the html files inside Python to construct the main page layout or display other interactive plots, specifically, by html.Iframe with src equals each web page source (the html file). 

The dynamic data visualisations are mainly on the ground of Python code, in which several callback functions can change the output element with the changing of input elements. The animation plot made by plotly.express.bar is also embedded into this Python file.

Talking about the file structure, our webpage is run by main.py., where also the server is started. Each webpage is run by a separate Python file in a folder called pages. All other files such as HTML, .png, and javascript files are put in the assets folder, to allow them to communicate with Python files and be an element of part of the webpage. In the assets folder, index.html displays the main page, and other HTML files are part of the visualisation. The index.css controls the majority of the styling of our website, and the minority of styling is embedded in HTML files and Python codes. Finally, index.js defines functions that allow the website to be more interactive and dynamic.



