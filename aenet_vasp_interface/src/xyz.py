with open('OUTCAR0', 'r') as f1:
    lines=f1.readlines()


def judge_file():
    TorF=False
    for x in lines:
        if 'General timing and accounting informations for this job:' in x:
            TorF=True
    return TorF

print(judge_file())
