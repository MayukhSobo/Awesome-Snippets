def plot_most_common(data, n, column, filter_by_class=True, **kwargs):
    # Remove any NaN values in the column
    d = data[~data[column].isna()]
    if kwargs.get('make_copy', True):
        data_f = d.copy()
    else:
        data_f = d
    target_col = kwargs['target']
    if filter_by_class:
        # Plot for a particular class
        target_val = kwargs['target_val']
        data_f = data_f[data_f[target_col] == target_val]
        c = Counter(data_f[column])
        plot_data = pd.DataFrame(c.most_common(n))
        plot_data.columns = [column, 'count']
        ax = sns.barplot(x='count', y=column, data=plot_data, palette=kwargs.get('palette', 'Blues_r'))
        plt.title(kwargs.get('title'))
        return ax
    else:
        # Plot for both the classes combined
        both_target = kwargs.get('both_target', [0, 1])
        data_f_0 = data_f[data_f[target_col] == both_target[0]]
        data_f_1 = data_f[data_f[target_col] == both_target[1]]
        c1 = Counter(data_f_0[column])
        c2 = Counter(data_f_1[column])
        plot_data = pd.DataFrame([c1, c2]).T
        if kwargs['handle_singular'] == 'drop':
            plot_data = plot_data.dropna().reset_index()
        elif kwargs['handle_singular'] == 'fill':
            plot_data = plot_data.fillna(value=0).reset_index()
        
        plot_data.columns = [column, both_target[0], both_target[1]]
        plot_data = plot_data.sort_values(by=[1, 0], ascending=[False, True]).head(n)
        out = pd.melt(plot_data, id_vars=column, var_name='class', value_name='count')
        out['count'] = out['count'].astype(int)
        ax = sns.barplot(x='keyword', y='count', hue='class', data=out, palette=['tomato', 'cornflowerblue'])
        return ax