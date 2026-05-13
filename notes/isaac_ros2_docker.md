**Isaac Sim Documentation, Nvidia**

- Isaac Sim can be installed on a workstation or through a Docker container. 
  - Workstation is suitable for tutorials, DIY dev projects, testing, etc.. System constraints can really slow down Isaac Sim on a workstation.
    - You do not necessarily have to meet the minimum requirements to install and run isaac sim?
    - https://docs.isaacsim.omniverse.nvidia.com/5.1.0/installation/install_workstation.html

  - Container installation is suitable for running isaac sim on a remote server. Would be used if developing an application? Can be useful for running different distributions of ros2 that may not be compatable with certain OS. 
    - https://docs.isaacsim.omniverse.nvidia.com/5.1.0/installation/install_container.html
- Isaac Sim and ros handle the data transfer from Isaac and ros running on different versions of Python3?
  - Isaac sim uses Python 3.11
  - Ubuntu 22.04, ros2 humble uses Python 3.10



**Isaac Sim in under half an hour, Articulated Robotics, https://www.youtube.com/watch?v=SjVqOqEXXrY**
- Isaac sim is a robotics simulator. It can create very realistic camera data. 
  - popular ways of Isaacsim is integrated into a developement workflow:
    1. interaction with ros
    2. reinforcement learning with isaaclab

-  