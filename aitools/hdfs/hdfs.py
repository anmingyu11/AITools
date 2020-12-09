def file_down(host, user_name, local_path, hdfs_path):
    print("file download from {} to {} start ......".format(hdfs_path, local_path))
    fs = pyhdfs.HdfsClient(hosts=host, user_name=user_name)
    fs.copy_to_local(hdfs_path, local_path)
    print("file download from {} to {} finish ......".format(hdfs_path, local_path))


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
                local_path=local_csv_path,
                hdfs_path=hdfs_path + item
            )

class PackageHdfs():

    def __init__(self):
        self.fs = pyhdfs.HdfsClient('192.168.200.19:50070')

    # 删除
    def delFile(self, path):
        fs = self.fs
        fs.delete(path)

    # 上传文件
    def upload(self, fileName, tmpFile):
        fs = self.fs
        fs.copy_from_local(fileName, tmpFile)

    def download(self, local_path, hdfs_path):
        fs = self.fs
        fs.copy_to_local(hdfs_path, local_path)

    # 新建目录
    def mkdir(self, filePath):
        fs = self.fs
        if not fs.exists(filePath):
            # os.system('hadoop fs -mkdir '+filePath)
            fs.mkdirs(filePath)
            return 'mkdir'
        return 'exits'

    # 重命名
    def rename(self, srcPath, dstPath):
        fs = self.fs
        if not fs.exists(srcPath):
            return
        fs.rename(srcPath, dstPath)