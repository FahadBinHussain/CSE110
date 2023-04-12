# dict1 = {'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}
dict1 = {'sci fi': 5, 'mystery': 3, 'horror': 14, 'young_adult': 2, 'adventure': 9}

max_genre = ""
max_dict1 = -1

for genre, books in dict1.items():
    if books > max_dict1:
        max_genre = genre
        max_dict1 = books

print(f"The highest selling book genre is '{max_genre}' and the number of books sold are {max_dict1}.")