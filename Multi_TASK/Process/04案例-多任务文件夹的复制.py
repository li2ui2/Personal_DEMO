import os
import multiprocessing


def copy_file(q, file_name, old_folder_name, new_folder_name):
    """完成文件的复制"""
    # print("模拟copy文件,从%s到%s，文件名是%s" % (file_name, old_folder_name, new_folder_name))

    old_f = open("F:\\Workspace\\PycharmProject\\Multi_TASK\\Process\\" + old_folder_name + "\\" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open("F:\\Workspace\\PycharmProject\\Multi_TASK\\Process\\" + new_folder_name + "\\" + file_name, "wb")
    new_f.write(content)
    new_f.close()

    # 如果拷贝完了文件，那么就向队列中写入一个消息，表示已经完成
    q.put(file_name)


def main():
    # 1.获取用户用copy的文件夹名字
    old_folder_name = input("请输入要copy的文件夹的名字：")

    # 2.创建一个新的文件夹
    new_folder_name = old_folder_name + "[复件]"
    try:
        os.mkdir("F:\\Workspace\\PycharmProject\\Multi_TASK\\Process\\" + old_folder_name + "[复件]\\")
    except Exception:
        pass

    # 3.获取文件夹中所有待copy的文件名字：listdir()
    file_names = os.listdir(old_folder_name)
    print(file_names)

    # 4.创建进程池
    po = multiprocessing.Pool(5)

    # 5.创建一个队列，用于进程间的通信
    q = multiprocessing.Manager().Queue()  # 有进程池时通过这种方法创建队列

    # 6.向进程池中添加copy文件的任务
    # 复制原文件夹中的文件，到新的文件夹中文件去
    # po.map(copy_file, file_names)
    for file_name in file_names:
        po.apply_async(copy_file, args=(q, file_name, old_folder_name, new_folder_name))
    po.close()
    # po.join()
    all_file_num = len(file_names)  # 测试一下所有文件的个数
    copy_complete_num = 0
    while True:
        # file_name = q.get()
        # print("已经完成copy：%s" % file_name)
        copy_complete_num += 1
        print("\r拷贝进程为：%.3f%%" % (copy_complete_num*100/all_file_num), end="")
        if copy_complete_num >= all_file_num:
            break


if __name__ == "__main__":
    main()
