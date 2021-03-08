def rename_columns(df, columns):
    if not isinstance(columns, dict):
        raise ValueError("'columns' should be a dict, like {'old_name_1':'new_name_1', 'old_name_2':'new_name_2'}")

    for old_name, new_name in columns.items():
        df = df.withColumnRenamed(old_name, new_name)

    return df


def word_count(rdd):
    return rdd.map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b)


def get_partitions(sql, table_name):
    partitions = sql('show partitions {}'.format(table_name)).collect()
    partitions = [pt['partition'] for pt in partitions]
    partitions = [pt.split('=')[1] for pt in partitions]
    return partitions


def get_partitions2(tb):
    partitions = f.sql('show partitions {}'.format(tb)).collect()
    partitions = [pt['partition'] for pt in partitions]
    partitions = [pt.split('=')[1] for pt in partitions]
    partitions = sorted(partitions)
    partitions.reverse()
    return partitions


def show_null(df):
    df.select(*(functions.sum(functions.col(c).isNull().cast("int")).alias(c) for c in df.columns)).show()

def table_exists(table_name):
    if '.' not in table_name:
        raise Exception("must format like '*.*'")

    database_list = f.sql('show databases').toPandas()['namespace'].values.tolist()
    db_tb = {}

    for e_db in database_list:
        tables = f.sql("show tables in {}".format(e_db)).toPandas()['tableName'].values.tolist()
        db_tb[e_db] = tables

    splits = table_name.split('.')
    if len(splits) != 2:
        raise Exception('InCorrect formation {}'.format(table_name))

    o_db_name = splits[0]
    o_tb_name = splits[1]

    if o_db_name not in db_tb:
        display('db {} not exists'.format(o_db_name))
        return False

    return (o_db_name in db_tb) and (o_tb_name in db_tb[o_db_name])

def split_vector(df,vec_col_name):
    df\
        .withColumn("vecs", vector_to_array(vec_col_name))\
        .select(["word"] + [col("vecs")[i] for i in range(3)])

def alter_partition(table_name, dt):
    partitions = load_partitions(table_name)
    if dt in partitions:
        display('dt has exists')
        f.sql("alter table {} drop if exists partition (dt='{}')".format(table_name, dt))