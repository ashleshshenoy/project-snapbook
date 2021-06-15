import cv2
import os
def click():
  videoCaptureObject = cv2.VideoCapture(0)
  result = True
  while(result):
      ret,frame = videoCaptureObject.read()
      cv2.imshow('frame',frame)
      if cv2.waitKey(1)==ord('p'):
        result = False

  videoCaptureObject.release()
  cv2.destroyAllWindows()
  return frame
















































'''
  img=cv2.line(frame,(0,0),(width,height),(255,255,255),10)
    img=cv2.line(img,(0,height),(width,0),(255,255,255),10)
    img=cv2.rectangle(img,(0,0),(width,height),(255,255,255),10)
    img=cv2.circle(img,(width//2,height//2),60,(0,0,255),-1)
    font=cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.putText(img,'Ashlesh shenoy',(width//2-100,height//2-100),font,1,(0,0,0),3,cv2.LINE_AA)
  '''