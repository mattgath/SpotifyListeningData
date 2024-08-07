#Author: Matthew Gathman

#Adding libraries to read in the .json and display the data
import json
import matplotlib.pyplot as plt

def addSongs(data,fileName):
    for entry in data:
        if "Audio" in fileName:
            track_name=entry.get('master_metadata_track_name')
            ms_played=entry.get('ms_played')/1000
        elif "StreamingHistory" in fileName:
            track_name=entry.get('trackName')
            ms_played=entry.get('msPlayed')/1000
        if track_name in uniqueSongList:
            x=uniqueSongList.get(track_name)[0]
            y=uniqueSongList.get(track_name)[1]
            uniqueSongList[track_name]=[x+1,y+ms_played]
        else:
            uniqueSongList[track_name]=[1,ms_played]
#Function for opening the .json file and to call the addSongs function to immediately add the songs to the main dictionary
def newFile(fileName):
    with open(fileName, encoding='utf-8') as json_file:
            addSongs(json.load(json_file),fileName)

def displayBarGraph():
    #Variable for the minimum amount of listens to be displayed on the bar graph
    minAmtListens=250

    #Filter out the songs that do not have the minimum amount of listens and sort the data from least to most
    filtered_data = {track: values for track, values in uniqueSongList.items() if values[0] > minAmtListens}
    sorted_data = dict(sorted(filtered_data.items(), key=lambda item: (item[1][0], item[1][1]), reverse=True))

    #Gets the data in workable lists for the garph
    tracks = list(sorted_data.keys())
    listens = [values[0] for values in sorted_data.values()]

    #Adjustments for the graph
    fig_width = 14
    fig_height = min(len(tracks) * 0.5, 15)  # Maximum height to prevent excessive size

    # Create a figure and axis
    _, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Bar Graph
    bar_width = 0.5
    bars = ax.barh(tracks, listens, height=bar_width, color='skyblue')
    ax.set_xlabel('Number of Times Listened', fontsize=5)
    ax.set_title('Number of Times Listened per Track', fontsize=5)

    # Add labels to bars
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.5, bar.get_y() + bar.get_height() / 2, f'{width}', 
                va='center', ha='left', fontsize=5)

    # Adjust the font size of the y-tick labels
    plt.yticks(fontsize=5)
    plt.show()

uniqueSongList={}
newFile('Audio-2023_4.json')
newFile('Audio-2017-2019.json')
newFile('Audio-2022-2023.json')
newFile('Audio-2020-2022.json')
newFile('Audio-2019-2020.json')
newFile('StreamingHistory0.json')
newFile('StreamingHistory1.json')
displayBarGraph()