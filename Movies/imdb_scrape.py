import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from .models import MoviesList

#a=MoviesList.objects.all()
def imdb():
    my_url='https://www.imdb.com/chart/top'
    uClient=uReq(my_url)
    page_html=uClient.read()
    uClient.close()
    page_soup=soup(page_html,"html.parser")
    containers=page_soup.findAll("tbody",{"class":"lister-list"})
    container=containers[0]
    #print(soup.prettify(containers[0]))
    name_container=container.findAll("td",{"class":"posterColumn"})
    name_container_len=len(name_container)


    rating_container=container.findAll("td",{"class":"ratingColumn imdbRating"})
    rating_container_len=len(rating_container)

    #filename="ratingss.csv"
    #f=open(filename,"w")

    #headers="Movie Name,Ratings,Users\n"
    #f.write(headers)


    for i in range(name_container_len-1):
        name=name_container[i].a.img["alt"]
        rating=rating_container[i].strong["title"]
        
        

        #print("Movie name"+name)
        #print("Rating"+rating)

        #stringParsing
        

        split_rating=rating.split(" ")
        final_rating=split_rating[0]
        users=split_rating[3]
        mname=MoviesList.objects.get(movie_name=name)
        if not mname:
            movie=MoviesList(movie_name=name,movie_rating=final_rating,rating_users=users)
            movie.save()
        
            

        #print(name + "," + final_rating + "," + users.replace(",","") +"\n")
        #f.write(name + "," + final_rating + "," + users.replace(",","") + "\n")

    #f.close()
        



