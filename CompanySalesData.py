#!/usr/bin/env python
# coding: utf-8

# # Read Total profit of all months and show it using a line plot

# Total profit data provided for each month. Generated line plot must include the following properties: 
# 
# X label name = Month Number
# Y label name = Total profit

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:\\Users\\presc\\OneDrive\\Desktop\\company_sales_data.csv")
profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()
plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()


# # Get total profit of all months and show line plot with the following Style properties
# 

# Generated line plot must include following Style properties: –
# 
# -Line Style dotted and Line-color should be red
# -Show legend at the lower right location.
# -X label name = Month Number
# -Y label name = Sold units number
# -Add a circle marker.
# -Line marker color as read
# -Line width should be 3

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:\\Users\\presc\\OneDrive\\Desktop\\company_sales_data.csv")
profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()

plt.plot(monthList, profitList, label = 'Profit data of last year', 
      color='r', marker='o', markerfacecolor='k', 
      linestyle='--', linewidth=3)
      
plt.xlabel('Month Number')
plt.ylabel('Profit in dollar')
plt.legend(loc='lower right')
plt.title('Company Sales data of last year')
plt.xticks(monthList)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()


# # Read all product sales data and show it  using a multiline plot

# Display the number of units sold per month for each product using multiline plots. (i.e., Separate Plotline for each product ).

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:\\Users\\presc\\OneDrive\\Desktop\\company_sales_data.csv")
monthList  = df ['month_number'].tolist()
faceCremSalesData   = df ['facecream'].tolist()
faceWashSalesData   = df ['facewash'].tolist()
toothPasteSalesData = df ['toothpaste'].tolist()
bathingsoapSalesData   = df ['bathingsoap'].tolist()
shampooSalesData   = df ['shampoo'].tolist()
moisturizerSalesData = df ['moisturizer'].tolist()

plt.plot(monthList, faceCremSalesData,   label = 'Face cream Sales Data', marker='o', linewidth=3)
plt.plot(monthList, faceWashSalesData,   label = 'Face Wash Sales Data',  marker='o', linewidth=3)
plt.plot(monthList, toothPasteSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, bathingsoapSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, shampooSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)
plt.plot(monthList, moisturizerSalesData, label = 'ToothPaste Sales Data', marker='o', linewidth=3)

plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.xticks(monthList)
plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
plt.title('Sales data')
plt.show()


# # Read toothpaste sales data of each month and show it using a scatter plot

# Also, add a grid in the plot. gridline style should “–“.
# 
# 

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:\\Users\\presc\\OneDrive\\Desktop\\company_sales_data.csv")
monthList  = df ['month_number'].tolist()
toothPasteSalesData = df ['toothpaste'].tolist()
plt.scatter(monthList, toothPasteSalesData, label = 'Tooth paste Sales data')
plt.xlabel('Month Number')
plt.ylabel('Number of units Sold')
plt.legend(loc='upper left')
plt.title(' Tooth paste Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.show()


# #  Read face cream and facewash product sales data and show it using the bar chart

# The bar chart should display the number of units sold per month for each product. Add a separate bar for each product in the same chart.
# 
# 

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:\\Users\\presc\\OneDrive\\Desktop\\company_sales_data.csv")
monthList  = df ['month_number'].tolist()
faceCremSalesData   = df ['facecream'].tolist()
faceWashSalesData   = df ['facewash'].tolist()

plt.bar([a-0.25 for a in monthList], faceCremSalesData, width= 0.25, label = 'Face Cream sales data', align='edge')
plt.bar([a+0.25 for a in monthList], faceWashSalesData, width= -0.25, label = 'Face Wash sales data', align='edge')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.title(' Sales data')

plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('Facewash and facecream sales data')
plt.show()


# # Read sales data of bathing soap of all months and show it using a bar chart. Save this plot to your hard disk

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:\\Users\\presc\\OneDrive\\Desktop\\company_sales_data.csv")
monthList  = df ['month_number'].tolist()
bathingsoapSalesData   = df ['bathingsoap'].tolist()
plt.bar(monthList, bathingsoapSalesData)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title(' Sales data')
plt.xticks(monthList)
plt.grid(True, linewidth= 1, linestyle="--")
plt.title('bathingsoap company sales data')
plt.show()


# # Read the total profit of each month and show it using the histogram to see the most common profit ranges

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:\\Users\\presc\\OneDrive\\Desktop\\company_sales_data.csv")
profitList = df ['total_profit'].tolist()
labels = ['low', 'average', 'Good', 'Best']
profit_range = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(profitList, profit_range, label = 'Profit data')
plt.xlabel('profit range in dollar')
plt.ylabel('Actual Profit in dollar')
plt.legend(loc='upper left')
plt.xticks(profit_range)
plt.title('Profit data')
plt.show()


# #  Calculate total sale data for last year for each product and show it using a Pie chart

# Note: In Pie chart display Number of units sold per year for each product in percentage.

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:\\Users\\presc\\OneDrive\\Desktop\\company_sales_data.csv")
monthList  = df ['month_number'].tolist()

labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
salesData   = [df ['facecream'].sum(), df ['facewash'].sum(), df ['toothpaste'].sum(), 
         df ['bathingsoap'].sum(), df ['shampoo'].sum(), df ['moisturizer'].sum()]
plt.axis("equal")
plt.pie(salesData, labels=labels, autopct='%1.1f%%')
plt.legend(loc='lower right')
plt.title('Sales data')
plt.show()


# # Read Bathing soap facewash of all months and display it using the Subplot
# 

# In[4]:


import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:\\Users\\presc\\OneDrive\\Desktop\\company_sales_data.csv")
monthList  = df ['month_number'].tolist()
bathingsoap   = df ['bathingsoap'].tolist()
faceWashSalesData   = df ['facewash'].tolist()

f, axarr = plt.subplots(2, sharex=True)
axarr[0].plot(monthList, bathingsoap, label = 'Bathingsoap Sales Data', color='k', marker='o', linewidth=3)
axarr[0].set_title('Sales data of  a Bathingsoap')
axarr[1].plot(monthList, faceWashSalesData, label = 'Face Wash Sales Data', color='r', marker='o', linewidth=3)
axarr[1].set_title('Sales data of  a facewash')

plt.xticks(monthList)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.show()


# # Read all product sales data and show it using the stack plot

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("C:\\Users\\presc\\OneDrive\\Desktop\\company_sales_data.csv")
monthList  = df ['month_number'].tolist()

faceCremSalesData   = df ['facecream'].tolist()
faceWashSalesData   = df ['facewash'].tolist()
toothPasteSalesData = df ['toothpaste'].tolist()
bathingsoapSalesData   = df ['bathingsoap'].tolist()
shampooSalesData   = df ['shampoo'].tolist()
moisturizerSalesData = df ['moisturizer'].tolist()

plt.plot([],[],color='m', label='face Cream', linewidth=5)
plt.plot([],[],color='c', label='Face wash', linewidth=5)
plt.plot([],[],color='r', label='Tooth paste', linewidth=5)
plt.plot([],[],color='k', label='Bathing soap', linewidth=5)
plt.plot([],[],color='g', label='Shampoo', linewidth=5)
plt.plot([],[],color='y', label='Moisturizer', linewidth=5)

plt.stackplot(monthList, faceCremSalesData, faceWashSalesData, toothPasteSalesData, 
              bathingsoapSalesData, shampooSalesData, moisturizerSalesData, 
              colors=['m','c','r','k','g','y'])

plt.xlabel('Month Number')
plt.ylabel('Sales unints in Number')
plt.title('Alll product sales data using stack plot')
plt.legend(loc='upper left')
plt.show()


# In[ ]:




