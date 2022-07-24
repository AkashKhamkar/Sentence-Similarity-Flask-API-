# Sentence-Similarity-Flask-API-
<p> The sentence_similarity.py file contains the flask app and the query.py file contains an example query and below is an example output obtained:</p>

<h2> 1. sentence_similarity.py file </h2>

-   I have used pretrained "<b>all-MiniLM-L6-v2</b>" model from the Hugging Face library which is trained on more than 1 billion sentence pairs. 
-   This model basically maps the sentences & paragraphs to a 384 dimensional dense vector space.
-  This file contains the code for the flask app and api and the model loading and tokenizing as well as generating the output.

<h2> 2. query.py file </h2>

-  This file contains and example query with 2 sentences.
-  Below is the output obtained when executing the query.py file

<h2> Query with 2 sentences: </h2>

![image](https://user-images.githubusercontent.com/34622497/180644397-0dad048e-3f2f-45f5-8ef6-1afc1c4f38d2.png)


<h2> OUTPUT: </h2>

(![image](https://user-images.githubusercontent.com/34622497/180644383-4bb16fcc-c4e2-4491-8cf1-68ced5bb79de.png)





-   Here I have used ngrok library as the project was done in gogle collab.
-   As local hosting can't be done in google collab I have used ngrok_flask library.
-   ngrok basically allows you to host the flask app on ngrok domain instead of local hosting.
-   Also this flask app is easily deployable anywhere with or without the ngrok library and the api works perfectly.
