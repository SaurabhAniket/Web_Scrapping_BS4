from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

print('Put some skill that you are not familiar with')
unfamiliar_skills = input('> ')
print(f'Filtering out {unfamiliar_skills}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    job_data = []

    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skills not in skills:
                job_info = {
                    'Company Name': company_name.strip(),
                    'Required Skills': skills.strip(),
                    'Published Date': published_date.strip(),
                    'More Info': more_info
                }
                job_data.append(job_info)
                print(f'File Saved: {index}')

    if job_data:
        df = pd.DataFrame(job_data)
        df.to_excel('job_data.xlsx', index=False)
        print('Data saved to job_data.xlsx')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
