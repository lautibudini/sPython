from collections import Counter
import csv

def my_function(file_name):
    
    with open(file_name) as file:
       reader = csv.reader(file, delimiter=',')
       artists = Counter(map(lambda x: x[0], reader))
       return artists.most_common(10)


try:
    my_songs = my_function('songs_n ormalize.csv')
except FileNotFoundError:
    print("Tenemos un problema!!")
finally:
    for song in my_songs:
        print(song)
