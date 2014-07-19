QDA
===
Implementation of Quadratic Discriminant Analysis (QDA) method for binary and multi-class classifications.
The only difference between QDA and [LDA](https://github.com/saifuddin778/LDA/) is that in QDA, we compute the pooled covariance matrix for each class and then use the following type of discriminant function for getting the scores for each of the classes involed:
<img align="center" src="https://github.com/saifuddin778/QDA/raw/master/images/QDA.png" alt="...">

![alt text](https://github.com/saifuddin778/QDA/raw/master/images/QDA.png "")

###Conventional LDA (for 2 classes):
```python
>>> from LDA import LDA
>>> t = LDA([[2.4, 5.4, 3.3], [5, 6.6, 3.4], [2.1, 2.4, 2.5], [5, 3.1, 6]], ['A', 'A', 'B', 'B'])
>>> t.predict([2.3, 3.2, 2.4])
>>> {'A': 2.1366024891345905, 'B': 3.2231442139356759}
```

