# include "ros/ros.h"
# include "std_msgs/String.h"

using namespace std;
using namespace ros;

// Callback function
void chatterCallback(const std_msgs::String::ConstPtr &msg) {
    ROS_INFO("Listened: %s\n", msg->data.c_str());
}

int main(int argc, char *argv) {
    ros::init(argc, argv, "Listener");
    NodeHandler node;

    Subscriber subscriber = node.subscribe("TopicName", 1000, chatterCallback);
    ros::spin();

    return 0;
}