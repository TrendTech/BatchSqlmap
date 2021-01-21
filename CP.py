import os
import re

if __name__ == "__main__":
    flagChange = "Yes"
    oldSession = "LoginSession=4ce772b130ab0dbb19861a10aedeae72b650a3d8"
    newSession = "LoginSession=d2b8da5a90b6bd3105e9de60a5ff672c2225760d"

    here = os.getcwd()
    interface_post_file = here+'\CP_Post_File'
    pathDir = os.listdir(interface_post_file)
    file_paths = []

    for allDir in pathDir:
        child = os.path.join('%s\%s' % (interface_post_file, allDir))
        if flagChange=='Yes':
            fOpen = open(child, 'r')
            w_str = ""
            for line in fOpen:
                if(re.search(oldSession,line)):
                    line = re.sub(oldSession, newSession, line)
                    w_str += line
                else:
                    w_str += line
            # print(w_str)
            print(child)
            wOpen = open(child,'w')
            wOpen.write(w_str)
            fOpen.close()
            wOpen.close()
        file_paths.append(child.encode().decode('gbk'))
    os.chdir('..')

    for file_path_index in range(len(file_paths)):
        wLog = open('D:\文档\PycharmProjects\BatchSqlmap\\temp_log.txt','w')
        print(wLog.name)
        wLog.write("start inject with file : %s \n" %file_paths[file_path_index])
        wLog.close()
        os.system('python c:/sqlmap/sqlmap.py -v 3 --dbms=postgresql --threads 10 --level=3 --timeout 10 -r %s --batch --output-dir ../PycharmProjects/BatchSqlmap/sqlmaplog'%file_paths[file_path_index])


    # final = ("D:\文档\PycharmProjects\BatchSqlmap\CP_Post_File\\getBalance").encode().decode('gbk')
    # os.system('python c:/sqlmap/sqlmap.py -v 3 --dbms=postgresql --threads 10 --level=3 --timeout 10 -r '
    # ' %s --batch --output-dir /sqlmaplog'%final)
