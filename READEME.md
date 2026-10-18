Created by Jacob Macy
In this application, users are able to enter various pieces of information regarding bowling leauges. Created for bowling alleys, this system allows users to create leagues and edit the information within them, specifically bowlers, and than add game statistics for each bowler. All information is displayed on top of the display of each bowler's average based on the games entered.

For this system to run properly, python must be installed as well as the python package "Flask".

Setup:

1. Download this repository as a zip file and extract it.
2. Open a terminal within the extracted file directory folder containing requirements.txt
3. Install Flask by entering into the terminal:

        python -m pip install -r requirements.txt

With this system, you are only allowed to enter games scores less than 300 and greater than or equal to 0, as is possible in bowling. Any number that does not meets these requirements prompts an alert, telling the user the number is invalid. The same thing happens if you try to add a league that is already present. Data is also only saved while the server is running. Once restarted, the data resets.

On top of the code, this file also contains the UML Class Diagram and inital project proposal for this assignment.

Trello Board Link: https://trello.com/b/fpsHPHNS