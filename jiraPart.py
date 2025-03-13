import json
from os.path import join
from jira import JIRA


class GatherJiraData:
    def __init__(self, jira_url, jira_query_symbol, project_name):
        self.jira_url = jira_url
        self.jira_query_symbol = jira_query_symbol
        self.project_name = project_name
        self.block_size = 100

        self.project_path = join("projects", project_name)
        self.data_path = join(self.project_path, "data")

    def gather(self):

        jira_conn = JIRA(self.jira_url)

        block_size = self.block_size
        block_num = 0
        sql_req = "project = " + self.jira_query_symbol + " and type = bug and (status = RESOLVED or status = closed)"
        #and resolution  = Fixed
        while True:  # while true
            print(block_num)
            start_idx = block_num * block_size
            if block_num == 0:
                issues = jira_conn.search_issues(sql_req, startAt=start_idx, maxResults=block_size)
            else:
                more_issue = jira_conn.search_issues(sql_req, startAt=start_idx, maxResults=block_size)
                if len(more_issue) > 0:
                    for x in more_issue:
                        issues.append(x)
                else:
                    break
            if len(issues) == 0:
                # Retrieve issues until there are no more to come
                break
            block_num += 1

        issues_dict = {'issues': []}

        for issue in issues:
            if (issue.fields.versions == None or issue.fields.versions == []  or  "Nightly Build" == issue.fields.versions) \
                    and (issue.fields.fixVersions == None or issue.fields.fixVersions == []):

                continue
            new_issue = {
                'issue_id': issue.key, 'project': issue.fields.project.name, 'title': issue.fields.summary,
                'type': issue.fields.issuetype.name, 'description': issue.fields.description,'resolved': issue.fields.resolutiondate.split('T')[0],
                'versions': [i.name for i in issue.fields.versions],
                'fixVersions': [i.name for i in issue.fields.fixVersions]}

            issues_dict['issues'].append(new_issue)



        with open(join(self.data_path, "issues.txt"), 'w') as outfile:
            json.dump(issues_dict, outfile, indent=4)


if __name__ == "__main__":
    jira_url = 'http://issues.apache.org/jira'
    #jira_url = "https://jira.spring.io"
    #jira_url = "https://issues.redhat.com"
    jira_query_symbol = 'CODEC'
    project_name = "Codec"
    GatherJiraData(jira_url, jira_query_symbol, project_name).gather()
