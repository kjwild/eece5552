<div align="center">
<h3 align="center">EECE5555 Group Project</h3>
EECE5552 Assistive Robotics
</div>

<!-- ABOUT THE PROJECT -->
## About the Project

This is the GitHub repository for the Fall 2022 EECE5552 group project.

<!-- GETTING STARTED -->
## Getting Started

Here are instructions for setting up a local instance of this project.

### Software

- Ubuntu 20.04
- ROS1
- Python 3.8

### Installation

This repository is public and does not require a key to clone.

1. Clone the repo
    * HTTPS
    ```sh
    git clone https://github.com/kjwild/eece5552.git
    ```
    * SSH
    ```sh
    git clone git@github.com:kjwild/eece5552.git
    ```
2. Open bash terminal.
3. Navigate to local directory containing `src` folder.
4. Run `catkin_make`.
5. Source the set-up file, e.g.
   ```sh
   source devel/setup.bash
   ```

Remember to source the set-up file for each new instance.

<!-- USAGE -->
## Usage

Here are instructions for running important packages in this project.

### burger_example

The burger_example package is an attempt at running and understand Gazebo.  It uses Turtlebot3.

#### burger_example Required Packages

To run with Turtlebot3 Burger, the primary model for this package, the following additional packages are needed:

- turtlebot3
- turtlebot3_msgs
- turtlebot3_simulations
- slam_gmapping
- openslam_gmapping

The SLAM packages assist with a mapping demonstration of a sample world.

### camera_reader

TBD

<!-- ROADMAP -->
## Roadmap
- [X] Mid-term proposal
- [ ] Camera hardware integration
- [ ] Robot locomotion
- [ ] Point cloud sampling
- [ ] Mapping
- [ ] Final presentation

<!-- CONTACT -->
## Contact

Kevin J. Wu - wu.kevi@northeastern.edu - wu.j.kevin@protonmail.ch
TBD: Others

Project Link: [https://github.com/kjwild/eece5552](https://github.com/kjwild/eece5552)
