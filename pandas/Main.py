import pandas as pd 
#Q1 read csv file
df=pd.read_csv('students.csv')
print(df)
#Q2 Check the no of rows and columns and check of columns
print(df.shape)
print(df.columns)
#Q3 selecting name column
Name_cloumn=df["Name"]
print(Name_cloumn)
#Q4 selecting first 1st row
print(df.head(1))
#Q5 filtering data 
filtered_data=[df["Grade"]>7]
print(filtered_data)
#Q6 adding new column
df["Passed"] = df["Grade"].apply(lambda x: "Yes" if x >= 8 else "No") #lamda used as an anonymous function to fulfil the condition cause I was geting error.
print(df)
#Q7 finding mean of age max of grade
mn_age=df["Age"].mean()
mx_grade=df['Grade'].max()
print(mn_age)
print(mx_grade)
# Sorting the students by Age in descending order.
des_age=df.sort_values(by='Age', ascending=False)
print(des_age)
#Q9 Handling Missing Values
df2=pd.read_csv("marks.csv")
miss_values=df2.fillna(0)
print(miss_values)
#Q10 Group by basis
grouped_data=df.groupby('Grade').size()
print(grouped_data)
#Q11. Value Counts
value_counts=df['Grade'].value_counts()
print(value_counts)
#Q12 Merging DataFrames
df3=pd.DataFrame({"ID":[1,2],"Name":["Amit","Sara"]})
df4=pd.DataFrame({"ID":[1,2],"Marks":[85,90]})
merge_data=pd.merge(df3,df4,on='ID')
print(merge_data)
#Q13 finding the average marks for each subject
df5=pd.read_csv("pracmarks.csv")
numbers = df5.select_dtypes(include='number')  
strings = df5.select_dtypes(exclude='number')
avg_marks=numbers.mean(axis=0)
print(avg_marks)
#Q14 Finding the total sales per product
df6=pd.read_csv("sales.csv")
total_sales=df6["Quantity"]*df6["Price"]
sales_per_product=df6.groupby("Product")["Quantity"].sum()
print(sales_per_product)
#Q15 Weather Dataset
df7=pd.read_csv("weather.csv")
#Part 1: Finding average temperature. 
avg_temp=df7["Temperature"].mean()
print(avg_temp)
#Part 2: Finding the day with maximum rainfall.
max_rainfall_day=df7.loc[df7["Rainfall"].idxmax()]
print(max_rainfall_day)
#Part 3:Showing days where temperature > 30.
hot_days=df7[df7['Temperature']>30]
print(hot_days)
#----------END OF THE CODE----------PANDAS--------------------