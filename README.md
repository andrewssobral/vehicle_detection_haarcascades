# Vehicle Detection with Haar Cascades

Last page update: **28/02/2016**

Last version: **1.0.0** (see Release Notes for more info)

Hello everyone,
An easy way to perform vehicle detection is by using Haar Cascades. Currently, I don't have a detailed tutorial about it, but you can get some extra information in the OpenCV homepage, see [Cascade Classifier](http://docs.opencv.org/2.4/doc/tutorials/objdetect/cascade_classifier/cascade_classifier.html) page. See also [Cascade Classifier Training](http://docs.opencv.org/2.4/doc/user_guide/ug_traincascade.html) for training your own cascade classifier.

<p align="center">
<a href="https://www.youtube.com/watch?v=c4LobbqeKZc" target="_blank">
<img src="https://sites.google.com/site/andrewssobral/vehicle_detection_haarcascades.png" border="0" />
</a>
</p>

The haar-cascade **cars.xml** was trained using 526 images of cars from the rear (360 x 240 pixels, no scale).
The images were extracted from the Car dataset proposed by Brad Philip and Paul Updike taken of the freeways of southern California.
 
For more information, please see:
 
* Train Your Own OpenCV Haar Classifier 
 * http://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html
 * https://github.com/mrnugget/opencv-haar-classifier-training
 
* Related paper:
 * Oliveira, M.; Santos, V. Automatic Detection of Cars in Real Roads using Haar-like Features ([PDF](https://sites.google.com/site/andrewssobral/Automatic_Detection_of_Cars_in_Real_Roads_using_Haar-like_Features.pdf))
 
* Some additional resources:
 * http://lars.mec.ua.pt/public/Media/ResearchDevelopmentProjects/HaarFeatures_RoadFilms/HaarFeaturesTests/CarsRear/
 * http://lars.mec.ua.pt/public/Media/ResearchDevelopmentProjects/HaarFeatures_RoadFilms/HaarFeaturesTests/

Additional informations:
* Check if your OpenCV is installed at: C:\OpenCV2.4.10
* There is a Visual Studio 2013 template project in the **vs2013/** folder. Open it in the Visual Studio IDE and select [Release]-[Win32] or [Release]-[x64] mode. Next, click on **run_vehicle_detection.bat** and enjoy!

Release Notes:
* Version 1.0.0:
First version.
