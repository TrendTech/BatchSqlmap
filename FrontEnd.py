import os
import re

if __name__ == "__main__":
    flagChange = "Yes"
    newSession = "JSESSIONID=CDA1E5E5F6339AC1AC60C83E3B56E751"
    oldSession = "JSESSIONID=86303F7575BA4332C5BBA216554AC3F1"

    here = os.getcwd()
    interface_post_file = here+'\FrontEnd_Post_File'
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
            print(w_str)
            wOpen = open(child,'w')
            wOpen.write(w_str)
            fOpen.close()
            wOpen.close()
        file_paths.append(child.encode().decode('gbk'))
    os.chdir('..')

    for file_path_index in range(len(file_paths)):
        os.system('python c:/sqlmap/sqlmap.py -v 3 --dbms=postgresql --threads 10 --level=3 --timeout 10 -r %s --batch --output-dir ../PycharmProjects/BatchSqlmap/sqlmaplog'%file_paths[file_path_index])

    # final = ("D:\文档\PycharmProjects\BatchSqlmap\FrontEnd_Post_File\\memberCentre").encode().decode('gbk')
    # os.system('python c:/sqlmap/sqlmap.py -v 3 --dbms=postgresql --threads 10 --level=3 -r '
    #           ' %s --batch'%final)