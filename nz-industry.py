from datetime import datetime

timestamp = datetime.now().isoformat(timespec='seconds')

# Initialise dictionary where industry growth / contraction is kept
industry_trends = {}

print(f'Starting imports ({timestamp})...')

# Principal imports
import pandas as pd
import statistics as stats
import matplotlib.pyplot as plt

# Load data set from web or local file path as appropriate
url = 'https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2024-financial-year-provisional/Download-data/annual-enterprise-survey-2024-financial-year-provisional.csv'
local_file_path = 'annual-enterprise-survey-2024-financial-year-provisional.csv'
timestamp = datetime.now().isoformat(timespec='seconds')
print(f'Loading data set ({timestamp}):', local_file_path, sep='\n')
data = pd.read_csv('annual-enterprise-survey-2024-financial-year-provisional.csv')
print('Sanity check: data.shape', data.shape)

# Total income subset: Select rows denoting Total Income
total_income = data.loc[data['Variable_name'] == 'Total income']

# Remove commas from "Value" column so that the Object data type can be cast to Int 
total_income['Value'] = total_income['Value'].str.replace(',', '').astype(int)

# Query for top industries based on 2024 total income
income_2024 = total_income.query('Year == 2024 and Variable_name == "Total income"')
industries_sorted = income_2024.sort_values(by=['Value'], ascending=False)
# Exclude 'All industries', which is at the top of the sorted list
top_industries = industries_sorted.head(20)[1:]

# Set up graphical representation of contracting industries
fig, ax = plt.subplots()

# Loop through industries and select that industry as a subset
for industry in total_income['Industry_name_NZSIOC'].unique():
    industry_subset = total_income.query(f'Industry_name_NZSIOC == "{industry}"')
    print('industry_subest.shape:', industry_subset.shape)
    industry_subset_x = industry_subset["Year"]
    industry_subset_y = industry_subset["Value"]
    try:
        industry_subset_lr = stats.linear_regression(industry_subset_x, industry_subset_y)
    except Exception as e:
        print(f"Industry {industry} encountered exception.")
        print(f"Exception of type {type(e)}:", str(e), sep='\n')
    else:
        print(f'Industry: {industry}\nLinear regression slope: {industry_subset_lr.slope}, intercept: {industry_subset_lr.intercept}')
        trend = 'growing' if industry_subset_lr.slope > 0 else 'contracting'
        print(f'The {industry} industry growth trend is ', trend, '.', sep='')
        industry_trends.update({industry: trend}) 
        # Conditional add to graphical representation of contracting industries
        if trend == 'contracting':
            ax.plot(industry_subset_x, industry_subset_y, label=industry)

# Labeling on graphical representation of contracting industries
ax.set_ylabel('Year')
ax.set_ylabel('Million NZ Dollars')
ax.set_title("NZ Contracting Industries")
ax.legend()
plt.show()


'''# Conclusion: "Food product manufacturing" is not a proper category;
# "Food Product Manufacturing" is the actual category
print(total_income.columns)
test_query = total_income.query('Industry_name_NZSIOC == "Food product manufacturing"')
print(test_query[['Year', 'Value']])
print(test_query['Year'].describe())
print(test_query['Value'].describe())'''

# Graph top industries (in growth trend)
fig, ax = plt.subplots()

for industry in top_industries['Industry_name_NZSIOC']:
    industry_trends.update({industry: "growing"})
    industry_subset = total_income.query(f'Industry_name_NZSIOC == "{industry}"')
    industry_subset_x = industry_subset["Year"]
    industry_subset_y = industry_subset["Value"]
    ax.plot(industry_subset_x, industry_subset_y, label=industry)

# Labeling on graphical representation of top industries
ax.set_ylabel('Year')
ax.set_ylabel('Million NZ Dollars')
ax.set_title("NZ Top Industries (2024)")
ax.legend()
plt.show()

# Output the winners (to 20) and losers (all in downward trend)
top_20_names = list(top_industries['Industry_name_NZSIOC'])
# print('Top 20 Names:', top_20_names, '\n')
print('='*10, 'Trends Dictionary - Growing Industries', sep='\n')
for ind, tre in industry_trends.items():
    if ind in top_20_names:
        print(ind, "is in a", tre, "trend")

print('='*10, 'Trends Dictionary - Contracting Industries', sep='\n')
for ind, tre in industry_trends.items():
    if tre == 'contracting':
        print(ind, "is in a", tre, "trend")

# That is a wrap
timestamp = datetime.now().isoformat(timespec='seconds')
print(f'Ending at {timestamp}')