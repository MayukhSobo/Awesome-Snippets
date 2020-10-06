import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def display_preformance(history):
    data = pd.DataFrame({
                         'epoch': range(1, len(history.history['val_loss']) + 1), 
                         'validation_loss': history.history['val_loss'],
                         'training_loss': history.history['loss']
                        })
    loss_data = pd.melt(data, 
                   var_name='loss_type', 
                   value_name='loss_value', 
                   id_vars='epoch')

 

    data = pd.DataFrame({
                         'epoch': range(1, len(history.history['val_loss']) + 1),
                         'validation_accuracy': history.history['val_acc'],
                         'training_accuracy': history.history['acc']
                        })

 

    accuracy_data = pd.melt(data, 
                   var_name='acc_type', 
                   value_name='acc_value', 
                   id_vars='epoch')

 

    sns.set(rc={'figure.figsize':(12, 6)})

 

    plt.subplot(121)
    sns.lineplot(x='epoch', y='loss_value', hue='loss_type', 
                 data=loss_data, lw=2);
    plt.title('Loss vs Epoch', fontsize=18);
    plt.subplot(122)
    sns.lineplot(x='epoch', y='acc_value', hue='acc_type', 
                 data=accuracy_data, lw=2);
    plt.title('Accuracy vs Epoch', fontsize=18);
    plt.show()