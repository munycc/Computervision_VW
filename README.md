# Computervision_VW
This project represents an innovative attempt to establish a connection between Python/OpenCV and Marionette for Vectorworks, aiming to enable dynamic design adjustments within the Vectorworks environment based on real-time input data.


## Overview

This GitHub repository consists of two components: Python code and a Vectorworks (VW) script. Using OpenCV, the Python code detects hand positions, finger movements, and screen proximity. Upon opening Vectorworks, the included VW script, implemented with Marionette, processes the collected data to create a point attractor. This attractor facilitates dynamic design adjustments within the Vectorworks environment based on the captured input.



## Installation

Before proceeding with the installation, ensure you have the following prerequisites:

- Python installed on your system
- Vectorworks installed on your system
- OpenCV library installed for Python (required for recording positions)

No further installation is needed beyond these prerequisites.



## Usage

1. Decide on the folder where you'd like to store the JSON file needed for Marionette/Vectorworks.
2. Open the Python file and enter the location of the folder in the dedicated area.
3. Run the code to record your movement; it will create the JSON file directly in the chosen folder.
4. In the Marionette script, indicate the location of the file at the beginning of the script.
5. Run the Marionette script. You can adjust scales, colors, and shapes of the grid elements for various design possibilities.



