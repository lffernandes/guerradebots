import requests 
import json
import threading 
import time

def Worker(self, a):
      url = 'http://34.219.164.43:3500/'
      meunome = 'Rickdiculo'
      params = {'text':meunome}
      while True: 
            rq1= requests.post(url, params) 
            print(meunome, rq1.elapsed.total_seconds()) 
            
            
          
      
if __name__ == "__main__":
  
      t1 =  threading.Thread(target=Worker, args='t1')
      t1.start()
      t2 =  threading.Thread(target=Worker, args='t2')
      t2.start()
      t3 =  threading.Thread(target=Worker, args='t3')
      t3.start()
      t4 =  threading.Thread(target=Worker, args='t4')
      t4.start()
      t5 =  threading.Thread(target=Worker, args='t5')
      t5.start()
      t6 =  threading.Thread(target=Worker, args='t6')
      t6.start()
      t7 =  threading.Thread(target=Worker, args='t7')
      t7.start()
      t8 =  threading.Thread(target=Worker, args='t8')
      t8.start()
      t9 =  threading.Thread(target=Worker, args='t9')
      t9.start()
      ta =  threading.Thread(target=Worker, args='ta')
      ta.start()
      tb =  threading.Thread(target=Worker, args='tb')
      tb.start()
      tc =  threading.Thread(target=Worker, args='tc')
      tc.start()
      td =  threading.Thread(target=Worker, args='td')
      td.start()
      te =  threading.Thread(target=Worker, args='te')
      te.start()
      tf =  threading.Thread(target=Worker, args='tf')
      tf.start()
      tg =  threading.Thread(target=Worker, args='tg')
      tg.start()
      th =  threading.Thread(target=Worker, args='th')
      th.start()