import matplotlib.pyplot as plt
import seaborn as sns


def dist_plot(series, title, figsize=(12, 6), bins=None):
    if bins is None:
        bins = min(100, len(series.unique()))
    plt.figure(figsize=figsize)
    sns.histplot(series, bins=bins, kde=True)
    plt.title(title, fontdict={'fontsize': 18})
    plt.show()


def heatmap1(df, title='Correlation Heatmap', fontsize=12, figsize=(16, 6)):
    # Increase the size of the heatmap.
    plt.figure(figsize=figsize)
    # Store heatmap object in a variable to easily access it when you want to include more features (such as title).
    # Set the range of values to be displayed on the colormap from -1 to 1, and set the annotation to True to display the correlation values on the heatmap.
    heatmap = sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True)
    # Give a title to the heatmap. Pad defines the distance of the title from the top of the heatmap.
    heatmap.set_title(title, fontdict={'fontsize': fontsize}, pad=12)
    plt.show()


def heatmap2(df, title='Correlation Heatmap', fontsize=18, figsize=(16, 6)):
    plt.figure(figsize=figsize)
    heatmap = sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True, cmap='BrBG')
    heatmap.set_title(title, fontdict={'fontsize': fontsize}, pad=12)
    # save heatmap as .png file
    # dpi - sets the resolution of the saved image in dots/inches
    # bbox_inches - when set to 'tight' - does not allow the labels to be cropped
    # save
    # plt.savefig('heatmap.png', dpi=300, bbox_inches='tight')
    plt.show()


def heatmap3(df, title='Triangle Correlation Heatmap', fontsize=18, figsize=(16, 6)):
    plt.figure(figsize=figsize)
    # define the mask to set the values in the upper triangle to True
    mask = np.triu(np.ones_like(df.corr(), dtype=np.bool))
    heatmap = sns.heatmap(
        df.corr(), mask=mask, vmin=-1, vmax=1, annot=True, cmap='BrBG')
    heatmap.set_title(title, fontdict={'fontsize': fontsize}, pad=16)
    plt.show()
