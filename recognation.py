import  cv2
import  numpy as np
import time

class setPics():
    def __init__(self):
        self.faceDetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        self.img=None

    def start(self,cl,n,p,id):

        cam=cv2.VideoCapture(0)
        

        c=0
        ret,self.img=cam.read()
        time.sleep(4)
        while(True):
            
            ret,self.img=cam.read()
            gray=cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
            faces=self.faceDetect.detectMultiScale(gray,1.1,6)
            for (x,y,w,h) in faces:
                c=c+1
                cv2.imwrite(str(cl)+"/"+"etudiant."+str(n)+" "+str(p)+"."+str(id)+"."+str(c)+".jpg",gray[y:y+h,x:x+w])
                cv2.rectangle(self.img, (x, y), (x + w, y + h), (0, 0, 155), 2)
                cv2.waitKey(100)
            cv2.imshow("face",self.img)
            cv2.waitKey(1)
            if c>40 :
                break
        cam.release()
        cv2.destroyAllWindows()


