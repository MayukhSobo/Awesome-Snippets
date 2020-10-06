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

</table>
