import requests
import csv
import pandas as pd

# List of movie IDs
df = pd.read_csv('/Users/yvette/Desktop/film/id_df.csv')
id_list = df['id'].tolist()

# Headers for the API request
headers = {
    "accept": "application/json",
    "Authorization": "{api_key}"
}


# Initialize lists to hold cast and crew data
cast_data = []
crew_data = []

# Process each movie ID
for movie_id in id_list:
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=en-US"
    response = requests.get(url, headers=headers)
    data = response.json()

    # Add movie_id to each cast and crew entry
    for cast_member in data.get('cast', []):
        cast_data.append({
            'movie_id': movie_id,
            'cast_id': cast_member.get('cast_id'),
            'name': cast_member.get('name'),
            'character': cast_member.get('character'),
            'gender': cast_member.get('gender'),
            'order': cast_member.get('order'),
            'id': cast_member.get('id')
        })

    for crew_member in data.get('crew', []):
        crew_data.append({
            'movie_id': movie_id,
            'credit_id': crew_member.get('credit_id'),
            'name': crew_member.get('name'),
            'department': crew_member.get('department'),
            'job': crew_member.get('job'),
            'gender': crew_member.get('gender'),
            'id': crew_member.get('id')
        })
    print(f"Movie ID {movie_id} has been processed.")
# Write cast data to CSV
with open('cast_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['movie_id', 'cast_id', 'name', 'character', 'gender','order','id'])
    writer.writeheader()
    writer.writerows(cast_data)

# Write crew data to CSV
with open('crew_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['movie_id', 'credit_id', 'name', 'department', 'job', 'gender', 'id'])
    writer.writeheader()
    writer.writerows(crew_data)

print("CSV files have been created successfully.")
