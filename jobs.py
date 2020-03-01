import requests
from bs4 import BeautifulSoup as bs
headers={'accept':'*/*',
         'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}

base_url='https://jobs.tut.by/search/vacancy?area=1002&st=searchVacancy&text=Python+%D1%81%D1%82%D0%B0%D0%B6%D0%B5%D1%80&from=suggest_post'
def tut_parser(base_url,headers):
    jobs=[]
    session = requests.Session()
    request=session.get(base_url,headers=headers)
    if request.status_code==200:
        soup=bs(request.content,'html.parser')

        divs=soup.find_all('div',{'data-qa':'vacancy-serp__vacancy'})
        for div in divs:
            title=div.find('a',{'class':'bloko-link'}).text
            href=div.find('a',{'class':'bloko-link'})['href']
            company=div.find('a',{'data-qa':'vacancy-serp__vacancy-employer'}).text
            text1=div.find('div',{'data-qa':'vacancy-serp__vacancy_snippet_responsibility'}).text
            text2 = div.find('div', {'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
            content=text1 + ' ' + text2
            jobs.append({
                'title': title,
                'href': href,
                'company': company,
                'content': content
            })
        print(jobs)

    else:
        print('ERROR')
tut_parser(base_url,headers)








