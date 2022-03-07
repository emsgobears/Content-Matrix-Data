
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(0)
content_data="https://raw.githubusercontent.com/emsgobears/Content-Matrix-Data/main/datatest2.txt"
# load awareness score and emotion score of each type of communcation content
df = pd.read_csv(content_data, sep="\t")
df.head()
x=df.Awareness
y=df.Emotion
colors = {'Entertain':'yellow', 'Educate':'green', 'Persuade':'blue', 'Convert':'purple'}
plt.scatter(x,y, c= df['Category'].map(colors),
            cmap='viridis')
plt.xlabel("Rational --> Emotional", fontweight ='semibold',  size=12)
plt.ylabel("Conversion --> Awareness", fontweight ='semibold', size=12)
plt.title('Interesting Graph\nThe Content Matrix')
plt.text(1, 1, "Convert", fontsize=10)
# add annotations one by one with a loop
for i in range(0,df.shape[0]):
     plt.text(x[i]+0.2, y[i]-0.3, T[i], horizontalalignment='right', size=6, color='grey')

plt.colorbar();  
plt.show()
