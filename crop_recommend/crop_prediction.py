# -*- coding: utf-8 -*-
"""crop_prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13IbAsE8KNHbnAPxdazZywgqkWGB5U5Xg
"""

import pandas as pd
import io
import numpy as np
import random
from sklearn.model_selection import cross_val_score
import joblib

import matplotlib.pyplot as plt
import seaborn as sns

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn import metrics
from sklearn import tree
import warnings
import pickle
warnings.filterwarnings('ignore')

"""# New Section"""



df=pd.read_csv('crop.csv')

df.head()

df.shape

df.columns

df.isnull().any()

print("Number of various crops: ", len(df['crop'].unique()))
print("List of crops: ",df['crop'].unique())

df['crop'].value_counts()

#sns.heatmap(df.corr(),annot=True)

crop_summary = pd.pivot_table(df,index=['crop'],aggfunc='mean')
crop_summary.head()

all_columns = df.columns[:-1]

#labels = df["crop"].unique()
#df["crop"].value_counts().plot(kind="bar")

#plt.show()
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
le.fit(['df.season'])
df['season']=le.fit_transform(df['season'])

df['season']

colorarr = ['#0592D0','#Cd7f32', '#E97451', '#Bdb76b', '#954535', '#C2b280', '#808000','#C2b280', '#E4d008', '#9acd32', '#Eedc82', '#E4d96f',
           '#32cd32','#39ff14','#00ff7f', '#008080', '#36454f', '#F88379', '#Ff4500', '#Ffb347', '#A94064', '#E75480', '#Ffb6c1', '#E5e4e2',
           '#Faf0e6', '#8c92ac', '#Dbd7d2','#A7a6ba', '#B38b6d']

all_columns = df.columns[:-1]
"""
plt.figure(figsize=(15,13))
i = 1
for column in all_columns[:-1]:
    plt.subplot(3,3,i)
    sns.histplot(df[column])
    i+=1
plt.show()

sns.histplot(df[all_columns[-1]])
plt.show()

plt.figure(figsize=(19,17))
sns.pairplot(df, hue = "crop")
plt.show()

f= plt.figure(figsize=(20,5))
ax=f.add_subplot(121)
sns.distplot(df['n'] , color ='red',ax=ax)

ax=f.add_subplot(122)
sns.distplot(df['p'] , color ='green' , ax = ax)
plt.tight_layout()
f= plt.figure(figsize=(20,5))
ax=f.add_subplot(121)
sns.distplot(df['k'] , color ='red',ax=ax)

ax=f.add_subplot(122)
sns.distplot(df['temperature'] , color ='green' , ax = ax)
plt.tight_layout()
f= plt.figure(figsize=(20,5))
ax=f.add_subplot(121)
sns.distplot(df['humidity'] , color ='red',ax=ax)

ax=f.add_subplot(122)
sns.distplot(df['ph'] , color ='green' , ax = ax)
plt.tight_layout()
sns.distplot(df['rainfall'],color ='red')
sns.distplot(df['season'],color ='red')

f= plt.figure(figsize=(15,5))
sns.countplot(df['crop'] , palette = 'Spectral')
plt.xticks(rotation=90)
plt.show()

crop_summary_N = crop_summary.sort_values(by='n', ascending=False)
  
fig = make_subplots(rows=1, cols=2)

top = {
    'y' : crop_summary_N['n'][0:10].sort_values().index,
    'x' : crop_summary_N['n'][0:10].sort_values()
}

last = {
    'y' : crop_summary_N['n'][-10:].index,
    'x' : crop_summary_N['n'][-10:]
}

fig.add_trace(
    go.Bar(top,
           name="Most nitrogen required",
           marker_color=random.choice(colorarr),
           orientation='h',
           text=top['x']),
    
    row=1, col=1
)

fig.add_trace(
    go.Bar(last,
           name="Least nitrogen required",
           marker_color=random.choice(colorarr),
           orientation='h',
          text=last['x']),
    row=1, col=2
)
fig.update_traces(texttemplate='%{text}', textposition='inside')
fig.update_layout(title_text="Nitrogen (N)",
                  plot_bgcolor='white',
                  font_size=12, 
                  font_color='black',
                 height=500)
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
fig.show()

crop_summary_P = crop_summary.sort_values(by='p', ascending=False)
  
fig = make_subplots(rows=1, cols=2)

top = {
    'y' : crop_summary_P['p'][0:10].sort_values().index,
    'x' : crop_summary_P['p'][0:10].sort_values()
}

last = {
    'y' : crop_summary_P['p'][-10:].index,
    'x' : crop_summary_P['p'][-10:]
}

fig.add_trace(
    go.Bar(top,
           name="Most phosphorus required",
           marker_color=random.choice(colorarr),
           orientation='h',
           text=top['x']),
           row=1, col=1
)

fig.add_trace(
    go.Bar(last,
           name="Least phosphorus required",
           marker_color=random.choice(colorarr),
           orientation='h',
           text=last['x']),
           row=1, col=2
)
fig.update_traces(texttemplate='%{text}', textposition='inside')
fig.update_layout(title_text="Phosphorus (P)",
                  plot_bgcolor='white',
                  font_size=12, 
                  font_color='black',
                 height=500)

fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
fig.show()

crop_summary_K = crop_summary.sort_values(by='k', ascending=False)
  
fig = make_subplots(rows=1, cols=2)

top = {
    'y' : crop_summary_K['k'][0:10].sort_values().index,
    'x' : crop_summary_K['k'][0:10].sort_values()
}

last = {
    'y' : crop_summary_K['k'][-10:].index,
    'x' : crop_summary_K['k'][-10:]
}

fig.add_trace(
    go.Bar(top,
           name="Most potassium required",
           marker_color=random.choice(colorarr),
           orientation='h',
          text=top['x']),
          row=1, col=1
)

fig.add_trace(
    go.Bar(last,
           name="Least potassium required",
           marker_color=random.choice(colorarr),
           orientation='h',
          text=last['x']),
    row=1, col=2
)
fig.update_traces(texttemplate='%{text}', textposition='inside')
fig.update_layout(title_text="Potassium (K)",
                  plot_bgcolor='white',
                  font_size=12, 
                  font_color='black',
                 height=500)

fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)
fig.show()

fig = go.Figure()
fig.add_trace(go.Bar(
    x=crop_summary.index,
    y=crop_summary['n'],
    name='Nitrogen',
    marker_color='indianred'
))
fig.add_trace(go.Bar(
    x=crop_summary.index,
    y=crop_summary['p'],
    name='Phosphorous',
    marker_color='lightsalmon'
))
fig.add_trace(go.Bar(
    x=crop_summary.index,
    y=crop_summary['k'],
    name='Potash',
    marker_color='crimson'
))
fig.update_layout(title="N, P, K values comparision between crops",
                  plot_bgcolor='white',
                  barmode='group',
                  xaxis_tickangle=-45)

fig.show()

labels = ['Nitrogen(N)','Phosphorous(P)','Potash(K)']
fig = make_subplots(rows=1, cols=5, specs=[[{'type':'domain'}, {'type':'domain'},
                                            {'type':'domain'}, {'type':'domain'}, 
                                            {'type':'domain'}]])

rice_npk = crop_summary[crop_summary.index=='rice']
values = [rice_npk['n'][0], rice_npk['p'][0], rice_npk['k'][0]]
fig.add_trace(go.Pie(labels=labels, values=values,name="Rice"),1, 1)

cotton_npk = crop_summary[crop_summary.index=='cotton']
values = [cotton_npk['n'][0], cotton_npk['p'][0], cotton_npk['k'][0]]
fig.add_trace(go.Pie(labels=labels, values=values,name="Cotton"),1, 2)
jute_npk = crop_summary[crop_summary.index=='jute']
values = [jute_npk['n'][0], jute_npk['p'][0], jute_npk['k'][0]]
fig.add_trace(go.Pie(labels=labels, values=values,name="Jute"),1, 3)

maize_npk = crop_summary[crop_summary.index=='maize']
values = [maize_npk['n'][0], maize_npk['p'][0], maize_npk['k'][0]]
fig.add_trace(go.Pie(labels=labels, values=values,name="Maize"),1, 4)

lentil_npk = crop_summary[crop_summary.index=='lentil']
values = [lentil_npk['n'][0], lentil_npk['p'][0], lentil_npk['k'][0]]
fig.add_trace(go.Pie(labels=labels, values=values,name="Lentil"),1, 5)
fig.update_traces(hole=.4, hoverinfo="label+percent+name")
fig.update_layout(
    title_text="NPK ratio for rice, cotton, jute, maize, lentil",
    annotations=[dict(text='Rice',x=0.06,y=0.8, font_size=15, showarrow=False),
                 dict(text='Cotton',x=0.26,y=0.8, font_size=15, showarrow=False),
                 dict(text='Jute',x=0.50,y=0.8, font_size=15, showarrow=False),
                 dict(text='Maize',x=0.74,y=0.8, font_size=15, showarrow=False),
                dict(text='Lentil',x=0.94,y=0.8, font_size=15, showarrow=False)])
fig.show()

labels = ['Nitrogen(N)','Phosphorous(P)','Potash(K)']
specs = [[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}],[
         {'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}]]
fig = make_subplots(rows=2, cols=5, specs=specs)
cafe_colors =  ['rgb(255, 128, 0)', 'rgb(0, 153, 204)', 'rgb(173, 173, 133)']

apple_npk = crop_summary[crop_summary.index=='apple']
values = [apple_npk['n'][0], apple_npk['p'][0], apple_npk['k'][0]]
fig.add_trace(go.Pie(labels=labels, values=values,name="Apple", marker_colors=cafe_colors),1, 1)

banana_npk = crop_summary[crop_summary.index=='banana']
values = [banana_npk['n'][0], banana_npk['p'][0], banana_npk['k'][0]]
fig.add_trace(go.Pie(labels=labels, values=values,name="Banana", marker_colors=cafe_colors),1, 2)

grapes_npk = crop_summary[crop_summary.index=='grapes']
values = [grapes_npk['n'][0], grapes_npk['p'][0], grapes_npk['k'][0]]
fig.add_trace(go.Pie(labels=labels, values=values,name="Grapes", marker_colors=cafe_colors),1, 3)

orange_npk = crop_summary[crop_summary.index=='orange']
values = [orange_npk['n'][0], orange_npk['p'][0], orange_npk['k'][0]]
fig.add_trace(go.Pie(labels=labels, values=values,name="Orange", marker_colors=cafe_colors),1, 4)

mango_npk = crop_summary[crop_summary.index=='mango']
values = [mango_npk['n'][0], mango_npk['p'][0], mango_npk['k'][0]]
fig.add_trace(go.Pie(labels=labels, values=values,name="Mango", marker_colors=cafe_colors),1, 5)

coconut_npk = crop_summary[crop_summary.index=='coconut']
values = [coconut_npk['n'][0], coconut_npk['p'][0], coconut_npk['k'][0]]
fig.add_trace(go.Pie(labels=labels, values=values,name="Coconut", marker_colors=cafe_colors),2, 1)

papaya_npk = crop_summary[crop_summary.index=='papaya']
values = [papaya_npk['n'][0], papaya_npk['p'][0], papaya_npk['k'][0]]
fig.add_trace(go.Pie(labels=labels, values=values,name="Papaya", marker_colors=cafe_colors),2, 2)

pomegranate_npk = crop_summary[crop_summary.index=='pomegranate']
values = [pomegranate_npk['n'][0], pomegranate_npk['p'][0], pomegranate_npk['k'][0]]
fig.add_trace(go.Pie(labels=labels, values=values,name="Pomegranate", marker_colors=cafe_colors),2, 3)

watermelon_npk = crop_summary[crop_summary.index=='watermelon']
values = [watermelon_npk['n'][0], watermelon_npk['p'][0], watermelon_npk['k'][0]]
fig.add_trace(go.Pie(labels=labels, values=values,name="Watermelon", marker_colors=cafe_colors),2, 4)

muskmelon_npk = crop_summary[crop_summary.index=='muskmelon']
values = [muskmelon_npk['n'][0], muskmelon_npk['p'][0], muskmelon_npk['k'][0]]
fig.add_trace(go.Pie(labels=labels, values=values,name="Muskmelon", marker_colors=cafe_colors),2, 5)
fig.update_layout(
    title_text="NPK ratio for fruits",
    annotations=[dict(text='Apple',x=0.06,y=1.08, font_size=15, showarrow=False),
                 dict(text='Banana',x=0.26,y=1.08, font_size=15, showarrow=False),
                 dict(text='Grapes',x=0.50,y=1.08, font_size=15, showarrow=False),
                 dict(text='Orange',x=0.74,y=1.08, font_size=15, showarrow=False),
                dict(text='Mango',x=0.94,y=1.08, font_size=15, showarrow=False),
                dict(text='Coconut',x=0.06,y=0.46, font_size=15, showarrow=False),
                 dict(text='Papaya',x=0.26,y=0.46, font_size=15, showarrow=False),
                 dict(text='Pomegranate',x=0.50,y=0.46, font_size=15, showarrow=False),
                 dict(text='Watermelon',x=0.74,y=0.46, font_size=15, showarrow=False),
                dict(text='Muskmelon',x=0.94,y=0.46, font_size=15, showarrow=False)])
fig.show()

crop_scatter =df[(df['crop']=='rice') | 
                      (df['crop']=='jute') | 
                      (df['crop']=='cotton') |
                     (df['crop']=='maize') |
                     (df['crop']=='lentil')]

fig = px.scatter(crop_scatter, x="temperature", y="humidity", color="crop", symbol="crop")
fig.update_layout(plot_bgcolor='white')
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False)

fig.show()



fig, ax = plt.subplots(1, 1, figsize=(15, 9))
sns.heatmap(df.corr(), annot=True,cmap='Wistia' )
ax.set(xlabel='features')
ax.set(ylabel='features')

plt.title('Correlation between different features', fontsize = 15, c='black')
plt.show()
"""

target=['crop']
features=['n','p','k','temperature','humidity','ph','rainfall','season']

X=df[features]
y=df[target]

from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain,Ytest = train_test_split(X, y, test_size = 0.3,
                                                    shuffle = True, random_state = 0)

# Initializing empty lists to append all model's name and corresponding name
acc = []
model = []

from sklearn.tree import DecisionTreeClassifier

DecisionTree = DecisionTreeClassifier(criterion="entropy",random_state=2,max_depth=5)

DecisionTree.fit(Xtrain,Ytrain)

predicted_values = DecisionTree.predict(Xtest)
x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('Decision Tree')
print("DecisionTrees's Accuracy is: ", x*100)

print(classification_report(Ytest,predicted_values))
"""
plt.figure(figsize = (15,9))
sns.heatmap(confusion_matrix(Ytest, predicted_values), annot = True)
plt.title("Confusion Matrix for Test Data")
plt.show()
"""

from sklearn.naive_bayes import GaussianNB

NaiveBayes = GaussianNB()

NaiveBayes.fit(Xtrain,Ytrain)

predicted_values = NaiveBayes.predict(Xtest)
x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('Naive Bayes')
print("Naive Bayes's Accuracy is: ", x*100)

print(classification_report(Ytest,predicted_values))
"""
plt.figure(figsize = (15,9))
sns.heatmap(confusion_matrix(Ytest,predicted_values), annot = True)
plt.title("Confusion Matrix for Test Data")
plt.show()
"""


from sklearn.svm import SVC

SVM = SVC(gamma='auto')

SVM.fit(Xtrain,Ytrain)

predicted_values = SVM.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('SVM')
print("SVM's Accuracy is: ", x*100)

print(classification_report(Ytest,predicted_values))
"""
plt.figure(figsize = (15,9))
sns.heatmap(confusion_matrix(Ytest,predicted_values), annot = True)
plt.title("Confusion Matrix for Test Data")
plt.show()
"""

from sklearn.linear_model import LogisticRegression

LogReg = LogisticRegression(random_state=2)

LogReg.fit(Xtrain,Ytrain)

predicted_values = LogReg.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('Logistic Regression')
print("Logistic Regression's Accuracy is: ", x*100)

print(classification_report(Ytest,predicted_values))
"""
plt.figure(figsize = (15,9))
sns.heatmap(confusion_matrix(Ytest,predicted_values), annot = True)
plt.title("Confusion Matrix for Test Data")
plt.show()
"""

from sklearn.ensemble import RandomForestClassifier

RF = RandomForestClassifier(n_estimators=20, random_state=0)
RF.fit(Xtrain,Ytrain)

predicted_values = RF.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('RF')
print("RF's Accuracy is: ", x*100)

print(classification_report(Ytest,predicted_values))
"""
plt.figure(figsize = (15,9))
sns.heatmap(confusion_matrix(Ytest,predicted_values), annot = True)
plt.title("Confusion Matrix for Test Data")
plt.show()




plt.figure(figsize=[10,5],dpi = 100)
plt.title('Accuracy Comparison')
plt.xlabel('Accuracy')
plt.ylabel('Algorithm')
sns.barplot(x = acc,y = model,palette='dark')
"""

accuracy_models = dict(zip(model, acc))
for k, v in accuracy_models.items():
    print (k, '-->', v)

data = np.array([[104,18, 30, 23.603016, 60.3, 6.7, 140.91,2]])
prediction = RF.predict(data)
print(prediction)

data = np.array([[90,42,43,20.87974371,82.00274423,6.502985292,202.9355362,2]])
prediction = RF.predict(data)
print(prediction)
le_season_map=dict(zip(le.classes_,le.transform(le.classes_)))
print(le_season_map)
pickle.dump(RF,open('model.pkl','wb'))
model1=pickle.load(open('model.pkl','rb'))
print(model1.score(Xtest,Ytest))


