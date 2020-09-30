__default_displays = 10


def show_columns(num=None):
    pd.set_option('display.max_columns', num)


def show_all_columns():
    show_columns(num=None)


def show_default_columns():
    show_columns(num=__default_displays)


def float_format_e():
    pd.set_option('display.float_format', lambda x: '%e' % x)


def float_format_f():
    pd.set_option('display.float_format', lambda x: '%.3f' % x)


def show_rows(num=None):
    pd.set_option('display.max_rows', num)


def show_default_rows():
    show_rows(num=__default_displays)


def show_all_rows():
    show_rows(num=None)


def shrink_data(df):
    for i, v in zip(df.dtypes.index, df.dtypes.values):
        vname = v.name
        if 'float' in vname:
            df[i] = df[i].astype('float32')
        if 'int' in vname:
            df[i] = df[i].astype('int32')
    return df


def clip_quantile(s, lo, hi):
    q_lo = np.percentile(s, lo)
    q_hi = np.percentile(s, hi)
    return ((s > q_lo) & (s < q_hi)).tolist()


def select_dtype_col(df, dtypes):
    res = []
    for t in dtypes:
        for i, v in zip(df.dtypes.index, df.dtypes.values):
            vname = v.name
            if t in vname:
                res.append(i)
    return res
