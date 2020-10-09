
def radar1(
        features, values, title,
        title_size=20, radar_range=(0, 1), label_fontsize=12, figsize=(8, 8)):
    N = len(values)
    # 设置雷达图的角度，用于平分切开一个圆面
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
    # 为了使雷达图一圈封闭起来，需要下面的步骤
    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    # 绘图
    fig = plt.figure(figsize=figsize)
    # 这里一定要设置为极坐标格式
    ax = fig.add_subplot(111, polar=True)
    # 绘制折线图
    ax.plot(angles, values, 'o-', linewidth=2)
    # 填充颜色
    ax.fill(angles, values, alpha=0.25)
    # 添加每个特征的标签
    ax.set_thetagrids(angles[:-1] * 180 / np.pi, features, fontsize=label_fontsize)
    # 设置雷达图的范围
    ax.set_ylim(radar_range[0], radar_range[1])
    # 添加标题
    plt.title(title, fontdict={'fontsize': title_size})
    # 添加网格线
    ax.grid(True)
    # 显示图形
    plt.show()


def radarN(features: list, values: np.ndarray, labels, title,
           title_size=20, radar_range=(0, 1), figsize=(8, 8)):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, polar=True)
    N = values.shape[1]

    # 设置雷达图的角度，用于平分切开一个圆面
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
    angles = np.concatenate((angles, [angles[0]]))
    for vs, label in zip(values, labels):
        # 为了使雷达图一圈封闭起来，需要下面的步骤
        vs = np.concatenate((vs, [vs[0]]))
        # 绘图
        # 绘制折线图
        ax.plot(angles, vs, 'o-', linewidth=2, label=label)
        # 填充颜色
        ax.fill(angles, vs, alpha=0.25)

    # 添加每个特征的标签
    ax.set_thetagrids(angles[:-1] * 180 / np.pi, features, fontsize = 12)
    # 设置雷达图的范围
    ax.set_ylim(radar_range[0], radar_range[1])
    # 添加标题
    plt.title(title, fontdict={'fontsize': title_size})
    # 添加网格线
    ax.grid(True)
    # 设置图例
    plt.legend(loc='best')
    # 显示图形
    plt.show()