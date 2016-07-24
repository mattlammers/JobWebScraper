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
            results = ''.join([results, jobTitle, '\n', companyName, '  ', location, '\n', href, '\n\n'])
    else:
        print('Indeed.com Error Code: ' + urlHtml.getcode())
    
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
            results = ''.join([results, jobTitle, '\n', jobCompany, '  ', jobLocation, '\n', href, '\n\n'])
    else:
        print('Simply Hired Error Code: ' + urlHtml.getcode())

    return results

#Get user input for job user wants to search for and format properly to be inserted into the urls
inputJob = raw_input('Enter job to search for:').strip()
inputJob = inputJob.lower()
inputJob = inputJob.replace(' ', '+')

#Get user input for location user wants to search and parse into array
inputLocation = raw_input('Enter location to search for using the format City, State abbreviation:').split(', ')

#Formatting the urls based on user given search parameters
indeedUrl = ''.join(['http://www.indeed.com/jobs?q=', inputJob, '&l=', inputLocation[0], ',+', inputLocation[1].upper(), '&radius=20&sort=date'])
simplyUrl = ''.join(['http://www.simplyhired.com/search?q=', inputJob, '&l=', inputLocation[0], '%2C+', inputLocation[1], '&mi=25&fdb=1&sb=dd'])

#Start getting results and creating string with results from our BeautifulSoup parsing
results = ''

results = results + indeed_scraper(indeedUrl)
results = results + simply_scraper(simplyUrl)

#Send email to gmail accounts with body containing the results of the search
emailSmtp = smtplib.SMTP('smtp.gmail.com', 587)
emailSmtp.starttls()
emailSmtp.login('YOUR EMAIL ADDRESS', 'EMAIL PASSWORD')

emailSmtp.sendmail('SENDING EMAIL ADDRESS', 'RECEIVING EMAIL ADDRESS', results)
emailSmtp.quit()
