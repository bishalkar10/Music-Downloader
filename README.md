# Music Download branch - 'extra'
## About  
This programme is built on Pyhton v3.11.2. To use this programme follow the instructions below. After you have installed the programme then visit https://pagalfree.com . Visit a page what looks like this :  
![Sample Image from where to get the website link](./images/website%20sample%20image.png) 

***Note*** : This project is built on a windows 10 laptop. So, the path of the directory is set according to the windows 10. If you are using any other operating system This function may not work as intended or not work at all. If you are using windows 10 then you can use this programme without any problem.    
## Requirements   
To use this programme in your computer you need to have Python3 installed on your computer. You can download the **Python3** from [here](https://www.python.org/downloads/) if not downloaded. 
You need to install few packages to use this programme on your computer.   
1. **requests**
2. **BeautifulSoup4**
3. **lxml**

## Intallation    
1. Go to the GitHub page of the repository you want to fork. The repository should be public and accessible.
2. On the top-right corner of the repository page, you will find a button labeled "Fork". Click on the "Fork" button.
3. You will be redirected to a new page where GitHub will create a copy of the repository under your GitHub account. 
4. Find the ***code*** button on the top right corner of the repository and click on it and copy the repo url.
5. Create folder on your computer and open the folder in the your IDE. Then open git bash terminal and type the following commands :    
```bash  
git clone 'your git repository link' 
pip install -r requirements.txt
```  
     
## Usage   
create isntance of *MusicDownloader* copy the url shown in the image : 

```python
downloader = MusicDownloader()  
url = 'https://pagalfree.com/music/bang-bang1-2014' 
downloader.download_music(url) 
```   
It will start downloading the music in the 'Music' folder. It is set as default. The download_music() takes two argument first one is the mandatory *url* and second one is the optional *music quality*. It can be only **low** or **high**. If you don't pass the second argument then it will download the music in low quality.   
###change the download path:   
To change the download path you need to type  :

```python 
change_directory() 
```     
and hit enter. It will ask you to enter the path. Either copy paste the path or write a path and hit enter. It will change the download path and create a directory.txt file in the same folder. It will save the path in the directory.txt file. Next time you run the programme it will automatically change the download path to the path you have entered.   

## Author    
Bishal Kar (Gain Prasad Kar) 

***GitHub Profile*** : [Gain Prasad Kar](https://github.com/bishalkar10) 
***Linkedin Profile*** : [Gain Prasad Kar](https://www.linkedin.com/in/bishalkar10/)