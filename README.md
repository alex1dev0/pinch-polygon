<div align="center"> 
   <img src="https://socialify.git.ci/alex1dev0/pinch-polygon/image?description=1&font=Inter&language=1&name=1&owner=1&pattern=Transparent&theme=Auto" alt="pinch-polygon" width="500" /> 
 </div> 
  
 <div align="center"> 
  
 <img src="https://img.shields.io/badge/license-MIT%20License-blue.svg?style=flat-square" alt="License" />
 <img src="https://img.shields.io/github/languages/top/alex1dev0/pinch-polygon?style=flat-square" alt="Language" />
 <img src="https://img.shields.io/github/repo-size/alex1dev0/pinch-polygon?style=flat-square" alt="Repo Size" />
 <img src="https://img.shields.io/github/issues/alex1dev0/pinch-polygon?style=flat-square" alt="Issues" />
 <img src="https://img.shields.io/github/stars/alex1dev0/pinch-polygon?style=flat-square" alt="Stars" />
  
 <p align="center"> 
   <em>Developed with the software and tools below.</em> 
 </p> 
 <p align="center"> 
   <a href="https://github.com/alex1dev0/pinch-polygon/graphs/contributors">
     <img src="https://img.shields.io/github/contributors/alex1dev0/pinch-polygon?style=flat-square" alt="Contributors" />
   </a>
   <a href="https://github.com/alex1dev0/pinch-polygon/network/members">
     <img src="https://img.shields.io/github/forks/alex1dev0/pinch-polygon?style=flat-square" alt="Forks" />
   </a>
   <a href="https://github.com/alex1dev0/pinch-polygon/stargazers">
     <img src="https://img.shields.io/github/stars/alex1dev0/pinch-polygon?style=flat-square" alt="Stars" />
   </a>
 </p> 
 </div> 
  
 --- 
  
 ## Table of Contents 
  
 - [Languages](#languages) 
 - [Tech Stack](#tech-stack) 
 - [Description](#description)
 - [Features](#features) 
 - [Getting Started](#getting-started) 
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Usage](#usage)
 - [Project Structure](#project-structure) 
 - [Contributing](#contributing) 
 - [License](#license) 
  
 ## Languages 
  
 ![Python](https://img.shields.io/badge/Python%20-3776AB?style=for-the-badge&logo=python&logoColor=white)   
  
 ## Tech Stack

 ![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-green.svg?style=for-the-badge&logo=opencv&logoColor=white)
 ![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10+-orange.svg?style=for-the-badge&logo=google&logoColor=white)
 ![NumPy](https://img.shields.io/badge/NumPy-1.24+-013243.svg?style=for-the-badge&logo=numpy&logoColor=white)

 ## Description

 **Pinch Polygon** is an innovative AI tool that transforms your webcam into a gesture controller. Using advanced hand tracking algorithms (MediaPipe Hands), the software identifies the position of your thumb and index finger to allow you to dynamically modify the number of sides of a polygon drawn on the screen in real-time.

 ## Features 
  
 - **🤖 AI Hand Tracking**: Precise and fast detection using MediaPipe.
 - **🎮 Intuitive Gesture Control**: 
   - **Spread** fingers to add sides.
   - **Pinch** fingers to remove sides.
 - **🎨 Real-time Rendering**: Fluid drawing of polygons from 3 to 20 sides.
 - **📊 Informative Interface**: Displays shape name, side count, and instructions.
 - **Clean and modular code structure**: Easy to customize and extend.
  
 ## Getting Started 
  
 ### Prerequisites 
  
 - Python 3.8+ 
 - A working webcam
  
 ### Installation 
  
 1. Clone the repository: 
 ```bash 
 git clone https://github.com/alex1dev0/pinch-polygon.git  
 cd pinch-polygon 
 ``` 
 
 2. Install dependencies:
 ```bash
 pip install -r requirements.txt
 ```
  
 ### Usage
  
 1. Run the application:
    ```bash
    python tool.py
    ```
 
 2. **Control the Polygon**:
    - Show your open hand to the camera.
    - **Increase sides**: Move your thumb away from your index finger ("spread" gesture).
    - **Decrease sides**: Move your thumb closer to your index finger ("pinch" gesture).
    - Press `q` to exit.

 ### Gesture Table

 | Gesture | Action | Result |
 |-------|--------|--------|
 | 🖐️ **Spread fingers** | ➕ Add side | Polygon complexity increases |
 | 🤏 **Pinch fingers** | ➖ Remove side | Polygon complexity decreases |
 | ❌ **No hand** | ⏸️ Pause | No change |
  
 ## Project Structure 
  
 ```text 
 ├── README.md          # Original documentation
 ├── requirements.txt   # Python dependencies
 └── tool.py            # Main application logic
 ``` 
  
 ## Contributing 
  
 Contributions are welcome! Please feel free to submit a Pull Request. 
  
 ## License 
  
 MIT License 

 <br>

 Created by **Alex1Dev**
