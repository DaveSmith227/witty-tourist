# About 🤳🌉

[wittytourist.com](https://wittytourist.com)


WittyTourist is a web application that gives you a witty caption when you upload a photo with a San Francisco landmark.  Using computer vision, the app identifies the landmark in your photo and returns a witty caption for that landmark.

# Usage - Snap Pic 📷 Get Wit 😉
You’ve taken the perfect photo and you’re ready post to social media, but now comes the hard part…coming up with a witty caption!

- Step 1 - Snap Pic
- Step 2 - Get Witty Caption
- Step 3 - Post to social media and watch your likes roll in like Karl on a foggy day in San Francisco.

[Try it out!](https://wittytourist.com)

![Snap Pic, Get Wit #wittytourist](https://github.com/DaveSmith227/witty-tourist/blob/master/screenshots/mockup-painted-ladies-small.jpg)

![Screenshots #wittytourist](https://github.com/DaveSmith227/witty-tourist/blob/master/screenshots/mockup-alcatraz-golden-gate-small.jpg)


# List of Landmarks 🌁
The app is currently trained to detect these San Francisco landmarks (more coming!):

1. The Golden Gate Bridge
2. The Oakland Bay Bridge
3. A cable car
4. Lombard Street
5. Alcatraz
6. The Painted Ladies at Alamo Square
7. The Palace of Fine Arts
8. The sea lions at Pier 39
9. The Transamerica Pyramid
10. Muir Woods
11. Ghirardelli Square
12. Coit Tower
13. Fisherman's Wharf sign

# Computer Vision - How it Works 🧐

__Blog Post: [9 Steps to Building a Deep Convolutional Neural Net in Excel for Normal Humans.](https://towardsdatascience.com/cutting-edge-face-recognition-is-complicated-these-spreadsheets-make-it-easier-e7864dbf0e1a)__

Cutting-Edge Face Recognition is Complicated. These Spreadsheets Make it Easier.

![Excel CNN](https://cdn-images-1.medium.com/max/1800/1*m65nIVO62a4Dua2QzmPI2A.png)

![CNN architecture](https://cdn-images-1.medium.com/max/2000/1*JrxHmdQH4HFNj4aBtuuEpQ.png)

# WittyTourist Model - How it was Trained 🏋️

The backbone architecture of this convolutional neural net (CNN) is ResNet-50.  The model was initially trained on ImageNet and using transfer learning, the weights were re-trained and fine-tuned to fit the landmark classes in this app.  This is a multi-class image classification algorithm.

To learn how to build your own app, check out these resources:

- [Video lesson from fast.ai](https://course.fast.ai/videos/?lesson=1) - How to build an image classification model
- [Model deployment](https://course.fast.ai/deployment_render.html) - Instructions on how to deploy an app on Render