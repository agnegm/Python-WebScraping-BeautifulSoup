#1st step : install and import the libraries/ Modules 
#install using pip in CMD 
#pip install lxml (parser)
#pip install requests 
#pip install beautifulsoup4
import requests 
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

#lists used to save the text of the contents 
job_titles_txt = []
companies_name_txt =[]
companies_location_txt=[]
links_txt = []
page_num = 0

        
#2nd step : use the request to fetch the URL of the web page 
result = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=python&start={page_num}") #f -> format string (using to add variable to string )

#3rd step : save the content of the web page 
src = result.content
#print(src)

#4th step : create the beatifulsoup object to parse the content 
soup = BeautifulSoup(src,"lxml")
#print(soup)

#5th step : finding the important content which i need 
#job title , company name , company location  
#soup.find_all return a list 

job_titles = soup.find_all("h2",{"class":"css-m604qf"}) 
#print(job_titles)
companies_name = soup.find_all("a" ,{"class":"css-17s97q8"}) 
#print(companies_name)
companies_location = soup.find_all("span",{"class":"css-5wys0k"})
#print(companies_location)


#6th step : Extracting only the text of the content using for loop 
# (1- loop over every list of the contents
#  2- extract text 
#  3- save the results in another list for each list    )

for i in range (len(job_titles)):
    job_titles_txt.append(job_titles[i].text)
    companies_name_txt.append(companies_name[i].text)
    companies_location_txt.append(companies_location[i].text)


#print(job_titles_txt, companies_name_txt , companies_location_txt )    

#7th step : create a CSV file and fill it with values of jobs 
#use unpacking and zip longest to fit the lists 
file_list = [job_titles_txt,companies_name_txt,companies_location_txt]
final_list =zip_longest(*file_list) 
with open( ".\Python Jobs.csv","w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Job Title ","Company Name","Company Location"])
    wr.writerows(final_list)

#8th step : Extracting elements from inner pages (links)

#9th step : Extracting from multiple pages (request + page number logic )