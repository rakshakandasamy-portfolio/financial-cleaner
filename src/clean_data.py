# import pandas, a library that helps us work with tables of data (like Excel sheets), and give it a short nickname "pd" so we type less
import pandas as pd

# create a small sample dataset by hand, styled like real quarterly financial data for Hero MotoCorp (your internship company)
# this mimics common real-world messiness: a missing value, a duplicate row, and inconsistent text formatting
sample_data = {
    "Quarter": ["Q1 FY24", "Q2 FY24", "Q3 FY24", "Q4 FY24", "Q1 FY24", "q2 fy24"],   # some quarters typed in lowercase, one repeated
    "Revenue_Cr": [9128.5, 9560.2, None, 10120.7, 9128.5, 9560.2],                   # revenue in INR crores, one missing value
    "Net_Profit_Cr": [1032.4, 1121.8, 1205.3, 1310.6, 1032.4, 1121.8],               # net profit in INR crores
    "Segment": ["Two-Wheelers", "Two-Wheelers", "Two-Wheelers", "Two-Wheelers", "Two-Wheelers", "Two-Wheelers"]  # business segment
}

# convert that dictionary into an actual table (called a DataFrame) that pandas can work with
df = pd.DataFrame(sample_data)

# print the table to the terminal so we can see what it looks like BEFORE cleaning
print("BEFORE CLEANING:")
print(df)

# standardize the "Quarter" text to be consistent - strip extra spaces and make the first letters match a uniform format
df["Quarter"] = df["Quarter"].str.upper()

# remove rows where "Revenue_Cr" is missing, since revenue is critical data we can't work without
df = df.dropna(subset=["Revenue_Cr"])

# remove exact duplicate rows (Q1 FY24 and Q2 FY24 appeared twice each with identical numbers)
df = df.drop_duplicates()

# reset the row numbering after removing rows, so it looks clean (0,1,2,3...) instead of skipping numbers
df = df.reset_index(drop=True)

# print the table again so we can see what changed AFTER cleaning
print("\nAFTER CLEANING:")
print(df)

# save the cleaned table into the data folder as a new Excel file, index=False means don't add an extra row-number column
df.to_excel("data/cleaned_hero_motocorp.xlsx", index=False)

# print a confirmation message so we know the file was saved successfully
print("\nSaved cleaned file to data/cleaned_hero_motocorp.xlsx")
