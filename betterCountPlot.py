def plot_most_common(data, n, column, filter_by_class=True, **kwargs):
    # Remove any NaN values in the column
    d = data[~data[column].isna()]
    if kwargs.get('make_copy', True):
        data_f = d.copy()
    else:
        data_f = d
    if filter_by_class:
        # Plot for a particular class
        target_col = kwargs['target']
        target_val = kwargs['target_val']
        data_f = data_f[data_f[target_col] == target_val]
    else:
        # Plot for all the class
        pass

    c = Counter(data_f[column])
    plot_data = pd.DataFrame(c.most_common(n))
    plot_data.columns = [column, 'count']
    sns.barplot(x='count', y=column, data=plot_data, palette=kwargs.get('palette', 'Blues_r'))
    plt.show()