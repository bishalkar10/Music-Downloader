import requests
from bs4 import BeautifulSoup
import os 
import sys

class MusicDownloader:

    def __init__(self):
        self.quality_dict = {'low': 0, 'high': 1}  # a dictionary to with value 0 and 1 to be used as link index
        self.directory = 'Music'
        self.load_directory()           # load the directory each time programme runs    
        
    def download_music(self) -> None:
          
        while True:
            try:
                inputs = list(map(str, input("Enter URL and quality (separated by space): ").split()))
                url = inputs[0] 
                if url.lower() == 'exit' :
                    return
                #if user didn't enter quality option then set the default value to 'low'
                quality = inputs[1].strip().lower() if len(inputs) > 1 else 'low' 
                    
                if quality not in self.quality_dict:
                    raise ValueError('Invalid input. Quality must be "low" or "high".')
                break
            except Exception as e :
                print(f"An error occurred on line {sys.exc_info()[-1].tb_lineno}: \n {e}") 

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the links to MP3 files on the page
        link = [link.get('href') for link in soup.find_all('a', class_="btn-download")]   # returns a list href links
        # print(link)

        mp3_response = requests.get(link[self.quality_dict[quality]]) 
        filename = link[self.quality_dict[quality]].split("/")[-1][4:] 
        
        print(f"Downloading {filename}...") 
      
        with open(os.path.join(self.directory, filename), 'wb') as f:
            f.write(mp3_response.content)
        print("Download completed successfully!") 

    def change_directory(self) :  
            # ask user to copy paste his/her directory path
            new_directory = input(r'Enter new directory path : ') 
            self.directory = new_directory.replace("\\", "/")   # change all the '/' with '\' 

            #if this directory doesn't exists in the computer then create the directory and create a 'directory.txt' file. 
            # when next time user open the programme then the .mp3 files will be saved in the new directory.
            if not os.path.exists(self.directory) : 
                os.makedirs(self.directory) 
                with open('directory.txt', 'w') as f : 
                    f.write(self.directory)
                print(f'New directory {self.directory} has been created.')  
                print(f'Directory is change to {self.directory}')

            # if directory exists then replace directory location in the 'directory.txt' file and change the self.directory value
            else :
                with open('directory.txt', 'w') as f : 
                    f.write(self.directory) 
                print(f'Directory is change to {self.directory}')
                
    def load_directory(self): 
            #if 'directory.txt' file is available then read the directory path and set new directory
            if os.path.exists('directory.txt'):
                with open('directory.txt', 'r') as f:
                    self.directory = f.readline().strip() 
            
            else:
                self.directory = 'Music'
                if not os.path.exists(self.directory):
                    os.makedirs(self.directory)

if __name__ =="__main__" : 
        
    # Create downloader instance and download music
    downloader = MusicDownloader() 
    downloader.download_music() 
    # downloader.change_directory()

