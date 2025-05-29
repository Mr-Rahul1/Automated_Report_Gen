# Automated_Report_Gen

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: RAHUL KAPSE

*INTERN ID*: CT04DK813

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

# In this task
In this task, we created a simple yet powerful automated report generation system using Python. The goal was to take raw data from a file, analyze it, and then produce a well-formatted PDF report that summarizes key insights. This kind of automation is widely useful in business intelligence, data analytics, and reporting workflows where manual report creation is time-consuming and prone to error.

Step 1: Creating the Data Source (CSV File):
Before analyzing data, we needed a structured data source. We chose the CSV (Comma-Separated Values) format because it is simple, human-readable, and easy to process programmatically. CSV files store tabular data, where each line corresponds to a record and each value is separated by a comma.

We demonstrated three methods to create the CSV file:

Using a text editor: Writing the data manually and saving it as .csv.

Using spreadsheet software: Entering the data into Excel or Google Sheets and exporting as CSV.

Using Python code: Writing a Python script that creates and writes rows into a CSV file using the built-in csv module.

This CSV contained sales data with columns: Name, Sales, and Region.

Step 2: Reading and Analyzing the Data: 
After the CSV file was created, we used the pandas library to read it into a DataFrame—a powerful data structure optimized for analysis. Pandas makes it easy to filter, group, and summarize data with just a few commands.

From the data, we extracted several key statistics:

*Total Sales: Sum of the sales column, showing overall revenue.

*Average Sales: Mean sales per individual, to understand typical performance.

*Max Sales & Top Salesperson: The highest sale value and the person who achieved it.

*Sales by Region: Grouped sales by geographical regions, summarizing how each area performed.

These insights are foundational for decision-making and performance monitoring.

Step 3: Generating the PDF Report:
The final step was to present the analysis in a clean, professional PDF report. For this, we used the FPDF library, a lightweight Python tool for PDF creation.

We created a custom PDF class with header and footer methods for consistent formatting. The report included:

*A title header for clarity.

*A summary section listing total, average, and highest sales, plus the top performer.

*A detailed breakdown of sales by region.

The report was formatted with readable fonts and spacing, making it easy to share or archive.

# OUTPUT
