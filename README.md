# Personal Finance PowerBI Dashboard

A project that utilizes Microsoft PowerBI to analyze personal financial data and visualize expenses through an interactive dashboard.


## Problem Description

As one should, I have been keeping track of all my daily spending using Microsoft Excel. Using basic sorting/filtering in Excel I'm able to see a very high-level overview of my spending. In order to perform data analysis at a more deeper level, we will turn my static Excel data into dynamic PowerBI dashboards.


## Project Goals

Here are the questions I would like the PowerBI dashboards to answer:
- Monthly spending (in a given year).
- How much money spent per item category.
- List all expenses with comments.
- How much money spent per location.
- The number of purchases in various price ranges.
- Quarterly and weekly spending information.
- Various average costs (per week, month, day).
- Comparison of food costs to restaurant costs.
- Spending behavior when I'm sick.
- Comparison of weekday and weekend spending.


## Data Analysis Summary


## Hardware and Software Used

- Python (v3.8)
- Python Libraries: openpyxl, os
- Windows 10 Machine
- Microsoft PowerBI Desktop (v2.93)
- Microsoft Excel
- Apple iPad (7th Gen) and pencil


## Overview of Microsoft Power BI


## Explanation of Project Files

Here is a brief description of each file/folder found in this GitHub repository.

### Finance_Data/20xx

This is the folder that contains each month's Excel data in a separate Excel workbook. The dates (currently) range from Aug 2018 - Dec 2020.

### change_excel_sheets.py

This Python script takes in an Excel file with multiple sheets and renames all sheets to 'Sheet1'. (*Apparantly this was necessary for importing the Excel data into PowerBI?*)

### Finance_Data.xlsx

This is a copy of the original Excel file that I was using to keep track of my spending.

### Personal_Finance_Dashboard.pbix

## Data Collection Methodology

I collected this data by keeping all receipts from purchases and recording the data manually into Excel.

In order to import this data into PowerBI, it was such a huge hassle...


## Data Cleaning

When I first imported the financial data from the Excel sheets...


## Feature Engineering/Metric Creation



## Conclusion


## How You Can View The Power BI Dashboard

For those interested in actually playing around with the dashboard, here are the steps to do so:
1. Download PowerBI
2. asdf
3. asdf
4. asdf


## Future Steps

For future improvement, we can consider the following ideas:
- asdf
- asdf
- asdf


## Author

AJ Singh (https://github.com/aj112358/)


## Acknowledgements


## UPDATES
### Jan 4, 2020
- loaded multiple Excel files from multiple folders
- extracted data from each file
- cleaned data
  - basic editing
  - standardized categories
  - removed unneeded null entries


### Jan 5, 2020
- had to fix date issues in original data
- started making visuals
- made list for EDA
- created date, location, item tables


