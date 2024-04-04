import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import seaborn as sns
import matplotlib.pyplot as plt

  
  
# actual    =['elon_musk','elon_musk', 'elon_musk', 'elon_musk' ,'elon_musk' ,'elon_musk',
#  'elon_musk', 'elon_musk', 'elon_musk' ,'elon_musk']
# predicted =['elon_musk' ,'elon_musk' ,'elon_musk', 'elon_musk', 'elon_musk', 'elon_musk',
#  'unknown', 'elon_musk' ,'elon_musk' ,'elon_musk']



actual    =['elon_musk', 'elon_musk', 'elon_musk', 'elon_musk', 'elon_musk', 'elon_musk', 'elon_musk', 'elon_musk', 'elon_musk', 'elon_musk','unknown']
predicted =['elon_musk', 'elon_musk', 'elon_musk', 'elon_musk', 'elon_musk', 'elon_musk', 'unknown', 'elon_musk', 'elon_musk', 'elon_musk','unknown']


labels=["elon_musk","unknown"]
# labels.reverse()
cm = confusion_matrix(actual,predicted,labels=labels)
print(cm)
# exit()

sns.heatmap(cm, 
			annot=True,
			fmt='g', 
			xticklabels=['elon_musk','Not elon_musk'],
			yticklabels=['elon_musk','Not elon_musk'])
plt.ylabel('Actual',fontsize=13)
plt.xlabel('Prediction',fontsize=13)
plt.title('Confusion Matrix',fontsize=17)
plt.show()
print(classification_report(actual, predicted))


