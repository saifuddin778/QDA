QDA
===

Iplementation of Quadratic Discriminant Analysis (QDA) method for binary and multi-class classifications.

###Conventional LDA (for 2 classes):
```python
>>> from LDA import LDA
>>> t = LDA([[2.4, 5.4, 3.3], [5, 6.6, 3.4], [2.1, 2.4, 2.5], [5, 3.1, 6]], ['A', 'A', 'B', 'B'])
>>> t.predict([2.3, 3.2, 2.4])
>>> {'A': 2.1366024891345905, 'B': 3.2231442139356759}
```
Each of the binary classes above ('A' and 'B') are predicted based on the standard discriminant function i.e. ![alt text](https://github.com/saifuddin778/QDA/raw/master/images/QDA.png ""), and one with maximum output is the predicted class for the given input.
