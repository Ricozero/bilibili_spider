import requests
from pprint import pprint
from tqdm import tqdm
import json

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

def dump_season_comments(mid):
    results = {}
    basics = get_season_basics(mid)
    results['basics'] = basics
    details = get_sesason_details(basics['result']['media']['season_id'])
    results['details'] = details
    comments = []
    for ep in tqdm(details['result']['episodes']):
        comments.append(get_video_comments(ep['aid']))
    results['comments'] = comments
    with open(str(mid) + '.json', 'w') as f:
        f.write(json.dumps(results))

def length(str):
    # length of a string, chinese characters counted as 2
    str_utf8 = str.encode('utf-8')
    return int((len(str_utf8) + len(str)) / 2)

def process_season_comments(mid):
    try:
        f = open(str(mid) + '.json', 'r')
    except IOError:
        dump_season_comments(mid)
    results = json.loads(f.read())
    f.close()

    f = open(str(mid) + '_comments.txt', 'w', encoding='utf-8')
    # iterate over replies of all episodes
    for i, epr in enumerate(results['comments']):
        title = results['details']['result']['episodes'][i]['long_title']
        s = '%d、%s' % (i + 1, title)
        l = length(s)
        if l % 2 == 1:
            l += 1
            s += ' '
        f.write('╔' + '═' * l + '╗\n')
        f.write('║%s ║\n' % s)
        f.write('╚' + '═' * l + '╝\n\n')
        for reply in epr['data']['replies']:
            uname = reply['member']['uname']
            content = reply['content']['message']
            f.write('[%s]\n%s\n\n' % (uname, content))
        f.write('\n')
    f.close()

process_season_comments(28229010)