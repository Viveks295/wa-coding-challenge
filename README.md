# Coding Challenge for Wisconsin Autonomous Perception

### Final Answer
![answer](https://user-images.githubusercontent.com/62948441/218298166-ebd6c32f-5b60-4fc4-9cf4-f6ac2698ef4b.png)

### Methodology
I solved this by finding filtering the image by color and by objects with a higher saturation. This allowed me to filter out the cones.
Then I used contours to put the coordinates of the cone centers in a list. I then split this list into two separate lists, one containing cones 
on the left and on the right. I then used fitLine to draw a line going through the cones.

### What I tried / Why it didn't work
I first tried to use grayscale and blur to filter out the image. I realized that it wasn't working out very well and it had trouble
distinguishing the cones. I then figured out that the cones were more saturated than the rest of the image, so a HSV image would be more useful.
After that I spent some time trying to find the best HSV range so that only the cones would be detected. At first, many other objects were being picked up
like the door, the background, and the exit sign. I displayed the mask image and kept playing around with the variables until I found a good match.
I then made the mistake of storing all the cones in a single list and trying to draw the best fit line with that list, which resulted in an incorrect line. 
I was able to easily solve this by splitting the big list of cones into two lists, one containing cones on the left and the other containing cones on the right.

### Libraries
The libraries I used are OpenCV and NumPy. OpenCV was necessary to filter the image and find the cones on the image. 
I used NumPy to convert my lists into NumPy lists to find the line of best fit with OpenCV.
