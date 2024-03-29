# Sign_Language_ASL_ML

<!-- GETTING STARTED -->
## About the Project

Project is focused at providing classification results for individual hand gestures that represent either letters or words

### Project Workflow

---
NEW APPROACH using KEYPOINTS RECOGNITION MODEL: https://www.youtube.com/watch?v=ZPykp8l05b8&ab_channel=LevanSulimanov
1. Data Collection:

   ---
   ![alt text](/readme_imgs/Keypoints_Data_collection.jpg)
   ---
   
---

2. Project Diagram:

   ---
   ![alt text](/readme_imgs/diagram_flow.jpg)
   ---

---
---
---
OLD APPROACH:
1. Data Gathering and Prep Work
   * Data is gathered through Web Cam video feed
   * BGR colors are getting converted into Gray Scale
   * Each image gets its label and ID name for later analysis
   * Lets us pick # of images for dataset and label
   ---
   ![alt text](/readme_imgs/data_gathering_samples.png)
   ---
   * Annotation
   ![alt text](/readme_imgs/annotation.png)
---

2. Background Reduction (for detection improvement: in accuracy and speed)
    * Using OpenCV, multiple filters used to remove the background, except selected colors
    <img src="/readme_imgs/background_reduction.gif"/>
---

3. Model Training Results:
    * ![alt text](/readme_imgs/classification_results.png)
    * ![alt text](/readme_imgs/CNN_diagram.png)
---

### Additional Thanks to:
    * Professor Fereydoon Vafaei