# webScrappingETL

This is an python project that contains a pipeline solution
#to monitor prices of a website called Mercado Livre and
#generates a dashboard by using Scrapy, Pandas, Streamlit and SQL to achieve its purpose.

Names and currency are currently in Portuguese.

# What is a ETL?
# R: It's an abreviation for Extract, Transform and Load, being one of the principal methods for web scrapping.

A ETL structure usually starts with the understand of the problem, which can be a marketing reseach to be on the right needed track. In this case, we'll be searching for the best laptop on the website.

# Scrapy documentation: https://scrapy.org/

1 - Most commont cli command: Scrapy crawl spider name -o(to save) file.ext

2 - Scrapy shell -> Fetch(url)

# Instructions

1 - Clone the file by using git clone command. Open GIT terminal and type git clone https://github.com/rafael-ceotto/webScrappingETL.git

2 - Check the structure of the folder and before running, confirm you have python installed in your machine by opening a terminal and typing python --version.

3 - Once confirming that, observe the directories data, src and subdirectories (collect, dash, transform).

4 - To run the dashboard, will be using streamlit, which is a python library that must be installed on the root of your folder by inputing the command pip install streamlit 
in the terminal.

5 - Also, make sure to install pandas by using the command pip install pandas.

6 - We will be using sqlite for a database connection but we don't need to install it since it was integrated in the newest python version: 3.13.

7 - To run the dashboard, on the root file, please open the terminal and type streamlit rung src/dash/main.py and it will open a localhost at your selected browser.

8 - For curiosity, if you want to open the mercadolivre.db file in the data folder, I recommend using dbeaver and passing a SQL command there as Select * from laptop

# Thank you so much for your time and have a great day.

# This project was created using a website in Portuguese called Mercado Livre and it's used for coding purposes that does not rewoke their rights on the website. To check the website, access the link: https://www.mercadolivre.com.br/ and search for laptops/notebooks.
