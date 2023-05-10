import requests
from bs4 import BeautifulSoup
import os  


class MusicDownloader:

    def __init__(self):
        self.quality_dict = {'low': 0, 'high': 1}  # a dictionary to with value 0 and 1 to be used as link index
        self.directory = 'Music'
        self.load_directory()           # load the directory each time programme runs

    def download_music(self, url : str, quality : str = 'low') -> None:
        """
        Downloads an MP3 file from the given URL and saves it to a directory.

        Args:
            inputs (list of str): A list containing the URL to download and an optional quality setting ('low' or 'high').

        Returns:
            None

        Example:
            >>> download_music('https://pagalfree.com/music/show-me-the-thumka-2023.html', 'low')
            None

        Note:
            If no quality setting is provided, the default quality setting is 'low'.
        """  
        
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        # Find all the links to MP3 files on the page
        link = [link.get('href') for link in soup.find_all('a', class_="btn-download")]   # returns a list href links
        # print(link)
       
        # self.quality_dict['low'] = 0 and link[0] is the link to low quality mp3 file
        mp3_response = requests.get(link[self.quality_dict[quality]]) 
        filename = link[self.quality_dict[quality]].split("/")[-1][4:] 
        
        print(f"Downloading {filename}...") 
        
        with open(os.path.join(self.directory, filename), 'wb') as f:
            f.write(mp3_response.content)
        print("Download completed successfully!") 

    # Function to change the file directory where music will be downloaded
    def change_directory(self) -> None :  
            # Ask user to enter new directory path store as a raw string and then replace all backslashes with forward slashes
            new_directory = input(r'Enter new directory path : ') 
            self.directory = new_directory.replace("\\", "/")  
            # If path doesn't exist, create the directory.txt file and store the new directory path
            if not os.path.exists(self.directory) : 
                os.makedirs(self.directory)      
                with open('directory.txt', 'w') as f : 
                    f.write(self.directory) 
            else : 
                with open('directory.txt', 'w') as f : 
                    f.write(self.directory)

    # Function to load the directory from a text file
    def load_directory(self) -> None: 
            # if the directory.txt file exists, read the first line and store it as the directory where music will be downloaded
            if os.path.exists('directory.txt'):
                with open('directory.txt', 'r') as f:
                    self.directory = f.readline().strip() 
            # if the directory.txt file does not exist, set the default directory as Music
            else:
                self.directory = 'Music'
                if not os.path.exists(self.directory):
                    os.makedirs(self.directory)



# Create downloader instance and download music 
if __name__ =="__main__" : 
        
    downloader = MusicDownloader() 
    # downloader.change_directory()
    print(downloader.directory)

    url = 'https://pagalfree.com/music/bang-bang1-2014'
    downloader.download_music(url) 
    
