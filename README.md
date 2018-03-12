# Coding challenge

In this repo there is store-locations.csv

This is a tabular dataset of the locations of every store of a major national retail chain.

# Deliverables

Please download the file (rather than forking this repo), do the exercise, and then upload to your own repo.

Write a command-line application that uses the data to conform to the following specification (note that this specification conforms to http://docopt.org/)

```
Find Store
  find_store will locate the nearest store (as the vrow flies) from
  store-locations.csv, print the matching store address, as well as
  the distance to that store.

Usage:
  find_store --address="<address>"
  find_store --address="<address>" [--units=(mi|km)] [--output=text|json]
  find_store --zip=<zip>
  find_store --zip=<zip> [--units=(mi|km)] [--output=text|json]

Options:
  --zip=<zip>          Find nearest store to this zip code. If there are multiple best-matches, return the first.
  --address            Find nearest store to this address. If there are multiple best-matches, return the first.
  --units=(mi|km)      Display units in miles or kilometers [default: mi]
  --output=(text|json) Output in human-readable text, or in JSON (e.g. machine-readable) [default: text]

Example
  find_store --address="1770 Union St, San Francisco, CA 94123"
  find_store --zip=94115 --units=km
```

Additionally:

- Please write up a paragraph or two about how your solution works, any assumptions or caveats, and put it in a readme file.
- Your solution should be well-tested in the testing framework of your choice. Commit the test suite to your repo.
- The output format is not rigidly specified. Use your judgement for both the text and json formats.

Send me a github link to the final project.

# Notes

Feel free to do this in whatever language you would like, and focus on the problem itself (rather than framework/scaffolding). Please make sure it's reasonably easy to run your code and there are clear instructions for doing so.

You will need to use an external geocoding service. However please implement the distance calculation in your own code. To the extent you need any algorithms, I'm not expecting you to invent anything from scratch, so use Google & external libraries judiciously, and cite/document appropriately.

You can add polish or an extra features if you'd like, but remember that software is about tradeoffs and *by far the most important thing is delivering working, practical software that solves the problem of finding the closest store location*. The goal is not to take up a bunch of your time, but see you solve a problem that looks very much like the type of work we do all the time.

There are a ton of different ways to skin this cat -- be smart, be practical, thanks, and good luck!
