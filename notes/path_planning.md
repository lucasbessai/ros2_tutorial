**Trajectory Planning 1/2, MECH572, Inna Sharf, McGill University, 20***
-
- Path Planning vs Trajectory Planning
  - A path is a purely geometric object. No relation to time.
    - Often defined parametrically?
  - A trajectory is defines motion along a path as a function of time.
    - (x(t), y(t), z(t)) defines the position of the end effector as a function of time.
    - a trajectory planner with generate **p(t)**, **v(t)**, and **a(t)** for the end effector to move from the initial state to the final state.
- With a point to point trajectory, we want to define $q(t)$, $\dot{q}(t)$, and $\ddot{q}(t)$
  - given the initial position and constraints on the velocity and acceleration, coefficients of a polynomial trajectory can be derived.
  - contraints may be: $\dot{q_i}(t)=0$, and $\dot{q_f}(t)=0$ and similar for acceleration constraints. 
- Trapezoidal velocity profiles are often desirable since joints are often characterized by limits on their velocities and accelerations (torques). The trapezoidal path can guarantee operation within these limits. 
  - providing these limiting values and solving some constraining equations will output the position, velocity, and acceleration profile for a given joint. 

**Robotics: Modelling, Planning and Control**
-

- The actual name robot arose from its use by the playwright Karel Capek in the play ˇ Rossum’s Universal Robots (1920). 

- Inverse Kinematics 

  - Given an end effector position, solve for the joint angles that realise this position. 

    - The solution is often not unique: for a two link planar arm the same position can be reached with elbow-up or elbow-down. In this case the inverse kinematics result outputs a set of possible solution.  

    - For path planning, you need to decide which branch of paths to take. You do not want to start going down a branch that leads to a singularity before reaching the desired final state.  

*Singular points*  

- Singularities represent configurations at which mobility of the structure is reduced, i.e., it is not possible to impose an arbitrary motion to the end-effector.  

- When the structure is at a singularity, infinite solutions to the inverse kinematics problem may exist.  

- In the neighbourhood of a singularity, small velocities in the operational space may cause large velocities in the joint space. 

- a continuous path in task space does not always mean a nice continuous path in joint space. 

  - For path planning with obstacle avoidance: find a path that is collision free, and avoids singular points. 

*Tragectory Planning*
- In principle, it can be conceived that the inputs to a trajectory planning algorithm are the path description, the path constraints, and the constraints imposed by manipulator dynamics, whereas the outputs are the end-effector trajectories in terms of a time sequence of the values attained by position, velocity and acceleration. 

- the trajectory planning algorithm generates a time sequence of variables that describe end-effector position and orientation over time in respect of the imposed constraints. Since the control action on the manipulator is carried out in the joint space, a suitable inverse kinematics algorithm is to be used to reconstruct the time sequence of joint variables corresponding to the above sequence in the operational space. 

*Motion through a sequence of points* 

- It should not be forgotten that the corresponding joint variables have to be computed from the operational space poses. A dense path requires significant computations 

- Creating a degree N-1 order polynomial to describe q(t) for a path through N path points is undesirable for several reasons.  

- instead use a series of cubic polynomials to  

 

*Why are the path planning problem and the trajectory planning problem separated in the literature?*

- Simple solution: discretized path  à feed to PID controller at a fixed rate à End effector moves along waypoints to desired final state. 

  - There is a difference between waypoint-following with feedback control (setpoint regulation) and trajectory planning.  

    - Low level control strategy 

    - With a series of setpints, the controller does not know the desired velocity, or acceleration and the constraints on these parameters. 

  - A trajectory is implicitly created through this method but you do not get control over speed, dynamic feasibility, coordination of joints, etc.  

- The separation (of path planning and trajectory planning) is useful because many planners first solve a geometric problem: “Find any collision-free route from start to goal.” Then they solve a timing/dynamics problem: “Move along that route smoothly and safely within actuator limits.” 

- Just using the position error could lead to breaking the robot with unintended jerks, large velocities, etc. Instead: 
  1. if you want to move between two points you make a trajectory that smooths the velocity, acceleration, maybe jerk that isn’t too computationally heavy.  

  2. Today this is often done with packages like “moveit.py”. These mechanics problems were largely solved in the 90s.  

  3. If you want to move between two states and in the process avoid hitting things along the way, you need to define other path points between initial and final state then generate a trajectory that goes through all the path points that also smooths velocity, acceleration, jerk.  

  4. The trajectory is a sequence of positions, velocities and accelerations. These ae converted to joint space thereafter for control of the robot.  

  5. From the joint space realization of the trajectory (ie. q, q_dot, q_ddot of each joint) you then use closed loop feedback control at each joint (with an encoder) to realize the trajectory. The closed loop feedback at each joint ensures that you actually realize the prescribed trajectory. 

  6. A more complex control method would involve MIMO control of all the joint states together. This will result in better tracking since each joint’s is coupled with the error of the other joints. A MIMO control matrix effectively communicates error at the joint level to all the joints resulting in a more holistic realization of the goal. (Depending on the use case of the robot, this may not be required.)