import pandas as pd
#Readthefile
data=pd.read_excel("D:\heigth.csv",sheet_name='height')
import matplotlib.pyplot as plt
fig,(ax1,ax2,ax3,ax4)=plt.subplots(nrows=4,ncols=1,
figsize=(15,15))
plt.title("StudentGrades")
ax1.plot(data.iloc[0:10,0],data.iloc[0:10,4],'-.c')
ax2.bar(data.iloc[0:10,0],data.iloc[0:10,4],color='orange')
ax3.pie(data.iloc[0:10,4],labels=data.iloc[0:10,0],
autopct="%1.1f%%",startangle=90)
ax4.scatter(data.iloc[0:10,0],data.iloc[0:10,4],color='magenta')
