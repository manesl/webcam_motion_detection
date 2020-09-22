# webcam_motion_detection
Motion detection of objects using laptop camera, plotted a graph for the entry and exit of the moving object, and smoothened the images using gaussian filter.

Author:Shweta Satyasheel Mane

Files:

* motion.py: Detects motion with help of a static frame at start, turn it into gray, then applies Gaussian filter on it. When a moving object comes into the picture, the same process is iterated for that one. Both frames are compared to detect moving objects and highlight a moving object by drawing a red rectangle around it.
* graph.py: Used the bokeh library, csv file exported from motion.py to create a graph.
* a sample csv file with exported timestamps while running the application.
* a sample graph generated while running the application.
