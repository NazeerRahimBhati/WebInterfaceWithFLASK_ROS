#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from flask import Flask, render_template

my_data= "hello"

def callback(data):
        global my_data
	my_data = data.data
	rospy.loginfo("RECEIVED DATA: %s", my_data)
	

def listener():       
        rospy.init_node("Subscriber_Node", anonymous=True)
        rs =rospy.Subscriber('webmsg', String, callback)
   	app = Flask(__name__) 
        @app.route("/")
        def home():
		global my_data 
                return render_template('about.html',value=my_data)
	app.run(debug=True) 
	rospy.spin()
	
	
if __name__=="__main__":		
	listener()
       


	

# @app.route('/about')
# def about():
#	return render_template('about.html')



	#Minimal_subscriber.destroy_node()
	#rospy.shutdown()

