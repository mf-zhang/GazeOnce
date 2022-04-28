# Muti-Person Swap Gaze Dataset

## Download
To download the MPSGaze dataset, please register here https://forms.gle/1L1fdgQBPAeosJRe8. Thank you!

(We will send you a link to download as soon as the data is prepared and your request is reviewed)

## Label explanation
We expand the data label based on:

http://shuoyang1213.me/WIDERFACE/

https://github.com/biubug6/Pytorch_Retinaface

Please note that not every face has a gaze label.

**An example in training labels:**

`449 330 122 149 492.757 371.811 0.0 547.390 375.932 0.0 515.031 412.83 0.0 485.174 425.893 0.0 538.357 431.491 0.0 0.82 -0.5174 -0.6243 -0.1190 -0.0576 0.0000`

449 330 122 149: face bounding box

492.757 371.811 0.0 547.390 375.932 0.0 515.031 412.83 0.0 485.174 425.893 0.0 538.357 431.491 0.0: five landmarks

0.82: we do not use it

-0.5174 -0.6243: gaze pitch and yaw

-0.1190 -0.0576 0.0000: head pose (only for matching in the swap process)

**An example in validation set:**

`451 197 24 42 0 0 1 0 1 0 -0.2363 -1.1481 0.0906 -0.3856 0.0000`

451 197 24 42: face bounding box

0 0 1 0 1 0: we do not use

-0.2363 -1.1481 0.0906 -0.3856 0.0000: gaze and head pose

## Visualization

Please run the code in this folder to visualize the gaze of one example.
