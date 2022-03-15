import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

def visual(test_accs, confusion_mtxes, labels, figsize=(10, 4)):
    
    cm = confusion_mtxes[np.argmax(test_accs)]
    cm_sum = np.sum(cm, axis=1, keepdims=True)
    cm_perc = cm / cm_sum * 100
    annot = np.empty_like(cm).astype(str)
    nrows, ncols = cm.shape
    for i in range(nrows):
        for j in range(ncols):
            c = cm[i, j]
            p = cm_perc[i, j]
            if c == 0:
                annot[i, j] = ''
            else:
                #annot[i, j] = '%.1f%%' % p
                annot[i, j] = ''
    cm = pd.DataFrame(cm, index=labels, columns=labels)
    cm.index.name = 'Actual'
    cm.columns.name = 'Predicted'
    
    fig = plt.figure(figsize=figsize)
    plt.subplot(1, 2, 1)
    plt.xlabel('Epoch')
    plt.ylabel('Test Accuracy (%)')
    plt.plot(test_accs, 'b')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    sns.heatmap(cm, annot=False, cbar=True, fmt='', cmap="Blues")
    plt.show()