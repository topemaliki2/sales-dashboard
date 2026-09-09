import  matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# line plot
# a line plot shows trends over time or sequence
x = [1,2,3,4]
y = [10,60,7,28]
plt.plot(x,y)
plt.show()

data = {"Name": ["Malik", "Dada"],
         "Age": [18, 12]}
df = pd.DataFrame(data)
print(df)

arr = np.array([1, 2, 3, 4, 5])
print(arr)

data = {
"fruits":[
    "apple", "banana", "cherry"
] ,
    "sales":[30, 40, 50]
}
sns.barplot(x="fruits", y = "sales", data=data)
plt.title("sales vs fruits")
plt.show()