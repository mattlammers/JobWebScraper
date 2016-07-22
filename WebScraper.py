from bs4 import BeautifulSoup
import urllib

url = "http://www.indeed.com/jobs?q=software+engineer&l=Longmont%2C+CO&jt=fulltime&explvl=entry_level&sort=date"
f = urllib.urlopen(url)

soup = BeautifulSoup(f.read(), 'html.parser')

for job in soup.find_all(True, {'class':' row result'}):
    jobTitle = job.find(True, {'class':'turnstileLink'}).text
    jobCompany = job.find(True, {'class':'company'})
    companyName = jobCompany.find(True, {'itemprop':'name'}).text.strip()
    jobLocation = job.find(True, {'class':'location'})
    location = jobLocation.find(True, {'itemprop':'addressLocality'}).text
    print('{0}\n{1}\t{2}\n'.format(jobTitle, companyName, location))
