#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import demo_pkg.sonar_io as SIO
import demo_pkg.sonar_lights_io as SLIO


def main():
    rospy.init_node('sonar_demo', anonymous=True)
    s = SIO.SonarIO()
    l = SLIO.SonarLightsIO()
    for i in range(0, 12):
        s.set_sonars(2**i)
        print("State :", len(s.state()), "Enabled: ", bin(s.get_sonars()))
        rospy.sleep(1)
    
    print("Lights Show!!!")
    rate = rospy.Rate(100)
    targetExit = rospy.Time.now() + rospy.Duration(5)
    while rospy.Time.now() < targetExit:
        l.set_lights(int('0b101010101010',2))
        rate.sleep()
        

if __name__ == '__main__':
    main()
