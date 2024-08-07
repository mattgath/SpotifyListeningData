# SpotifyListeningData
# Description
This project analyzes and visualizes audio streaming data from Spotify by processing JSON files that contain streaming history. It aggregates the number of times each track has been listened to and the total playtime. The project then generates a bar graph to display the number of listens for each track, filtered to include only tracks with more than a specified number of listens.

# Features
Data Aggregation: Reads and aggregates song play counts and total playtime from JSON files.
Visualization: Generates a bar graph showing the number of times each track was listened to.
Filtering: Allows filtering of tracks based on the minimum number of listens.
# Requirements
Python 3.x
matplotlib library
json library (part of Python standard library)


# Code Overview
addSongs(data, fileName): Aggregates song play counts and durations from the provided data based on the file name.
newFile(fileName): Opens a JSON file, reads its contents, and calls and songs to add the data to the main dictionary.
displayBarGraph(): Filters and sorts the aggregated data, then generates and displays a bar graph showing the number of times each track was listened to.

# Issues Overcame
There were issues with the JSON files containing my decrypted IP address that I had to write a separate program to remove. Additionally, graph spacing has been an issue while working on the project, which is why there is a minimum amount of time I listened to make the graph.

Author
Matthew Gathman

