
##udm_wafik_gb est un noeud utilisant global_localization pour localiser le robot dans une carte connue en appelant les services necessaires.
#Pour uploader le fichier faire les commandes ci-dessous:

cd catkin_ws/src

git clone https://github.com/wafiik-aumeer/udm_wafiik_gb.git

cd ..

catkin_make

source devel/setup.bash

roslaunch turtlebot3_gazebo turtlebot3_world.launch

roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml

rosrun udm_wafiik_gb global_localization.py

