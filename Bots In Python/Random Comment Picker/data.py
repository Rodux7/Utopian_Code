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
