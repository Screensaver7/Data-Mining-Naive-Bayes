# Data-Mining-Amazon-Fake-Reviews
Determining fakes reviews in "Amazon Fine Foods reviews" database.

What data will you use?

https://snap.stanford.edu/data/web-FineFoods.html
http://www.scribd.com/doc/285431272/Amazon-Review-Complaint

The reviews of Amazon food products provided by the Stanford Network Analysis Project (SNAP) gives us 568,454 reviews by 256,059 users on 74,258 products between October 1999 to October 2012. Each review contains the product ID, user ID, the name of the user, the helpfulness of the review, the rating given to the product, the time it was posted, the summary of the review, and the actual text of the review. The size of the data file was 116 MB. We’ll manually select the reviews that we believe are fake as the class attribute in a small sample as the training data. The second link contained a list of usernames on a website called Fiverr who post fake reviews on Amazon. We’ll try to match it to Amazon reviewers and use them as fakes.

How will you solve the problem?

We will classify each review with yes for fake or no if not fake if a reviews based on navie bayes algorithm implemented by a program we will write for the classification tree. This program will classify the users based on the frequency of certain words that have emotional and generic wow words. We’ll also use the helpfulness, the rating given to the product, as well as the punctuation used in the summary and the actual review as attributes to determine whether the review was fake or not. Amazon recently sued 1,114 fake reviewers on Fiverr with all their Fiverr account usernames posted. We’ll try to match them with the accounts on Amazon and use their reviews as guaranteed fake reviews.

How will you evaluate your method?

We will use a subset of the data as the training set to for our program to create the probability for the classifier. Then we run it against an already classified dataset and compare the results with the know results to develop an error rate. 
