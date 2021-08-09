import os

fileName = 'student.txt'

def main():
    while True:
        menu()

        choice = int(input('请输入您的选择序号：'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                print("您确定要退出吗？y/n")
                answer = input()
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！！！')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()
        else:
            print('输入的序号不在范围内，请重新输入！！！')

def menu():
    print('==============================学生信息管理系统==============================')
    print('---------------------------------功能菜单----------------------------------')
    print('\t\t\t\t\t\t1. 录入学生信息')
    print('\t\t\t\t\t\t2. 查找学生信息')
    print('\t\t\t\t\t\t3. 删除学生信息')
    print('\t\t\t\t\t\t4. 修改学生信息')
    print('\t\t\t\t\t\t5. 排序')
    print('\t\t\t\t\t\t6. 统计学生总人数')
    print('\t\t\t\t\t\t7. 显示所有学生信息')
    print('\t\t\t\t\t\t0. 退出系统')
    print('--------------------------------------------------------------------------')

def save(lst):
    stu_txt = open(fileName, 'a', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()

def insert():
    student_list = []
    while True:
        id = input('请输入id(如1001):')
        if not id:
            break
        name = input('请输入姓名:')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入python成绩：'))
            java = int(input('请输入java成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        # 将录入的学生信息保存到字典中
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        # 将学生信息添加到列表中
        student_list.append(student)
        answer = input('是否继续添加？y/n\n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    # 保存学生信息到文件中
    save(student_list)
    print('学生信息录入完毕!!!')

def show_student(lst):
    # 传过来空列表
    if len(lst) == 0:
        print('没有查找到该生信息！')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^8}\t{:^8}\t{:^10}\t{:^10}\t{:^18}\t'
    print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'java成绩', '总成绩'))
    # 定义内容的显示格式
    format_data = '{:^6}\t{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^18}\t'
    for item in lst:
        sum = int(item['english']) + int(item['python']) + int(item['java'])
        print(format_data.format(item['id'], item['name'], \
                                 item['english'], item['python'], item['java'], \
                                 sum))

def search():
    while True:
        stu_query = []
        id = ''
        name = ''
        # 判断文件是否存在
        if os.path.exists(fileName):
            # 输入查询标号
            mode = input('按ID查找请按1，按姓名查找请按2：')
            if mode == '1':
                id = input('请输入要查找的学生id：')
            elif mode == '2':
                name = input('请输入要查找学生的姓名:')
            else:
                print('您的输入有误，请重新输入!')
                continue
            # 如果文件存在，并且用户输入了正确的查询标号，则打开文件
            with open(fileName, 'r', encoding='utf-8') as rfile:
                students = rfile.readlines()
            # 将读取到的信息转换为字典类型
            for item in students:
                d = dict(eval(item))
                if id != '':
                    if id == d['id']:
                        stu_query.append(d)
                elif name != '':
                    if name == d['name']:
                        stu_query.append(d)
            # 显示查询结果
            show_student(stu_query)
            # 是否查询其他学生信息
            answer = input('还要查询其他学生吗？y/n\n')
            if answer == 'y' or answer == 'y':
                continue
            else:
                break
        else:
            print('学生信息文件不存在！')
            return

def delete():
    while True:
        student_id = input('请输入要删除学生的id:')
        if student_id != '':
            if os.path.exists(fileName):
                with open(fileName, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记是否删除
            if student_old:
                with open(fileName, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转换为字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已经删除')
                    else:
                        print(f'学生表中没有找到id为{student_id}的学生')
            else:
                print('学生表中无任何学生信息')
                break
            show()  # 重新显示所有学生信息
            answer = input('是否继续删除？y/n\n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break

def modify():
    while True:
        # 展示学生信息
        show()
        # 如果原文件存在，打开原文件，读出所有信息
        if os.path.exists(fileName):
            with open(fileName, 'r', encoding='utf-8') as rfile:
                student_old = rfile.readlines()
        else:
            print('学生文件信息不存在！')
            return
        # 创建一个新的文件，读取之前文件中的每一个学生信息
        student_id = input('请输入要修改的学生id：')
        flag = False  # 标记是否在学生信息表中找到要修改的学生信息
        with open(fileName, 'w', encoding='utf-8') as wfile:
            for item in student_old:
                d = dict(eval(item))
                # 如果在原文件的某一行找到要修改的学生id，则对其进行修改
                if d['id'] == student_id:
                    print('找到学生信息，可以修改该生的相关信息')
                    while True:
                        try:
                            d['name'] = input('请输入姓名:')
                            d['english'] = input('请输入英语成绩:')
                            d['python'] = input('请输入python成绩:')
                            d['java'] = input('请输入java成绩:')
                            break
                        except:
                            print('您的输入有误，请重新输入!!!')
                    wfile.write(str(d) + '\n')
                    flag = True
                else:
                    wfile.write(str(d) + '\n')
        if flag:
            print('修改成功!!!')
        else:
            print('没有找到要修改学生的id!!!')
        # 询问是否要接着修改
        answer = input('是否修改其他学生信息？y/n\n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

def sort():
    show()
    # 判断文件是否存在，如果存在则打开文件，读取信息
    if os.path.exists(fileName):
        with open(fileName, 'r', encoding='utf-8') as rfile:
            students_list = rfile.readlines()
        students_new = []
        # 判断读取到的学生信息是否为空
        if students_list:
            # 将所有的item加入到students_new中
            for item in students_list:
                d = dict(eval(item))
                students_new.append(d)
            # 选择升序or降序
            asc_or_desc = input('请选择(0为升序，1为降序):')
            if asc_or_desc == '0':
                asc_or_desc_bool = False
            elif asc_or_desc == '1':
                asc_or_desc_bool = True
            else:
                print('您的输入有误，请重新输入')
                sort()
            # 选择按照什么成绩排序
            mode = input('请选择排序方式（1.按英语成绩排序   2.按python成绩排序   \
                        3.按java成绩排序   0.按总成绩排序):')
            if mode == '1':
                students_new.sort(key=lambda x: int(x['english']), reverse=asc_or_desc_bool)
            elif mode == '2':
                students_new.sort(key=lambda x: int(x['python']), reverse=asc_or_desc_bool)
            elif mode == '3':
                students_new.sort(key=lambda x: int(x['java']), reverse=asc_or_desc_bool)
            elif mode == '0':
                students_new.sort(key=lambda x: int(x['english']) + int(x['python']) + int(x['java']), \
                                  reverse=asc_or_desc_bool)
            else:
                print('您的输入有误，请重新输入！！！')
                sort()
            # 将排序后的成绩进行输出
            show_student(students_new)
        else:
            print('学生文件中还没有录入学生信息！')
    else:
        print('学生文件不存在！')
        return

def total():
    # 判断文件是否存在，如果存在则打开文件，读取信息
    if os.path.exists(fileName):
        with open(fileName, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            # 判断读取到的学生信息是否为空
            if students:
                print('一共有{}名学生'.format(len(students)))
            else:
                print('学生文件中还没有录入学生信息！')
    else:
        print('学生文件不存在！')
        return

def show():
    student_list = []
    # 判断文件是否存在，如果存在则打开文件，读取信息
    if os.path.exists(fileName):
        with open(fileName, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            # 判断读取到的学生信息是否为空
            if students:
                for item in students:
                    student_list.append(eval(item))
                # 展示学生信息
                show_student(student_list)
            else:
                print('学生文件中还没有录入学生信息！')
    else:
        print('学生文件不存在！')
        return

if __name__ == '__main__':
    main()
