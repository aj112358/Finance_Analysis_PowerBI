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

In order to answer these questions, I invested time in planning the PowerBI measures I would need to create and also planned a rough outline of the dashboard visuals I wanted. Here are some screenshots of my dashboard planning:

insert pics here


## Data Analysis Summary

I spend way too much money.


## Hardware and Software Used

- Python (v3.8)
- Python Libraries: openpyxl, os
- Windows 10 Machine
- Microsoft PowerBI Desktop (v2.93)
- Microsoft Excel
- Apple iPad (7th Gen) and pencil


## Overview of Microsoft Power BI

asdf


## Explanation of Project Files

Here is a brief description of each file/folder found in this GitHub repository.

### Finance_Data/20xx
This is the folder that contains each month's Excel data in a separate Excel workbook. The dates (currently) range from Aug 2018 - Dec 2020.

### change_excel_sheets.py
This Python script takes in an Excel file with multiple sheets and renames all sheets to 'Sheet1'. (*Apparantly this was necessary for importing the Excel data into PowerBI?*)

### Finance_Data.xlsx
This is a copy of the original Excel file that I was using to keep track of my spending.

### Personal_Finance_Dashboard.pbix
This is the main PowerBI file containing the finance dashboards.


## Data Collection Methodology

I collected this data by keeping all purchase receipts and inputting the data manually into Excel. The information I kept track of was: Date, Item Category, Price, Location, Comment.

In order to import this data into PowerBI, it was quite the process. Since the data was contained in *multiple Excel sheets in the same Excel workbook*, I first had to separate the sheets into their own Excel workbook - this turned out to be the easiest avenue to importing the data.


## Data Cleaning

There was quite a bit of data cleaning to do. I had to do some basic editing of the 'Item' category column, in order to have consistent categories. For example, I had 'hair cut', 'Hair cut', 'Hair-Cut' as separate categores, and so had to standardize this into simply a 'Hair Cut' category.

There was a lot of work needed to be done with dates. Some dates were of a 'Text' type, some were a 'General' type, and still others were the 'Date' type. These had to be standardized.

There were only a few rows that contained null entries, so I simply chose to remove these rows from the overall dataset; This would now drastically affect the variance of the overall data.


## Measure Creation & Visualizations

In order to help answer the questions listed above, I started by making three other tables: (i) Calendar Lookup, (i) Item Lookup, (iii) Location Lookup.

The calendar lookup contains each range of dates from the data. From this I created various other useful calculated columns including month name/number, month-and-year, quarter,  and end of week/month.
  
The item lookup table contained a single column of each distinct Item category. While working through the project, I realized that every month had a rental payment listed. It didn't make sense to me to have this consistently in each month, so I created a filter that can be used to manually include or exclude rental payments. To accomplish this I needed a second column in the Item Lookup table to represent the 'Rent' item as a Boolean.
  
The location table contains a single column of each distinct location of purchase.

Once these lookup tables were ready, I followed my planned layout above and created each visual one at a time. As I created these, I also created the associated measure I would need to portray the data. Some of the measures I made were:
- total cost
- price ranges
- average cost per day, week, year
- Boolean to adress my sick days

The main visuals I used were 'slicers'. I created calendar slicers for overall date, year, quarter, month, and day of week. With these one has a lot of options as to what granularity they wish to visualize their data with respect to dates. I also have two slicers for weekday/weekend and healthy/sick selections. There is also a slicer that acts as a dropdown to select various purchase price ranges.


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



### Jan 5, 2020
- had to fix date issues in original data
- started making visuals
- made list for EDA
- created date, location, item tables


