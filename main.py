import requests
import os
import time 

def get_and_save(api_key, orientation, query, index):
    base_url = "https://api.unsplash.com/photos/random/"
    url = f"{base_url}?client_id={api_key}&orientation={orientation}&query={query}&content_filter=high"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        image_url = data["urls"]["full"]
        filename = f"wallpaper_{index}_{int(time.time())}.jpg"
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(image_response.content)
                remove_previous_wallpaper(index - 1)  
    return False

def remove_previous_wallpaper(index):
    previous_filename = f"wallpaper_{index}_*.jpg"
    
    for file in os.listdir():
        if file.startswith(previous_filename):
            os.remove(file)
            print(f"Предыдущие обои {file} успешно удалены.")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    orientation = "landscape"
    query = "tokyo"

    interval = 10

    num_images_to_download = 2

    while True:

        for i in range(1, num_images_to_download + 1):
           
            get_and_save(api_key, orientation, query, i)
            
     
            time.sleep(interval)
