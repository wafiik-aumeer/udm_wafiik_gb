cd catkin_ws/src

git clone https://github.com/Goohuram/udm_gb.git

cd ..

catkin_make

source devel/setup.bash

roslaunch turtlebot3_gazebo turtlebot3_world.launch

roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml

rosrun udm_gb global_localization.py

