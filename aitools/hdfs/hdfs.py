def file_down(host,user_name,local_path,hdfs_path):
    print("file download from {} to {} start ......".format(hdfs_path,local_path))
    fs = pyhdfs.HdfsClient(hosts=host,user_name=user_name)
    fs.copy_to_local(hdfs_path,local_path)
    print("file download from {} to {} finish ......".format(hdfs_path,local_path))

def download_hdfs_csv(hdfs_path, local_path, prefix='part'):
    mkdir(local_path)
    lists = fs.listdir(hdfs_path)
    idx = 0
    for item in lists:
        if item.endswith('.csv'):
            local_csv_path = '{}{}_{}.csv'.format(local_path, prefix, idx)
            idx += 1
            file_down(
                host=host,
                user_name=user_name,
                local_path= local_csv_path,
                hdfs_path= hdfs_path + item
            )