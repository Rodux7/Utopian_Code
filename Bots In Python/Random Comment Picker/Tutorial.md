### Introduction
Hi Everyone! Today I am creating my first Utopian post. I recently got to know about Utopian while casually searching Steemit and I was like "This is perfect!". I started looking into it, what types of contributions are accepted and what categories can I contribute to. I found three categories that caught my attention and they were tutorials, development and analysis. I am developing something on the other side of the screen and it will be out soon but till it's completed I started making tutorials. The idea of this tutorial was got from @lonelywolf (Thanks!). He creates bots in nodeJS and steemJS but I am going to be recreating those bots in Python so all of you Pythoneers can understand how these bots are built and maybe start making bots for communities or something.
### What Bot Am I Going To Build And Why
The bot that I am going to be building in this post is *Random Comment Picker*. A very simple but that will pick a random comment from a post that we will assign. The reason I chose this was that I wanted to start from something basic and slowly we will move towards building complex bots. This bot can be used on multiple occasions like for giveaways or in other projects.
### What Are We Going To Be Using To Build This Bot
We will be using Beem which is a Python library that we will use to get information from Steem Blockchain and - of course - this all will be done in Python. We will also be showing the result on a web app page that will be built in Flask.
### Repository
https://github.com/python/cpython
### What Will I Learn?
In this tutorial, you will learn how you can create a bot that will pick a random comment from a post that can be used for giveaways or other projects. In the process of doing it, you will also learn these things.
- How to get comments of a post
- How to create a unique list of authors of the comment
- How to show the result on a web app built in Flask
### Requirements
- Basic knowledge of Python
- Basic knowledge of Flask
### Difficulty
- Intermediate
### Tutorial Content
#### Idea Behind It
Let me recall what we are going to be creating. There will be a website - a simple one. One that website there will be a form in which we will be able to input the post's link and then submit the info. After that, a random comment will be chosen and displayed on the screen.
### Setting Up Files
To displaying the results, as I said before we will be using Flask so setting it up should be our first step. You should have a directory completely dedicated for this project. Inside that directory create a file called  "\_\_init\_\_.py". This will be our file in which all the routes will be present. Create two folders, one named "static" and other named "templates". Create a file named "data.py", in this file all the process of getting comments and picking the random one will occur. The directory should now look like this.
```
- Main Directory
-- templates
-- static
-- __init__.py
-- data.py
```
### Getting Comments Of The Post, Filtering Them And Returning A Random Comment
Now that we have the basic files, open up the file called "data.py". Inside it, we will be creating a function that will take one parameter and that is "permalink" and then return a random comment of that post. Start by defining the function, name it "rand_com" - stands for random_comment. The first thing that we will do is to parse the link of the post because Beem only requires authorperm (i.e rodus/steemhunt-or-my-thoughts-on-it). Inside the function, create a variable called "permlink" and assign it the value ```permalink.split("@")```. If you are new to Python then this will confuse you a little but let me explain it to you.

Here's how a sample link of a post looks like ```https://steemit.com/steemhunt/@rodus/steemhunt-or-my-thoughts-on-it```. Here's what Beem wants from this url ```rodus/steemhunt-or-my-thoughts-on-it```. By using split() function, we will split the permalink into a list. The first string in the list will be ```https://steemit.com/steemhunt/``` and second string will be ```rodus/steemhunt-or-my-thoughts-on-it```. Now we have got what we want to be able to get information about this post. Here's how the function looks like until now.
```
def rand_com(permalink):
  permlink = permalink.split("@")
```
Before we move forward we need to import Comment from beem.comment. To do that first we need to make sure that Beem is installed and after that at the top of the file, type ```from beem.comment import Comment```. Let's get back to the function. On the next line, type ```c = Comment(permlink[1])```. We created a variable known as "c" in the previous line of code then assigned it the value Comment. In the Comment, we passed in the permlink as the parameter and we want the second part of the string to be there because that is authorperm. In the next line, we are going to be creating another variable called "comments" and assign it the value ```c.get_replies()```. The get_replies() gets all the comments of the post. Here's how the function looks like until now.
```
def rand_com(permalink):
  permlink = permalink.split("@")
  c = Comment(permlink[1])
  comments = c.get_replies()
```
Now that we have all the comments of the post, we will need to filter it. We want to have everyone equal chance of winning so we will only take one comment from an author. To do this we will create a list called "unique_authors" and we will put every author's name on it whose comment is counted but for now leave it as an empty list ```[]```. Create another variable known as "unique_com" - meaning unique comments. Counted comments from unique authors will be added to this list but for now, leave it as an empty list for now. Now that we have two important variables created, we will create a for loop that will loop through each comment and then check if the author is in the "unique_authors" list and then if he is not then it will add the author of that post to the "unique_authors" list and then add the comment to "unique_com" list. Here's how it's done.
```
  for com in comments:
    if com["author"] not in unique_authors:
      unique_authors.append(com["author"])
      unique_com.append(com)
```
com is used as a short form of "comment". If you don't know ```.append``` appends the value in the list at the last. This is what we have done until now.
```
from beem.comment import Comment

def rand_com(permalink):
  permlink = permalink.split("@")
  c = Comment(permlink[1])
  comments = c.get_replies()
  unique_authors = []
  unique_com = []
  for com in comments:
    if com["author"] not in unique_authors:
      unique_authors.append(com["author"])
      unique_com.append(com)
```
We have almost everything done for this function. The last thing that we have to do is to return a random comment. For this, we will use randint from a library known as random. We have to first import it, you can do that by typing ```from random import randint``` at the top of the file. By the way, randint is a short form of "random integer". It takes two parameters, e.g if we pass in 0 and 10 then it will return a random integer between 0 and 10. Here's what we will do to get a random comment. All the unique comments are stored in a variable called "unique_com" so we will first get the number of comments we have on that list. We can do that by using ```len()``` function. Create a variable called num_com and set it to ```len(unique_com)```. The number of unique comments we have been stored inside that variable now. Now we just have to do one last thing and that is to return a random comment. You can do this by typing ```  return unique_com[randint(0, num_com)]```, this will return a random comment. Here's how the data.py looks like now.
```
from beem.comment import Comment
from random import randint

def rand_com(permalink):
  permlink = permalink.split("@")
  c = Comment(permlink[1])
  comments = c.get_replies()
  unique_authors = []
  unique_com = []
  for com in comments:
    if com["author"] not in unique_authors:
      unique_authors.append(com["author"])
      unique_com.append(com)
  num_com = len(unique_com)
  return unique_com[randint(0, num_com)]
```
### Setting Up Flask
Now that we have created the function that takes in a link and returns a random comment of that post, let's move on to building the website. The website will be very simple, it will just have an input field in the middle and a submit button below it. We are not going to be adding any stylish styles - I mean we are going to but I will not be teaching that part. Let's just start by creating a basic flask application to get the basic code that we need. Open up the \_\_init\_\_.py, inside it we will first import Flask. You can do that by typing ```from flask import Flask```. On the next line type, ```app = Flask(__name__)```. This will let Flask know that the name of our app is "app" which is okay for this app. On the next line, we will create our first route which will be very simple for now and will return a simple string that is "Hi". Here's what is our route going to look like.
```
@app.route("/")
def index():
    return "Hi"
```
At the last, one the next line, type this block of code.
```
if __name__ == "__main__":
    app.run()
```
This is how our whole \_\_init\_\_.py will look for now. You can also check out all this code on the Github Repository present at the end of the tutorial.
```
# Imports
from flask import Flask

# Variables
app = Flask(__name__)

# Routes
@app.route("/")
def index():
  return "Hi"

# Run App
if __name__ == "__main__":
  app.run()
```
I have added some optional comments to help you better understand the code and what is happening in each section. Here's how it looks like when we run the app. By the way, it can be done by simply running the file by typing ```python __init__.py``` on the terminal once you are in the directory.
![steem.png](https://ipfs.busy.org/ipfs/QmWezcvRyf6MkuNg1fi3Yy1vgDwkW4LBq8hZsk5p8MXfYj)
Now - of course - we are not going to put all the html in the \_\_init\_\_.py because that's never a good practice and you should never to that. Instead we are going to be creating a template inside the templates folder and return it. Open the templates folder, create a file named "index.html" inside it and open it. Inside that html file, just paste this html code.
```
<DOCTYPE html>
<html>
<head>
    <title>Random Comment Picker</title>
</head>
<body>
    <p>RANDOM COMMENT PICKER</p>
</body>
</html>
```
Just for some basic code, this will be enough. Open the \_\_init\_\_.py file, and then instead of returning string we will return template. For that, we will first import ```render_template``` module from flask. Where it is written ```from flask import Flask``` add a comma and change it to ``` from flask import Flask, render_template```. Now it was return ```return "Hi"``` change it to ```return render_template("index.html")```. Now run the file and open it on the local host (http://127.0.0.1:5000/). Here's how it will look like right now.
![steem.png](https://ipfs.busy.org/ipfs/QmRJZmvyYU54bdUkrywpYDd6MamEeYDqmFz1oGAmMXbeyb)
Nothing really fancy, just a simple website that shows some text for now but it will change after some time. There is going to be form on the home/index page so let's start creating it. First thing you should do is to ensure that wtf_forms has been installed. After that, open the \_\_init\_\_.py file and import it by typing ```from flask_wtf import FlaskForm``` on the top and then on next line ```from wtforms import StringField```. Under the variables create a class called "post_link" and it will inherit from FlaskForm. Inside this, we will be creating the fields that will be present in our form. We will have only one field and that is "link". So under the defining the class, type ```link = StringField("Post Link")```. Now we have created the form. We will need to create a variable called "form" inside the route and then assign it the form that we created after that pass it through the template. The next thing we have to do now is to set up a secret key for our app for some protection. You can do that by typing ```app.config["SECRET_KEY"] = "abracadabra"``` in the variables section. Remember to change your key. Here's how the code will be looking right now.
```
# Imports
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField

# Variables
app = Flask(__name__)
app.config["SECRET_KEY"] = "abracadabra"

# Classes For Forms
class post_link(FlaskForm):
    link = StringField("Post Link")

# Routes
@app.route("/")
def index():
  form = post_link()
  return render_template("index.html", form=form)

# Run App
if __name__ == "__main__":
  app.run()
```
The next things it to show the form and this is very simple. Open the index.html file from the templates folder and then in the body tag. Type this under the paragraph tag.
```
    {{ form.csrf_token }}
    {{ form.link }}
    <input type="submit" value="Submit">
```
Now the file's code will look like the code present below.
```
<DOCTYPE html>
<html>
<head>
    <title>Random Comment Picker</title>
</head>
<body>
    <p>RANDOM COMMENT PICKER</p>
    {{ form.csrf_token }}
    {{ form.link }}
    <input type="submit" value="Submit">
</body>
</html>
```
You can now run the server and you will see an input bar and a submit button as present in the image below. We haven't done anything fancy. Here's how it looks like.
![steem.png](https://ipfs.busy.org/ipfs/QmPgDVatL8xrkATXQ5EVfya32yRhvrhg5DHgssTndZN5jZ)
Now we will be creating another route to which the submit button will redirect to when we click the submit button but before it we will import the function that we created in data.py file. You can do that by typing ```from data import rand_com```. The route is going to be a dynamic route which means that it will change from time to time. Below the previous route copy and paste this code.
```
@app.route("/@<author>/<permlink>")
def comment(author, permlink):
  fake_link = "https://steemit.com/steemhunt/@%s/%s" % (author, permlink)
  com = rand_com(fake_link)
  return render_template("com.html", com=com)
```
Let me explain this route a bit. The url will be something like this, ```127.0.0.1:5000/@rodus/introducing-myself```. So there will only be the author and permlink in the url. Our route will get the link from the url and then perform the function that will give us the random comment. We will also create a fake link that would be used. As we don't need the first part, it can be anything. It will be then stored in the variable called "com" and then I have passed it through the render template so we can use it. Now we will need to display that random comment. For that we will need to create "com.html". Open the templates folder and then create a file named "com.html" and then inside it copy and paste this code.
```
<DOCTYPE html>
<html>
<head>
    <title>Random Comment Picker</title>
</head>
<body>
    <h3>By {{ com["author"] }}</h3>
    <p>{{ com["body"] }}</p>
</body>
</html>
```
We are now just displaying the author and body of the comment in correct places. There is one last thing to do and that is to redirect the user when they click the submit button present on the index page. To redirect the user we will first need to import it which we can do by using a module. You can import that module by simply adding the comma after ```render_template``` and then type redirect. The import will now look like ```from flask import Flask, render_template, redirect```. Now change the index route to something like below.
```
@app.route("/", methods=["POST", "GET"])
def index():
  form = post_link(name="form")
  if form.validate_on_submit():
    data = str(form.link.data)
    authorperm = data.split("@")
    return redirect("http://127.0.0.1:5000/@" + authorperm[1])
  return render_template("index.html", form=form)
```
There are plenty of things that we have done here. First of all, we have allowed both "POST" and "GET" methods but the form is taking place on this route. After that, we have created an if statement that will be run when the form is submitted and validated. Inside that, if statement, we have converted the "link" data into a string. Then we have parsed/split it into a list because we only want the front part. At last, we have redirected the user to another route in which random comment will be shown. Everything is completed. Let's see it in action!
### Working
Normal index page with one input field and a submit button. The cool thing about this is that you can input link of any steem front-end whether it is Busy, SteemHunt or any other. After pasting the link click submit.
![steem.png](https://ipfs.busy.org/ipfs/QmUh64MbgDgTYytMVU983eoi69XBnSLF9dQdoABfseH6pi)
This is how random comment is then displayed on the screen. Of course, you can make it better by using some CSS or Bootstrap but for now I just wanted to show you how it's done and I think I have succeeded in it.
![steem.png](https://ipfs.busy.org/ipfs/QmRuhfZpxgqbvL4j6mV4Sf3o41NpEymEmeu4tTqwYh9thh)
### End Of Tutorial
Thanks for reading this tutorial and I hope that you found it useful. If you have any suggestion for the next tutorial that you would like me to do then leave them in the comment section down below. Stay tuned for the next part! See Ya!
### Proof Of Work
[Github Repository](https://github.com/Rodus7/Utopian_Code)
[Github Profile](https://github.com/Rodus7)
### Original Post
[Steemit Post](https://steemit.com/rodustutorials/@rodus/bots-in-python-1-or-random-comment-picker)
