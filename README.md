# Student-Placement-Project

This is my first AI app. I developed it in four steps:

    Generate Data:
    In this step, I used Python's random module to generate random data and saved it in a CSV file named "student.csv".

    Develop Model:
    In this step, I used Python's pandas and numpy libraries to load data from the "student.csv" file. I then separated the data into X and Y variables and divided the datasets into training and testing sets. Next, I employed the RandomForestClassifier from sklearn as our model, trained and tested it, and used the pickle module to save the model for later use in the project.

    Develop API:
    In this step, I used Python's Flask framework to develop an API. I ran this API and accessed it over Wi-Fi. This API utilizes the pickle model created in the previous step.

    Develop App:
    In this step, I developed an Android app using Java and designed the UI with XML. This app connects Android users with the backend API.