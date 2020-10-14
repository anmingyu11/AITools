def dist_plot(series, title, figsize=(12, 6), bins=None):
    if bins is None:
        bins = min(100, len(series.unique()))
    plt.figure(figsize=figsize)
    sns.histplot(series, bins=bins, kde=True)
    plt.title(title, fontdict={'fontsize': 18})
    plt.show()
