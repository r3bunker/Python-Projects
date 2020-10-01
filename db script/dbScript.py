
import sqlite3

conn=sqlite3.connect('script.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_txtFile TEXT \
        )") #creates table with an ID and txtFile column
    conn.commit()
conn.close()



def scanFiles(fileList):
    

    conn = sqlite3.connect('script.db')


    with conn:
        cur = conn.cursor()
        for i in fileList:
            if i.endswith('.txt'):
                print(i)
                cur.execute("INSERT INTO tbl_files(col_txtFile) VALUES (?)", (i,))
        conn.commit()
    conn.close()












if __name__ == "__main__":
    fileList = ('information.docx','Hello.txt','myImage.png',\
            'myMovie.mpg','World.txt','data.pdf','myPhoto.png','graffititxt.png')
    scanFiles(fileList)
    


