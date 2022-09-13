from __future__ import division
import key_press as kp
import numpy as np
import cv2 
import math
font = cv2.FONT_HERSHEY_SIMPLEX
def length_centrte(centre,end):
    aa= (end[0]-centre[0])
    bb= (end[1]-centre[1]) 
    cc= (aa*aa)+(bb*bb)
    return math.sqrt(cc)
def extreme_distance(mid_centre,ext_points):
    a=length_centrte(mid_centre,ext_points[0])
    b=length_centrte(mid_centre,ext_points[1])
    c=length_centrte(mid_centre,ext_points[2])
    d=length_centrte(mid_centre,ext_points[3])
    return [round(a, 8),round(b, 8),round(c, 8),round(d, 8)]
def count(thresholded, segmented):
    chull = cv2.convexHull(segmented)
    extreme_top    = tuple(chull[chull[:, :, 1].argmin()][0])
    extreme_bottom = tuple(chull[chull[:, :, 1].argmax()][0])
    extreme_left   = tuple(chull[chull[:, :, 0].argmin()][0])
    extreme_right  = tuple(chull[chull[:, :, 0].argmax()][0])
    cX = (extreme_left[0] + extreme_right[0]) / 2
    cY = (extreme_top[1] + extreme_bottom[1]) / 2
    extreme_points=[extreme_left, extreme_right, extreme_top, extreme_bottom]    
    distance = extreme_distance((cX, cY),extreme_points)
    maximum_distance = max(distance)
    radius = int(0.8 * maximum_distance)                
    circumference = (2 * np.pi * radius)
    circular_roi = np.zeros(thresholded.shape[:2], dtype="uint8")
    cv2.circle(circular_roi, (int(cX), int(cY)), radius, 255, 1)
    circular_roi = cv2.bitwise_and(thresholded, thresholded, mask=circular_roi)
    (_, cnts, _) = cv2.findContours(circular_roi.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    count = 0
    for c in cnts:
        (x, y, w, h) = cv2.boundingRect(c)
        if ((cY + (cY * 0.25)) > (y + h)) and ((circumference * 0.25) > c.shape[0]):
            count += 1
    return count
def reset_all():
    kp.ReleaseKey(0xC8)
    kp.ReleaseKey(0xCB)
    kp.ReleaseKey(0x38)
    kp.ReleaseKey(0xCD)
    kp.ReleaseKey(0xD0)    
def midpoint(start,end):
    mid = (start+end)/2
    return int(mid)
def angle(p1,p2,angle):
    x=p2[0]-p1[0]
    y=p2[1]-p1[1]
    if((x<0)and(0<y)):
         an =  angle*(-1)
         return an
    elif((0<x)and(0<y)): 
         an =  180-angle
         return an
    elif((0<x)and(y<0)): 
         an = ((angle)*(-1))+180
         return an
    elif((x<0)and(y<0)): 
         an = 360-angle
         return an
    else:
         return angle                     
def slope_angle(p1,p2):
    try:
       m=(p2[1]-p1[1])/(p2[0]-p1[0])  
       ang = angle(p1,p2,math.degrees(math.atan(m)))   
       return ang
    except ZeroDivisionError:
       m=0 
       return math.degrees(math.atan(m))         
def front_back(p1,p2,angle):  
    if(0<angle<180):
        print("front")
        kp.ReleaseKey(0xD0) 
        kp.PressKey(0xC8)        
    elif(180<angle<360):
        print("back")
        kp.ReleaseKey(0xC8) 
        kp.PressKey(0xD0) 
def left_right(p1,p2,angle):  
    if(90<angle<270):
        print("right")
        kp.PressKey(0xCD)        
    elif((270<angle<360)or(0<angle<90)):
        print("left")
        kp.PressKey(0xCB) 
def car_race(finger_val,js,pt1,pt2,m):
                        if((finger_val==1)and(js==1)):                                                                           
                            left_right(pt1,pt2,m)                        
                        elif((finger_val==1)and(js==2)):                                                  
                            front_back(pt1,pt2,m)       
                        else:                            
                            reset_all()           
def joystick(frame,x_start,x_end,y_start,y_end,js):
            fram=frame[y_start:y_end,x_start:x_end]
            gr=cv2.cvtColor(fram,cv2.COLOR_BGR2GRAY)
            cv2.rectangle(frame,(x_start,y_start),(x_end,y_end),(0,255,0),3)
            hsv=cv2.cvtColor(fram,cv2.COLOR_BGR2HSV)
            hsv=cv2.medianBlur(hsv,11)
            low=np.array([0,48,80])
            high=np.array([25,255,255])
            mask=cv2.inRange(hsv,low,high)
            blur=cv2.medianBlur(mask,5)
            y_centre = midpoint(y_start,y_end)
            x_centre = 125
            cv2.circle(fram,(x_centre,y_centre),3,(0,255,0),-1)                          
            _,cts,hie=cv2.findContours(blur,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)             
            if len(cts)!=0:                                
                areas=[cv2.contourArea(i) for i in cts]     
                maxcnt=cts[np.argmax(areas)]
                hull=cv2.convexHull(maxcnt,returnPoints=False)    
                defecti=cv2.convexityDefects(maxcnt,hull)                
                M=cv2.moments(maxcnt)                
                if ((max(areas)>4500)):                                                                                         
                        finger_val = count(blur,max(cts, key=cv2.contourArea))                        
                        cx=int(M['m10']/M['m00'])
                        cy=int(M['m01']/M['m00'])
                        m=slope_angle((cx,cy),(x_centre,y_centre))                    
                        cv2.circle(fram,(cx,cy),3,(0,0,255),-1)   
                        car_race(finger_val,js,(cx,cy),(x_centre,y_centre),m)
            return  fram,blur
def video_start():
    cap=cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,512)      
    while True:        
        retval,frame=cap.read()          
        if retval:           
            joystick(frame,0,250,50,350,1)
            joystick(frame,int(cap.get(3)-250),int(cap.get(3)),50,350,2)   
            dd = cv2.flip(frame, 1)
            cv2.putText(dd,'press u to exit window',(10,400), font, 1,(0,0,255),2,cv2.LINE_AA)
            cv2.imshow('Car Race',dd)
            if cv2.waitKey(2) & 0xFF==ord('u'):
                break            
    cap.release()
    cv2.destroyAllWindows()    