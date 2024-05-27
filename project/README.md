# MENTAL HELP
#### Video Demo:  <https://youtu.be/ui8yg71hZJs>

## Description:
Mental help is a web application built to track the mood daily, in order to help people understand how the mood fluctuates and influence other behaviors, impacting mental health.
Charting could be the best way to detect mood swings and will give you a tool to use with your doctor to fight disorders, such as bipolar disorder. Learn how to chart your mood and notice signs that can important for your recovery.


## Stack
The technology stack used at this project:
+ Python: Backend;
+ Jinja: to integrate frontend with backend;
+ HTML, Javascript, CSS;
+ Bootstrap: frontend framework;

## Thirdpart Componets
Google Chart API
The Google Chart API connect the data in real time using a variety of data connection tools and protocols.

## Pages
Mental Help has 6 pages to ensure the main function:
+ home
+ register
+ login
+ question form
+ mood chart
+ about

## Basic functionality
Some functions ensure the functionality of Mental Help:

### Index
>Render the homepage with simple and basic information.
There are a caroulser that will allow the user to click and start using the mood chart. When logedin, the user will see the mood chart directly.

### Register
>The user will provide two simple information (username and password) that will be stored into the SQL database for creating an account

### Login
>Allow users to sign in with their credentials based on the registration

### Track Your Mood
>The user will answer a form with 4 questions with three options each. Those simple daily information that will be stored into the SQL database and each of them will have a disigned 'weight' to be used in the mood chart. The user should access the webpage to provide the information every day.

### Mood Chart
>Allow users to track their mood behalf a chart provided by the Google Chart API.
The chart will use the data provided by the user on 'track my mood'and show the status of the mental health.
There are three status: Good, Stable and Poor.

### About
>Information about the webpage and how to use the mood chart. Make people aware of mental health and how to analyze your own mood and how it is influenced by different aspects is a clever way to be mentally stable.

### Logout
>If the user wants to log out


## Requirements
+ Use all the files and folders from project;
+ Run the command using the terminal ``flask run``;
+ SQL moodtracker.db is needed;

## Instructions to use it
1. Sign up and create an account;
2. Answer the 'Track My Mood' form;
3. Automatically the chart will load and the user will analyze the status of the mental health.

