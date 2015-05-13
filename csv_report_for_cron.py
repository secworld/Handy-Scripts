#! /usr/bin/env python
#  
#  Coded By H4Wk
#  

from collections import OrderedDict
import shutil
import csv
import time
 
def csv_func(file_obj):
    
    path = "Unfixed_Vulneranilities.csv"
    reader = csv.DictReader(file_obj, delimiter=',')
    list_data = []
    for line in reader:
		status = line["Open Status"]
		severe = line["Severity"]
		titl = line["Title"]
		ip = line["IP Address"]
		sol = line["Solution"]
		rslt = line["Result"]
		tym = line["Scheduled Scan Time"]
		if status == "Open" and severe == "High":
			data = [tym,ip,titl,severe,status,rslt,sol]
			list_data.append(data)
			#print(line["Title"]),
			#print(line["Severity"]),
			#print(line["Open Status"]),
			#print "\n"
    my_list = []
    #print list_data[0]
    #print list_data [1]
    fields = OrderedDict([('Scan Time',None),('IP Address',None),('Title',None),('Severity',None),('Status',None),('Result',None),('Solution',None)])
    for values in list_data[0:]:
		inner_dict = dict(zip(fields, values))
		my_list.append(inner_dict)
		with open (path, "wb") as out_file:
			writer = csv.DictWriter(out_file, delimiter=",", fieldnames = fields)
			writer.writeheader()
			for row in my_list:
				print row
				writer.writerow(row)
 
    
 
if __name__ == "__main__":
	print "\n\n"
	input_path = raw_input("Please Enter the path of the input report  :  ")
	with open("%s" %input_path) as file_obj:
		csv_func(file_obj)
print "\n\n"
print ("Please Wait.. Generating Report ....")

# --------Please change the source and destination path accordingly-----------

src_file = "/home/user/Desktop/Indusind/Scripts/xml_report/Unfixed_Vulneranilities.csv"
dst_file = "/home/user/Desktop/"#Please change accorgingly
shutil.copy(src_file, dst_file)
print ("The file can be found on your Desktop")
time.sleep(5)
