# Computervision_VW
This short project represents an innovative attempt to establish a connection between Python/OpenCV and Marionette for Vectorworks, aiming to enable dynamic design adjustments within the Vectorworks environment based on user input data.


## Overview

This GitHub repository consists of two folders, each containing Python files utilizing OpenCV to capture and interpret movement data. 
The first folder focuses on detecting hands and faces, while the second folder specializes in recognizing finger movements. 
Additionally, both folders include a Vectorworks (VW) script. When opened in Vectorworks, the included VW script, implemented with Marionette, processes the collected data to create a point attractor. 
This attractor enables dynamic design adjustments within the Vectorworks environment based on the interpreted movement data.


## Installation

Before proceeding with the installation, ensure you have the following prerequisites:

- Python installed on your system
- Vectorworks installed on your system
- OpenCV library installed for Python (required for recording positions)
- Madiapipe library installed for Python (required for face / hand detection)

No further installation is needed beyond these prerequisites.



## Usage


1. **Download the GitHub repository** and choose a folder: Hand+Face detection or Finger detection.

2. **Open the Python file** within the selected folder.

3. **Run the code** to record your movement. Press the "e" key when you're done. This action will generate JSON file(s) in the same folder as the Python file.

4. **Open the Vectorworks file** containing the Marionette script.

5. **Specify the location of the JSON file** in the following Marionette nodes:

   - For Hand+Face detection:
     - Modify the JSON file path in Marionette nodes: "Rectangle for JSON", "Point 2D_head", "Point 2D_hand", "Coeff_head", "Coeff_hand".

   - For Finger detection:
     - Modify the JSON file path in Marionette nodes: "Rectangle for JSON", "List_pt".

6. **Run the Marionette script**. You can customize scales, colors, and shapes of the grid elements to explore different design possibilities.



