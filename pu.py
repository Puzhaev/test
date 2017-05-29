import bs4
import  requests
import sqlite3
import urllib2

conn = sqlite3.connect('Chinook_Sqlite.sqlite')
cursor = conn.cursor()


class Novosti:
    name = ''
    data = ''
    photo = ''
    author = ''
    
    def __init__(self,name , data, photo,author):
        self.name = name
        self.data = data
        self.photo = photo
        self.author = author


def  info  ( url ):
    data  = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(data, 'html.parser')
    
    c = Novosti( soup.title.text  ,soup.find('span', {'class': "article-content__data-date"}).text , soup.find(property="og:image").text , soup.find('a', {'class': "article-content__data-authors"}).text    )
    cursor.execute(" insert into inf values ('%s', '%s', '%s', '%s');" %(answer.name, answer.data, answer.photo, answer.author))

for i in range(10):
    info(input())





conn.commit()