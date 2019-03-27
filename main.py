"""
'Python-is-Easy' Homework #2 (Functions)
DESCRIPTION: 
The main goal of this file created, is to get acquianted with functions in Python.  It is the second homework assigment in the
'Python is Easy' course, from Pirple.

Three functions are created, each of which would call a specifc attribute according to the name of the function.   
"""


def NameOfSong():
	Title = "In the End" # This is the name of the song.
	return Title

def NameOfBand():
	Artist = "Linkin Park"
	return Artist

def DateRecorded():
	RecordedDate = 2000
	print(RecordedDate)

Album = "Hybrid Theory"
Genre = "Nu metal - Rap Rock"
DurationInSeconds = 216 # This is the length of the song in seconds.
DurationInMinutes = 3.6
ReleaseDate = "October 9, 2001"
Label = "Warner Bros." # The Record Label company who published the song. 
WikipediaPage = "https://en.wikipedia.org/wiki/In_the_End" # Added the Wikipage as reference on where I got the informtion from.

print(NameOfSong())

Artist = NameOfBand() #trying different ways to call a function
print(Artist)

DateRecorded()

# print(Title)
# print(Artist)
# print(Album)
# print(Genre)
# print(DurationInSeconds)
# print(DurationInMinutes)
# print(RecordedDate)
# print(ReleaseDate)
# print(Label)
# print(WikipediaPage)