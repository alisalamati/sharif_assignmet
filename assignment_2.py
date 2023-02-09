# importing libraries
import datetime
import time
import calendar
import sys
import os

input_user = sys.argv[1] #input from user str type
input_date_conv = datetime.datetime.strptime(input_user, "%Y-%m-%d") #convert str type to datetime type
file_mtime_dict = {} #dictionry to store file with modifed time
file_finall_lst = [] #list for all file modified after input date 

input_date_epoch = calendar.timegm(input_date_conv.timetuple()) #convert input date to epoch 

for (curr_dir, dir_lst, file_lst) in os.walk("/home/alisalamati/Desktop/sharif_prc/"):
   for file_name in file_lst:
      file_path = os.path.join(curr_dir,file_name)
      file_mtime = os.stat(file_path).st_mtime
      file_mtime_dict[file_name] = file_mtime
   
for m_time_key in file_mtime_dict:
   if file_mtime_dict[m_time_key] > input_date_epoch:  #check file mtime from input mtime
      file_finall_lst.append(m_time_key) #add to finall lst

print(file_finall_lst)      #print all file modified after the input date 