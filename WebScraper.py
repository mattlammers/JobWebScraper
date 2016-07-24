from bs4 import BeautifulSoup
import smtplib
import urllib

def indeed_scraper(url):
    results = 'Indeed Results\n\n'

    urlHtml = urllib.urlopen(url)
    if urlHtml.getcode() is 200:
        soup = BeautifulSoup(urlHtml.read(), 'html.parser')
        
        for job in soup.findAll('div', ' row result'):
            jobTitle = job.find('a', 'turnstileLink').text
            href = 'http://www.indeed.com' + job.find('a', 'turnstileLink').get('href')
            companyName = job.find(True, {'itemprop':'name'}).text.strip()
            location = job.find(True, {'itemprop':'addressLocality'}).text
            results = results + '{0}\n{1}  {2}\n{3}\n'.format(jobTitle, companyName, location, href) + '\n'
    else:
        print('Indeed.com Error Code:{0}'.format(urlHtml.getcode()))
    
    return results

def simply_scraper(url):
    results = 'Simply Hired Results\n\n'

    urlHtml = urllib.urlopen(url)
    if urlHtml.getcode() is 200:
        soup = BeautifulSoup(urlHtml.read(), 'html.parser')

        for job in soup.findAll('div', 'card js-job'):
            jobTitle = job.find('h2', 'serp-title').text
            href = 'http://www.simplyhired.com' + job.find('a', 'card-link js-job-link').get('href')
            jobCompany = job.find('span', 'serp-company').text.strip()
            jobLocation = job.find('span', 'serp-location').text.strip()
            results = results + '{0}\n{1}  {2}\n{3}\n'.format(jobTitle, jobCompany, jobLocation, href) + '\n'
    else:
        print('Simply Hired Error Code:{0}'.format(urlHtml.getcode()))

    return results

results = ''
           
results = results + indeed_scraper("http://www.indeed.com/jobs?q=software+engineer&l=Longmont,+CO&radius=20&sort=date")
results = results + simply_scraper("http://www.simplyhired.com/search?q=software+engineer&l=longmont%2C+co&fdb=1&sb=dd")

emailSmtp = smtplib.SMTP('smtp.gmail.com', 587)
emailSmtp.starttls()
emailSmtp.login('YOUR EMAIL ADDRESS', 'YOUR EMAIL PASSWORD')

emailSmtp.sendmail('YOUR EMAIL ADDRESS', 'RECEIVING ADDRESS', results)
emailSmtp.quit()
