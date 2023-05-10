#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
turn = 0
timer = 0
def callback(dt):
    global turn, timer
    print ('-------------------------------------------')
    print ('Range data at front:   {}'.format(dt.ranges[0]))
    print ('Range data at left:   {}'.format(dt.ranges[90]))
    print ('Range data at right:  {}'.format(dt.ranges[270]))
    print ('Range data at back:  {}'.format(dt.ranges[180]))
    print (turn)
    print (timer)
    print ('-------------------------------------------')
    pub.publish(move)
    if turn==0:
        move.linear.x=-0.1
        move.angular.z=0.0
        if (dt.ranges[180] <  1.5):
            turn=turn+1
    elif turn==1:
        move.linear.x= 0.0
        move.angular.z= -0.5
        if (dt.ranges[0] > 1.5 and dt.ranges[270] > 1.4 and dt.ranges[180] < 0.5 and dt.ranges[90]>1.4 and dt.ranges[0] < 1.55):
            turn=turn+1 
    elif turn==2:
        move.linear.x= 0.1
        move.angular.z= 0.0
        if (dt.ranges[0] < 0.5):
            turn=turn+1
    elif turn==3:
        move.linear.x=      0.0
        move.angular.z=     -0.5
        if (dt.ranges[0] > 1.4 and dt.ranges[0] < 1.7 and dt.ranges[90] < 0.5):
            turn=turn+1
    elif turn==4:
        move.linear.x=      0.1
        move.angular.z=     0.0
        if (dt.ranges[0] < 0.5):
            turn=turn+1
    elif turn==5:
        move.linear.x=      0.0
        move.angular.z=     0.5
        if (dt.ranges[0] > 1.2 and dt.ranges[0] < 1.55 and dt.ranges[270] < 0.5 ):
            turn=turn+1
    elif turn==6:
        move.linear.x=      0.1
        move.angular.z=     0.0
        if (dt.ranges[0] < 0.5):
            turn=turn+1
    elif turn==7:
        move.linear.x=      0.0
        move.angular.z=     0.5
        timer = timer+1
        # if (dt.ranges[180] < 0.5 and dt.ranges[270] < 0.5 and dt.ranges[90] < 1.8 and dt.ranges[0] == False):
        if (timer>16):
            turn=turn+1
    elif turn==8:
        move.linear.x =     0.1
        move.angular.z =    0.0
        timer = timer+1
        if (dt.ranges[0] < 0.5):
            
            move.linear.x =     0.0
            move.angular.z =    0.5
            
move = Twist()
rospy.init_node('obstacle_avoidance_node')
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
sub = rospy.Subscriber("/scan", LaserScan, callback)

rospy.spin()