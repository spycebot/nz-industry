# nz-industry

Exploring NZ industry survey data to see what we can see

## Summary

The goal of this project is to go from online data source to reasonable visualisation of the most outstanding features of the data, via an exploration of the data using our standard tool set. Our standard for determining whether the data exploration is complete will be that the visualisation is both reasonable, and holds up to scrutiny by third parties.

We will choose a dataset is conveniently available, and is in a known file format that is easy to process. Economic data published by the New Zealand government provides a ready source of data matching these criteria.

After having conducted meaningful exploration of our chosen data set, we set out requirements for a solution that would render the meaningful visualsations that we seek.

### Problem

When we come to dataset with pre-conceived notions about what that dataset contains, we risk losing the opportunity to gain real insights from the data itself.

How do we understand a complex data set without relying on the summaries and opinions of others (statisticians, researchers and data scientists)? How do we tease out the structure of the data while relying solely on the data itself?

### Data

Starting with the following source files, we create the useful meta-data described below.

Source: [Stats NZ - Large Datasets](https://www.stats.govt.nz/large-datasets/csv-files-for-download/)

File: [Annual enterprise survey: 2024 financial year (provisional) – CSV](https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2024-financial-year-provisional/Download-data/annual-enterprise-survey-2024-financial-year-provisional.csv)

Meta-data:
1. Data Frame of top 20 industries
2. List of industries in decline (negative slope of linear regression object)

### Method

Requirements

pandas-2.3.1
- numpy-2.3.1
- python-dateutil-2.9.0.post0
- pytz-2025.2
- siz-1.17.0
- tzdata-2025.2
matplotlib-3.10.3
- contourpy-1.3.2 
- cycler-0.12.1 
- fonttools-4.59.0 
- kiwisolver-1.4.8  
- packaging-25.0 
- pillow-11.3.0 
- pyparsing-3.2.3

1. For each "Industry_name_NZSIOC" (Column 3), capture the "Value" (Column 8) of "Variable_name" Total Income (Column 6) for each "Year" (Column 0).

1. For each subset of data captured above, calculate the linear regression of "Value" (Column 8). If the slope is positive, the industry is in a growth trend, if the slope is negative, the industry is in a contraction trend.

1. Graph 20 largest industries per 2024 "Value" by highest and lowest slope.

1. Graph all industries in a negative growth trend (contracting)

### Model

### Discussion

Having already conducted data exploration, the act of re-categorising, prioritising, shifting, re-tabulating and visualising data yields even further insights. In the act of making a limited number of concrete visualsations, we open up new avenues for understanding, and new perspectives from which to view and review the same set of data which is at hand. 

In the present case, we have just skimmed the surface of the Annual Enterprise Survey 2024 Financial Year (Provisional) dataset, by capturing a linear regression of total income over the period from 2013 to 2024 for each of the industries provided. Now that we have broken the ice, the next step is to look at the additional categories provided under "Variable_name" or even "Variable_category", and ponder what insights a review of those sub-sets can yield.