from bs4 import BeautifulSoup
import urllib

def indeed_scraper(url):
    print('Indeed.com results')
    urlHtml = urllib.urlopen(url)

    soup = BeautifulSoup(urlHtml.read(), 'html.parser')

    for job in soup.find_all(True, {'class':' row result'}):
        jobTitle = job.find(True, {'class':'turnstileLink'}).text
        jobCompany = job.find(True, {'class':'company'})
        companyName = jobCompany.find(True, {'itemprop':'name'}).text.strip()
        jobLocation = job.find(True, {'class':'location'})
        location = jobLocation.find(True, {'itemprop':'addressLocality'}).text
        print('{0}\n{1}  {2}\n'.format(jobTitle, companyName, location))

def simply_scraper(url):
    print('Simply Hired results')
    urlHtml = urllib.urlopen(url)

    soup = BeautifulSoup(urlHtml.read(), 'html.parser')

    for job in soup.find_all(True, {'class':'card js-job'}):
        jobTitle = job.find(True, {'class':'serp-title'}).text
        jobCompany = job.find(True, {'class':'serp-company'}).text.strip()
        jobLocation = job.find(True, {'class':'serp-location'}).text.strip()
        print('{0}\n{1}  {2}\n'.format(jobTitle, jobCompany, jobLocation))

urlList = ["http://www.indeed.com/jobs?q=software+engineer&l=Longmont%2C+CO&jt=fulltime&explvl=entry_level&sort=date",
           "http://www.simplyhired.com/search?q=software+engineer&l=longmont%2C+co&fdb=1&sb=dd"]

for urls in urlList:
    if "www.indeed.com" in urls:
        indeed_scraper(urls)
    elif "www.simplyhired.com" in urls:
        simply_scraper(urls)
