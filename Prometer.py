#!/usr/bin/env python3
from statistics import mean 

def performance_issue(df):
    issue_score = df.assign(issue_score = df['Issue Total'] / df['Issue Total'].mean())
    return issue_score

def performance_pull(df):
    pull_score = df.assign(pull_score = df['PR Total'] / df['PR Total'].mean())
    return pull_score

def performance_commit(df):
    commit_score = df.assign(commit_score = df['Commit Total'] / df['Commit Total'].mean())
    return commit_score


def performance_LOC(df):
    
    loc_score = df.assign(loc_score = df['LOC Total'] / df['LOC Total'].mean())
    return loc_score

def Total(merge1):
    issue = []
    pull = []
    commit = []
    loc = []

    for i in range(len(merge1['User Name'])):
        iss = merge1['Issue Score'][i]
        pll = merge1['PR Score'][i]
        cmm = merge1['Commit Score'][i]
        lc = merge1['LOC Score'][i]
        issue.append(iss)
        pull.append(pll)
        commit.append(cmm)
        loc.append(lc)

    totalState = []
    for j in range(len(issue)):
        result = issue[j] + pull[j] + commit[j] + loc[j]
        totalState.append(result)
        
    return totalState
