#Create list for different apps
playlist = ["Shape Of You", "Naa Ready", "Believer", "Tum Hi Ho"] #Spotify
favourite_foods = ["Pizza","Burger", "Dosa", "Biryani"] # Zomato
recent_locations = ["Home", "Airport", "Work", "Mall"] # Uber

print("Spotify Playlist:", playlist)
print("Zomato Foods:", favourite_foods)
print("Recent Locations:", recent_locations)


#List Methods:

playlist.append("oo antava")
print("after append", playlist)

playlist.insert(1,"Deva Deva Deva")
print("after insert", playlist)

playlist.remove("Naa Ready")
print("after removing", playlist)

playlist.pop()
print("after pop", playlist)

playlist.reverse()
print("after reverse", playlist)

print("count ",playlist.count("Shape Of You"))

#List Slicing:

print("top 2 songs", playlist[0:2])