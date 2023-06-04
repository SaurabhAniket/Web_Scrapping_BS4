from bs4 import BeautifulSoup
import requests
import time

print('Put Some skill that you are not familiar with')
unfamiliar_skills = input('>')
print(f'Filtering out {unfamiliar_skills}')
def find_jobs():
    html_text  = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    # print(html_text) #request accept sucessful
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index , job in  enumerate (jobs):
        published_date = job.find('span' , class_ ='sim-posted').span.text
        if 'few' in published_date:
            #print(job)
            company_name = job.find('h3' , class_ = 'joblist-comp-name').text.replace(' ','')
            # companys_name = soup.find_all('h3' , class_ = 'joblist-comp-name').text
            #print(company_name)
            # print(companys_name)
            skills = job.find('span' , class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                with open(f'posts/{index}.txt' , 'w') as f:
                #print(skills) 
                    f.write(f"Company Name : {company_name.strip()}")
                    f.write(f"Required Skills: {skills.strip()}")
                    f.write(f"Published Date: {published_date.strip()}")
                    f.write(f'More Info:{more_info}')
                print(f'File Saved: {index}')
    
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} Minutues...')
        time.sleep(time_wait*60)