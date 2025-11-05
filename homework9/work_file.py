import os

check_os = os.name
if check_os == 'posix':
    print("1) На компьютере Unix подобная ОС: linux или MacOS")
elif check_os == 'nt':
    print("1) На компьюте ОС Windows")
else:
    print("1) Какая-то ошибка")

print("2) Текущее положение:", os.getcwd())
print("Название папки:", os.path.basename("experiment_derictory"))
files = os.listdir(os.getcwd())
print("Файла имеющиеся в папке:", files)


if os.path.exists("folder_with_py") and os.path.exists("folder_with_txt"):
    print("Две папки уже созданы")
elif not os.path.exists(folder_with_txt) and os.path.exists(folder_with_py):
    print(os.mkdir("folder_with_txt"))
    print("Папка folder_with_py уже есть")
elif os.path.exists(folder_with_txt) and not os.path.exists(folder_with_py):
    print(os.mkdir("folder_with_py"))
    print("Папка folder_with_txt уже есть")
else:
    print(os.mkdir("folder_with_txt"))
    print(os.mkdir("folder_with_py"))


change_file = "file_one.txt"
new_place = "folder_with_txt"
join_file_and_place = os.path.join(change_file, new_place)
if os.path.exists(change_file):
    os.replace(change_file, new_place)
    size_one = os.path.getsize(join_file_and_place)
else:
    print("file_one.txt уже перемещен")

change_file = "file_two.py"
new_place = "folder_with_py"
join_file_and_place = os.path.join(change_file, new_place)
if os.path.exists(change_file):
    os.replace(change_file, new_place)
    size = os.path.getsize(join_file_and_place)
else:
    print("file_two.py уже перемещен")

change_file = "file_three.txt"
new_place = "folder_with_txt"
join_file_and_place = os.path.join(change_file, new_place)
if os.path.exists(change_file):
    os.replace(change_file, new_place)
    size = os.path.getsize(join_file_and_place)
else:
    print("file_three.txt уже перемещен")

change_file = "file_four.py"
new_place = "folder_with_txt"
join_file_and_place = os.path.join(change_file, new_place)
if os.path.exists(change_file):
    os.replace(change_file, new_place)
    size = os.path.getsize(join_file_and_place)
else:
    print("file_four.py уже перемещен")


files_first_fold = os.listdir("folder_with_txt")
files_second_fold = os.listdir("folder_with_py")
print("3) Файлы имеющиеся в папке folder_with_txt:", files_first_fold)
print("3) Файлы имеющиеся в папке folder_with_py:", files_second_fold)


all_size = 0

for dirpath, dirnames, filenames in os.walk("folder_with_txt"):
    for i in filenames:
        file_path = os.path.join(dirpath, i)
        all_size = all_size + os.path.getsize(file_path)

all_size_py = 0

for dirpath, dirnames, filenames in os.walk("folder_with_py"):
    for i in filenames:
        file_path = os.path.join(dirpath, i)
        all_size_py = all_size_py + os.path.getsize(file_path)

print(f"4) В папку с текстровыми файлами было перемещено {len(files_first_fold)} файл(a)ов, их суммарный размер - {all_size} байт")
print(f"4) В папку с файлами для python было перемещено {len(files_second_fold)} файл(a)ов, их суммарный размер - {all_size_py} байт")

os.chdir("folder_with_py")

old_name = "file_four.py"
new_name = "new_file_four.py"
if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"6) Файл {old_name} был переименован в {new_name}")
elif os.path.exists(new_name):
    print(f"6) Файл {old_name} уже ранее был переименован в {new_name}")
else:
    print("Какая-то ошибка")

































