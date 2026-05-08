- Terminator is a graphical user interface (gui) that allows you to split terminal windows easily.  

 

**ROS2 Humble Crash Course, Robotics Back-End** 

- ROS2 node: a program that interacts with ROS2 tools and communications 

- Rqt_graph visualizes the relationship between different nodes in a diagrammatic matter 

 

- ros2_ws 
    - ROS2 workspace (just a folder) 

    - Src (source) within the workspace  

 

- Install future ros2 packages with: "sudo apt install ros-humble-____" 

- Ros2 topic: something that is sent form one node to another 

- Every time you use a new package in Python, put a dependency into ```packages.xml``` 

*Nodes* 

- rclpy is the package that allows communication between ros2 and python 

  - rclpy.init(args=args) starts a node 

  - rclpy.spin(node) keeps a node running until Ctrl+C kills it 
  - ```ros2 run <build directory> <name of executable node>``` *Name of the node is defined in setup.py 

- "colcon build --symlink-install" in parent workspace folder  

  - Allows you to save changes to the node program and have them run instantly without having to rebuild in the parent workspace directory.  

- "chmod +x <file_name>" makes a file executable 

  - Must be done to any node or topic file to make it interact with ros2 


*Topics* 

- Topic is a way to communicate between nodes 

- Nodes do not directly communicate to each other; they either publish or subscribe to topics. Multiple nodes can publish or subscribe to a single topic. 

- A topic has a name, which is effectively its address (ie. Where the nodes know to publish to or subscribe from) 

- Topics are anonymous. A subscriber will not know what node is publishing to the topic it is subscribed to.  

*Publisher*

- "self.cmd = self.create_publisher(<pusblish_variable>, <topi>, <q_rate>) in __init__(self):"

  - Q size (Q essentailly meaning Queue here) denotes how many times the command is published to ensure that a subscriber actually receives the command from the topic. 

- The topic to publish to can be found from: 

  - ros2 topic list 

  - ros2 topic info /<topic> 

- "self.cmd.publish(msg) publishes msg" 

  - "msg" must be the variable type that the publisher is defined to publish 

- "self.create_timer(<time>, <callback>)" makes a timer that calls a callback function on a defined interval. For a publisher that is continuously publishing, that callback function should contain a "self.cmd.publish(msd)"


*Subscriber*

- ros2 topic echo /<topic_name> 

  - Makes a subscriber to the desired topic 

- self.<subscriber method name> = self.create_subscriber() creates a subscriber
  - a subscriber needs the to know the data type coming in, the exact name of the topic, and the have a callback function of what to do with the data coming from topic
    - "ros2 topic list" gives a list of the active topics that could be subscribed to. 

*Closed loop control (subscriber and publisher)*
- In draw_circle node, the publisher is using a timer to publish to the cmd topic. Creating a publisher does not require a callback. In the callback of a timer or subscriber, the publisher can be used to publish to a given topic. When the callback of a subscriber publishes to a topic based on the value of the topic the node is subscribing to, this is feedback control.
- 
 

**Linux Command Line Tutorial for Robotics, Control, and Machine Learning - Part 1, Aleksandar Haber PhD**

- Pwd: print working directory 

- Cd: change directory 

- Ls-l: list contents of working directory  

- Ls –la: list contents of working directory including hidden files 

- Hidden files start with a period “.” 

  - Hidden files often contain settings or config scripts by convention 

  - .env files are common so they do not get pushed to git 

  - Notes ~/.notes are often used to prevent clutter  

- ./”file_name” runs an executable file  

 

**The Linux command line for beginners, Canonical Ubuntu** 

- The “-p” that we used is called an option or a switch (in this case it means “create the parent directories, too”). Options are used to modify the way in which a command operates, allowing a single command to behave in a variety of different ways. Unfortunately, due to quirks of history and human nature, options can take different forms in different commands. You’ll often see them as single characters preceded by a hyphen (as in this case), or as longer words preceded by two hyphens. The single character form allows for multiple options to be combined, though not all commands will accept that. And to confuse matters further, some commands don’t clearly identify their options at all, whether or not something is an option is dictated purely by the order of the arguments! You don’t need to worry about all the possibilities, just know that options exist and they can take several different forms. 

- “>” redirects the output of the terminal to a file 

  - Redirection clears the file name. BE CAFEFUL 

  - If you do want to append to, rather than replace, the content of the files, double up on the greater-than character before writing into it. “>>” 

 

- “cat” prints at the content of a file 

  - “cat” can take multiple arguments and prints all arguments concatenated together 

  - A question mark (“?”) can be used to indicate “any single character” within the file name. An asterisk (“*”) can be used to indicate “zero or more characters”. These are sometimes referred to as “wildcard” characters. 

 
- “echo” prints the argument it is given back 

- two dots (..) represents the parent directory, so a single dot (.) can be used to represent the current working directory. 

- “mv” to move files 

  - If you pass more than two arguments, the last one is taken to be the destination directory and the others are considered to be files (or directories) to move. 

  - Can be used to rename files aswell 

- “cp” copies files similarly to mv (two arguments) 

- “rm” removes files 

- “rmdir” removes directories 

- “|” is used to pipe the output of a command to the input of the next 

  - Ex. “ls ~ | wc –l" 

- Most command line tools come with a brief (and sometimes not-so-brief) instruction manual, accessed through the “man” (manual) command. 

- “sort” sorts a file alphabetically and prints the contents 


**Object-Oriented Programming (OOP) in Python,
https://realpython.com/python3-object-oriented-programming/**
- super().<method> searchs the parent class for a method and calls is.
  - A class can be built from a parent class so the objects have all the same attributes as the parent. This allows for significantly reducing the amount of code duplication. 



 

 

 