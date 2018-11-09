# Ideas:

- Look at all of the LeBron James nicknames I find
- Find inside jokes


# Process Ideas from Roberto

I have my **reddit comments**

## then CLEANUP

* English
* alpha numeric
* punctuation
* lowercase
* stop words

## then TOKENIZE

#### Maybe even train/test/split here before?!?!
* 

## then Matrix

#### NOTE: You should Train/Test/Split before Count Vectorizing to do be able to later test supervised learning models.

Options:
* CountVectorize
* TF-IDF
* Word2Vec
  * Comparison
  * 
  
  
Problem with matrices? Is we are blowing up our data into huge sparse matrices with tons of value-less zeroes.

So why Dim Red (below)? This will help us smush our ginormous count of features into LESS interpretable features, but fewer.
Then we can make our **documents (reddit comments)** have a few features and allow us to do some ML techniques on them.

## Dimensionality Reduction (LDA)

* PCA
* NMF
* LDA
* LSA / LSI


## Unsupervised Learning

* Clustering (KMeans, DB Scan, Hierarchial)

## Supervised (Classification or Regression)

* Random Forest, Decision Trees, etc etc
* Poisson distribution of how many "points" a reddit comment will receive

## Comparison / Similarity

* see which comments are most similar (Cosine similarity, or Euclidian distance)
  * then do some aggregate grouping with this
  
## Visualizations

* PCA
* t-she


## Train / Test Split

If you split data, and then do a countvectorizer on your training data. Your test data will have a matrix which is highly likely to have some words that your training data never saw. Thus, one good way in your training data matrix is to create an 'EVERYTHING ELSE' category and that would group everything else there. Thus.
^^ Dan says to ignore this. Do fit_transform like normal on training set. and then ONLY transform on test set. Because it's native to simply ignore words in the test set it has never seen before.









# Next steps:
1. I want to find the X topics/clusters about these texts. Perhaps it's fitness, politics, training, performance, GOAT.
  * Stem and lemmative better.
  * Inclue n_grams in my grouping
  * Continue with LDA and find then LABEL some groups that make sense.
2. Figure out which topic each document best corresponds to, and place the document within that topic/cluster
3. Chart a stacked-bar or a multi-line chart for each year (or month, or something else) from 2011-2018, and show
   the PERCENTAGE (Or COUNT) of each topic for that period of time.
4. Look at the insights! What does that mean?
5. Perhaps do sentiment analysis. See if I can find a well-trained model. Or train my own based on upvote? score? (Probably not doing this)

**NOTE**: Simply do LDA first, and make this work. Get a chart. Get some insights.
**THEN:** Make it repeatable. Get it in a function somehow. Try other Dim Red and Unclassifying and Topic modeling techniques. See what works best.