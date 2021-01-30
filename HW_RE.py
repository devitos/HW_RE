import re
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)
new_list = list()


for contact in contacts_list:

    pattern = re.compile("(\+7|8)\s*[\(\s*]?(\d{3})[\)\s*\-*]?\s*(\d{3})[-\s]?(\d{2})[-\s]?(\d+)")
    contact[5] = pattern.sub(r"+7(\2)\3-\4-\5", contact[5])
    fio = contact[0] + ' ' + contact[1] + ' ' + contact[2]
    pattern2 = re.compile("^([\wа-яА-ЯёЁ]+)[\s*\,?]([\wа-яА-ЯёЁ]+)[\s*\,?]([\wа-яА-ЯёЁ]+)?")
    new_fio = pattern2.sub(r"\1 \2 \3 ", fio)
    contact[0] = new_fio.split(' ')[0]
    contact[1] = new_fio.split(' ')[1]
    contact[2] = new_fio.split(' ')[2]
    new_list.append(contact)


for i in range(len(new_list)):
    n = 0
    for cont in new_list:
        # print(cont)
        if cont[0] == new_list[i-1][0] and cont[1] == new_list[i-1][1]:
            n += 1
            if n >= 2:
                for m in range(2, len(cont)-1):
                    if cont[m] == '':
                        cont[m] = new_list[i-1][m]


with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_list)
