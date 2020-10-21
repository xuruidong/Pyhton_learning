
import pandas as pd
import pymysql
from snownlp import SnowNLP


def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments

def main():
    sql  =  'SELECT *  FROM phone'
    conn = pymysql.connect('10.0.110.34','root','123456','smzdm', 3306, charset='utf8mb4')
    df = pd.read_sql(sql, conn) 
    print (df.values[0])
    df["sentiment"] = df.comment.apply(_sentiment)
    
    # s = SnowNLP(df.values[0][1])
    # print (s.sentiments)
    # print (df)
    cur = conn.cursor()
    for item in df.values:
        sql = 'insert into index_smzdmresult (title, comment, sentiment) values (%s, %s, %s)'
        data = (item[0], item[1], float(item[2]))
        try:
            cur.execute(sql, data)
        
            # cur.close()
            conn.commit()
        except Exception as e:
            conn.rollback()  
            print ("error", e)
            break
    conn.close()
    
    
if __name__ == "__main__":
    main()