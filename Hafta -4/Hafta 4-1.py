#hafta 4-1

#import os
#os.getcwd()

def get_words(my_file=u"C:\Users\Emre Ekinci\Documents\data_files\1.txt"):

    my_list=[]
    f=open(my_file,"r+")
    contents=f.readlines()
    for line in contents:
        #print(line) #noktalardan sonra cümleleri ayırıyoruz.(spirit fonk. gibi bir nevi..)**
        words=line.split(" ")
        for word in words:  #Kelimeleri listede dolaşırken tek tek alt alta yazıyoruz.
            #print(word)
            my_list.append(word) #Kaç kelime olduğunu yazdı.
    #print(contents) #string parse for phyton
    f.close()
    return my_list

def get_hist(my_list):
    my_hist={}
    for w in my_list:
        if w in my_hist.keys():
            my_hist[w]=my_hist[w]+1
        else:
            my_hist[w]=1
    return my_hist


def get_files(path_1):
    file_s = [file for file in my_list if os.path.isfile(file)]
    return file_s

lst_1=get_words()
get_hist(lst_1)

import os
my_list=os.listdir()

for item in my_list:
    if os.path.isdir(item):
        print(item)
    if os.path.isfile(item):
        print(item)
#Her şeyi daha net görebilmek için aşağıdaki gibi..
dir_s =[dir for dir in my_list if os.path.isdir(dir)]    #dizileri almak için
file_s=[file for file in my_list if os.path.isfile(file)]  #dosyaları almak için

dir_s,file_s