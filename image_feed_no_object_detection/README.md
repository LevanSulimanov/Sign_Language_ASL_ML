# Sign_Language_ASL_ML
- dataset: https://www.kaggle.com/datamunge/sign-language-mnist
- Implementation Author: Levan Sulimanov
* Project aim is to create a classifier to detect ASL gestures and link them with alphabet letters
American Sign Language (visual picture reference):

<img src="/readme_imgs/data_gathering_samples.png"/>

* classifier_analysis.ipynb file contains various approaches towards solving this problem, but as expected CNN takes the first place. It is also interesting to take a look at SVM results and how One Versus All(Rest) strategy provides very good results.

* CNN results reach 94% of accuracy and 93% for precision. Early Stopping is used with max_delta=0.001.</br>
Refer to the confusion matrix for visual result: </br>
![CNN Confusion Matrix](/readme_imgs/classification_results.png)

*Please remember to extract "sign-language-mnist" zip-file, in order to be able to run provided models.
