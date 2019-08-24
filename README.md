# price_observer
Application that observes the prices of products once a day and informs by email if the price of a product is lower than a certain limit

# Usage
Follow steps below:

1. Clone the project
2. Enable Less secure app access (Gmail: https://myaccount.google.com/lesssecureapps)
3. At `credentials.txt` file, write your email address and password (so the application can send you emails) and your headers (by just google "what is my user agent" and copy and paste the result)
4. At `urls.txt` file, write the links of the products you want to observe followed by a space and the price limit you want
5. At `price_observer.py` change the html tags with the html tags that your site of interest uses (by inspecting each element)
6. Run your personalized observer with command `python price_observer.py credentials.txt urls.txt`


# **Attention**

Files `credentials.txt` and `urls.txt` must be in the same folder as the price_observer.py 
