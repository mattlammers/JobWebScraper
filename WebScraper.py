from bs4 import BeautifulSoup
import urllib

def indeed_scraper(url):
    results = 'Indeed Results\n\n'

    urlHtml = urllib.urlopen(url)
    if urlHtml.getcode() is 200:
        soup = BeautifulSoup(urlHtml.read(), 'html.parser')

        for job in soup.find_all(True, {'class':' row result'}):
            jobTitle = job.find(True, {'class':'turnstileLink'}).text
            href = 'http://www.indeed.com' + job.find(True, {'class':'turnstileLink'}).get('href')
            jobCompany = job.find(True, {'class':'company'})
            companyName = jobCompany.find(True, {'itemprop':'name'}).text.strip()
            jobLocation = job.find(True, {'class':'location'})
            location = jobLocation.find(True, {'itemprop':'addressLocality'}).text
            results = results + '{0}\n{1}  {2}\n{3}\n'.format(jobTitle, companyName, location, href) + '\n'
    else:
        print('Indeed.com Error Code:{0}'.format(urlHtml.getcode()))
    
    return results

def simply_scraper(url):
    results = 'Simply Hired Results\n\n'

    urlHtml = urllib.urlopen(url)
    if urlHtml.getcode() is 200:
        soup = BeautifulSoup(urlHtml.read(), 'html.parser')

        for job in soup.find_all(True, {'class':'card js-job'}):
            jobTitle = job.find(True, {'class':'serp-title'}).text
            href = 'http://www.simplyhired.com' + job.find(True, {'class':'card-link js-job-link'}).get('href')
            jobCompany = job.find(True, {'class':'serp-company'}).text.strip()
            jobLocation = job.find(True, {'class':'serp-location'}).text.strip()
            results = results + '{0}\n{1}  {2}\n{3}\n'.format(jobTitle, jobCompany, jobLocation, href) + '\n'
    else:
        print('Simply Hired Error Code:{0}'.format(urlHtml.getcode()))

    return results

results = ''

urlList = ["http://www.indeed.com/jobs?sort=date&jt=fulltime&q=software+engineer&l=Longmont%2C+CO&radius=15",
           "http://www.simplyhired.com/search?q=software+engineer&l=longmont%2C+co&fdb=1&sb=dd"]

for urls in urlList:
    if "www.indeed.com" in urls:
        results = results + indeed_scraper(urls)
    elif "www.simplyhired.com" in urls:
        results = results + simply_scraper(urls)

print(results)
