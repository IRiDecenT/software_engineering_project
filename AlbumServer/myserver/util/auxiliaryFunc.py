import os

# 删除头像文件
def check_and_delete(*, id, mainPath):
    # 检查文件夹是否存在
    # 如果存在，删除文件夹
    # 如果不存在，不做任何操作
    file_list = os.listdir(mainPath)
    for file_name in file_list:
        # 找1-开头的文件，找到即删除
        if file_name.startswith(f'{id}-'):
            file_path = os.path.join(mainPath, file_name)
            os.remove(mainPath + file_name)
            print('删除文件', file_path)
            return True
