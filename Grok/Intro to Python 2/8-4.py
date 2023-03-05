import string
import collections
hashtags = []

tweet = input("Tweet: ")
while tweet:
  tweet_list = tweet.split()
  for word in tweet_list:
    if '#' in word[0]:
      hashtags.append(word.lower().rstrip(string.punctuation))
  tweet = input("Tweet: ")

"""
master = ["#Python is #AWESOME!", "This is #So_much_fun #awesome"]
for tweet in master:
  tweet = tweet.split()
  for word in tweet:
    if '#' in word:
      hashtags.append(word.lower().rstrip(string.punctuation))
"""
      
hashtag_counts = collections.defaultdict(int)
for hashtag in hashtags:
  hashtag_counts[hashtag] += 1
#print(hashtag_counts)

for output in hashtag_counts:
  print(output, hashtag_counts[output])

#print(hashtags)