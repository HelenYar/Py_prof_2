import io
import re
import csv

def read_file(file_name):
  with io.open(file_name, encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
  return contacts_list

def format_number(contacts_list):
  contacts_list_=[]
  for contact in contacts_list:
    contact_str = ','.join(contact)
    f_contact_ = re.sub(r"(\s|\s\()(доб\W)\s?(\d{4})\)?", r" \2\3", contact_str)
    f_contact = re.sub(r"(\+7|8)?[\(\s-]*?(\d{3})?[\)\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})", r"+7(\2)\3-\4-\5", f_contact_)
    contacts_as_list = f_contact.split(',')
    contacts_list_.append(contacts_as_list)
  contacts_list = sorted(contacts_list_)
  return contacts_list


def format_name(contacts_list):
  list = []
  for cl in contacts_list:
    lfs = ("".join(f'{cl[0]} {cl[1]} {cl[2]}').replace("  ", " "))
    list_name = (lfs.split())
    if len(list_name) != 3:
      list_name = (lfs.split(" "))
    list_name.append(f'{cl[3]}')
    list_name.append(f'{cl[4]}')
    list_name.append(f'{cl[5]}')
    list_name.append(f'{cl[6]}')
    list.append(list_name)
  return list

def join_duplicates(list):
  list_csv = []
  x = ''
  for l in list:
    lfs = ("".join(f'{l[0]} {l[1]}').replace("  ", " "))
    if re.search(lfs, x) == None:
      list_csv.append(l)
    else:
      if list_csv[-1][2] == '':
        s1 = l[2]
      else:
        s1 = list_csv[-1][2]
      if list_csv[-1][3] == '':
        o1 = l[3]
      else:
        o1 = list_csv[-1][3]
      if list_csv[-1][4] == '':
        p1 = l[4]
      else:
        p1 = list_csv[-1][4]
      if list_csv[-1][5] == '':
        ph_1 = l[5]
      else:
        ph_1 = list_csv[-1][5]
      if list_csv[-1][6] == '':
        e1 = l[6]
      else:
        e1 = list_csv[-1][6]

      list1 = []
      list1.append(list_csv[-1][0])
      list1.append(list_csv[-1][1])
      list1.append(s1)
      list1.append(o1)
      list1.append(p1)
      list1.append(ph_1)
      list1.append(e1)

      del (list_csv[-1])
      list_csv.append(list1)
    x = lfs
  return list_csv


def write_file(list_csv):
  with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(list_csv)

if __name__ == '__main__':
    contacts = read_file('phonebook_raw.csv')
    contacts = format_number(contacts)
    contacts = format_name(contacts)
    contacts = join_duplicates(contacts)
    write_file(contacts)
