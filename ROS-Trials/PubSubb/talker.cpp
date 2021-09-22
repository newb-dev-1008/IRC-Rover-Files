# include "ros/ros.h"
# include "std_msgs/String.h"
# include <sstream>

using namespace std;
using namespace ros;

int main(int argc, char **argv) {
    init(argc, argv, "Talker");

    NodeHandler n;
    Publisher publisher = n.advertise<std_msgs::String>("Chatter", 1000);
    Rate loop_rate(1.0);

    int count = 0;
    while (ok()) {
        std_msgs::String msg;
        std::stringstream ss;

        ss << "Hello World" << count;
        msg.data = ss.str();

        ROS_INFO("Published: %s\n", msg.data.c_str());
    }
})