Instructions to setup:
1. Make sure Python,Django, pipenv("pip install pipenv"), pandas, matplotlib and seaborn are installed in your terminal.
2. Clone the GitHub repository to your local machine using git clone <repository_url>.
3. Navigate to Django-Project folder and Run pipenv install to install dependencies specified in Pipfile.lock.
4. activate the virtual environment using "pipenv shell".
5. Navigate to ve3web folder and run "python manage.py migrate" to apply migrations and set up the database. 
7. Run the server using "python manage.py runserver" or "python3 manage.py runserver".
8. This deploys the application in your Local Host.
9. Opening the link of your localhost specified in the terminal, you will be able to see the webpage.

Brief explanation of the project:
1. The project is intended to build an web application to analyse and present the analysis of user uploaded CSV file.
2. It has a user friendly outlook and easy to use.
3. The first page contains header and footer, containing about the elements of the page like home, about, services and the footer contains information like address, user reviews etc...
4. Users are only able to upload .csv files or they get an error message.
5. After successful upload we have a success page with success message and the further functionalities.
6. If the csv file is already uploaded by user before, it renders already uploaded message with further functionalities.
7. It contains 4 functionalities, view first few rows, view statistics, handle missing values, visualising the graphs.
8. first few rows: render the first few rows of the csv file using pandas. 
9. view statistics: displays statistics like mean,median, quartiles etc.. using pandas. These are stored in a scrollable table.
10. handle missing values: Displays No. of values are missing in each column. It also has options to fill the missing values, drop the rows and interpolate the missimg values.
11. visualize: This page gives the histograms of numerical columns using matplotlib. 
12. we can navigate back to success/file_already_uploaded page from all functionality pages.
