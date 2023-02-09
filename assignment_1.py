import os
file_size_sum = 0
for (current_path,dir_names,file_names) in os.walk("/home/alisalamati/Desktop/sharif_prc/"):
   for add_to_path in file_names:
      file_size_sum += os.stat(str(current_path) + "/"+ str(add_to_path)).st_size
print("total file size is: ")
print(file_size_sum)