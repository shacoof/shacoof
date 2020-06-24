# https://jira.readthedocs.io/en/master/examples.html#
from jira import JIRA 

def search_JIRA(jql,fields):
    jira = JIRA(basic_auth=('scohenofir', 'JennyXO123!'),server="https://jira.devfactory.com/")
    issueList = [(i.key, i.fields.status.name,i.fields.issuetype.name) 
        for i in jira.search_issues(jql, maxResults=1000,fields=fields)]
    return issueList

def main():
    #filter=124619 sharon's overdue releases 
    fields = 'key,status,issuetype'
    list = search_JIRA('filter=124619',fields)
    print(fields)
    print('\n')
    print('\n'.join('{}: {}'.format(*k) for k in enumerate(list)))

if __name__ == '__main__':
    main()





