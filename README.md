# Awesome-Snippets :heartbeat:
Some awesome snippets for the data science community

> Snippets with :fire: are used by me a lot

<table style="width:70%">
  <tr>
    <th>Usage</th>  
    <th>File</th>
    <th>Cautions</th> 
  </tr>
  
  <tr>
    <td>If you got bored with the boring confusion matrix in sklearn and want something really cool and beautiful for your model performance. :fire: </td>
  <td> <a href="https://raw.githubusercontent.com/MayukhSobo/Awesome-Snippets/main/confusionMatrix.py">confusionMatrix.py</a></td>
    <td>Please don't use it for more than 15 class labels and keep the name of the class labels shorter so that it can be visuialised easily</td>
  </tr>
  

  <tr>
  <td>Ever wanted a snippet that can perform different types of sent2vec using word2vec! Well, your wait is over here! </td>
  
  <td> <a href="https://raw.githubusercontent.com/MayukhSobo/Awesome-Snippets/main/sent2vec.py">sent2vec.py</a></td>
  
  <td>Please note that only average word2vec and tfidf weighted word2vec is supported. Also, you need to download the pertrainined word2vec model. Use the following link <a href="https://s3.amazonaws.com/dl4j-distribution/GoogleNews-vectors-negative300.bin.gz"> word2vec Model</a>. You can download this using wget command from terminal</td>
  </tr>

  <tr>
  <td> Once you train a tensorflow2 or keras model, if you want to see the loss vs epoch or accuracy vs epoch for both validation and training data, you can use this snippet.</td>
  
  <td> <a href="https://raw.githubusercontent.com/MayukhSobo/Awesome-Snippets/main/display_performance.py">display_performance.py</a></td>
  
  <td>Keep in mind that this only works for classification problems where you have separate training and validation data. Moreover accuracy is a metric that you are actively tracking. May not work for some special kind of metric however can always be modified as the code is written in simple python.</td>
  </tr>

  <tr>
  <td> This uses SOTA transformer models to get the text features. This is ideal for a lot of zero shot learning where we want to get BERT/GPT features of the text data. :fire: :fire: </td>
  
  <td> <a href="https://raw.githubusercontent.com/MayukhSobo/Awesome-Snippets/main/transformerFeatures.py">transformerFeatures.py</a></td>
  
  <td> This is still half baked and may not support all the libraries and their versions.</td>
  </tr>

  <tr>
  <td> This shows how one can use tesnsorflow dataset API for Image Classification taks</td>
  
  <td> <a href="https://github.com/MayukhSobo/Awesome-Snippets/blob/main/tfdataImage.ipynb"> tfdataImage.ipynb </a></td>
  
  <td>It would only work with tensorflow 2.3 or above </td>
  </tr>
  
  <tr>
  <td>  Well this is not much realted to data science but this code generates the test cases if you are interested in Competitive Programming. </td>
  
  <td> <a href="https://raw.githubusercontent.com/MayukhSobo/Awesome-Snippets/main/gene.py"> gene.py </a></td>
  
  <td>It may not work for all the types. Please raise a PR </td>
  </tr>

</table>
