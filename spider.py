import requests
from pprint import pprint

dn = 'https://api.bilibili.com' # domain name

def get_season_basics(mid):
    r = requests.get(dn + '/pgc/review/user?media_id=%d' % mid)
    return r.json()

def get_sesason_details(id, type='sid'):
    if type == 'sid':
        r = requests.get(dn + '/pgc/view/web/season?season_id=%d' % id)
    elif type == 'eid':
        r = requests.get(dn + '/pgc/view/web/season?ep_id=%d' % id)
    else:
        raise ValueError('Wrong type argument.')
    return r.json()

def get_video_comments(oid, sort='hot'):
    if sort == 'hot':
        r = requests.get(dn + '/x/v2/reply/main?type=1&oid=%d' % oid)
    elif sort == 'time':
        r = requests.get(dn + '/x/v2/reply?type=1&oid=%d' % oid)
    else:
        raise ValueError('Wrong sort argument.')
    return r.json()

basics = get_season_basics(28229010)
pprint(basics)
details = get_sesason_details(basics['result']['media']['season_id'])
#pprint(details)
scom = [] # season comments
for ep in details['result']['episodes']:
    scom.append(get_video_comments(ep['aid']))
#pprint(scom)