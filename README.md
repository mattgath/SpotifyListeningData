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
# Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/spotify-listening-history-analyzer.git
Navigate to the project directory:

bash
Copy code
cd spotify-listening-history-analyzer
Install the required libraries:

bash
Copy code
pip install matplotlib
Usage
Place your JSON files containing Spotify streaming history in the project directory. Supported files include:

Audio-YYYY_MM.json (or similar)
StreamingHistoryX.json
Modify the newFile function calls in the script to include the paths to your JSON files.

Run the script:

bash
Copy code
python your_script_name.py
This will process the JSON files, aggregate the data, and display a bar graph of the number of times each track was listened to.

Code Overview
addSongs(data, fileName): Aggregates song play counts and durations from the provided data based on the file name.
newFile(fileName): Opens a JSON file, reads its contents, and calls addSongs to add the data to the main dictionary.
displayBarGraph(): Filters and sorts the aggregated data, then generates and displays a bar graph showing the number of times each track was listened to.
Example
python
Copy code
import json
import matplotlib.pyplot as plt

def addSongs(data, fileName):
    # Implementation here

def newFile(fileName):
    # Implementation here

def displayBarGraph():
    # Implementation here

uniqueSongList = {}
newFile('Audio-2023_4.json')
newFile('Audio-2017-2019.json')
newFile('Audio-2022-2023.json')
newFile('Audio-2020-2022.json')
newFile('Audio-2019-2020.json')
newFile('StreamingHistory0.json')
newFile('StreamingHistory1.json')
displayBarGraph()
License
This project is licensed under the MIT License - see the LICENSE file for details.

Author
Matthew Gathman

