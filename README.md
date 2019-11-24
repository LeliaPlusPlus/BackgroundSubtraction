# Background Subtraction

This program separates a background image from a foreground image using background subtraction, and then places a red bounding box around the foreground image. The image is in portable pixmap (PPM) format. The original.ppm file is an image with both background and foreground, and the background.ppm file is an image of the background. Both files have the "magic number" of P3 and are in ASCII. The program writes output to a file called foreground.ppm where the background pixels are white, the foreground pixels are their original colors, and there is a red bounding box around the foreground image. The program makes the assumption that there will be only one foreground object and no noise. 

Note: The original.png and background.png files are in this repository to show what the images look like, and are not involved with the execution of the program. The original image is a photo of Beyonc`e against Spelman College's Giles building. The background image is Spelman College's Giles building.

## Steps to Run the Program
1. Clone the repository to your desktop.
2. Download Python v3 64-bit. (Skip this step if it is already downloaded to your computer.)
3. Open main.py with IDLE.
4. Click **Run** and then click **Run module** in the dropdown.  
5. Download IrfanView.
6. Use IrfanView (or a similar software) to open the original.ppm (input), background.ppm (input), and foreground.ppm (output) files to see the results.
