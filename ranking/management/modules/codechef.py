#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import json
import traceback
import tqdm
from pprint import pprint

from common import REQ, LOG
from common import BaseModule
from excepts import ExceptionParseStandings

import conf


class Statistic(BaseModule):
    API_CONTEST_URL_FORMAT_ = 'https://www.codechef.com/api/contests/{key}'
    API_RANKING_URL_FORMAT_ = 'https://www.codechef.com/api/rankings/{key}?sortBy=rank&order=asc&page={page}&itemsPerPage={per_page}'  # noqa

    def __init__(self, **kwargs):
        super(Statistic, self).__init__(**kwargs)
        self._username = conf.CODECHEF_USERNAME
        self._password = conf.CODECHEF_PASSWORD

    def get_standings(self, users=None):
        REQ.get('https://www.codechef.com/')

        try:
            form = REQ.form()
            form['post'].update({
                'name': self._username,
                'pass': self._password,
            })
            page = REQ.get(form['url'], post=form['post'])

            form = REQ.form()
            if form['url'] == '/session/limit':
                for field in form['unchecked'][:-1]:
                    form['post'][field['name']] = field['value'].encode('utf8')
                page = REQ.get(form['url'], post=form['post'])
        except Exception:
            pass

        url = self.API_CONTEST_URL_FORMAT_.format(**self.__dict__)
        page = REQ.get(url)
        data = json.loads(page)
        if data['status'] != 'success':
            raise ExceptionParseStandings(json.dumps(data))
        if 'child_contests' in data:
            contest_infos = {
                d['contest_code']: {'division': k}
                for k, d in data['child_contests'].items()
            }
        else:
            contest_infos = {self.key: {}}

        result = {}

        problems_info = dict() if len(contest_infos) > 1 else list()

        for key, contest_info in contest_infos.items():
            n_page = 0
            per_page = 150
            n_total_page = None
            pbar = None
            contest_type = None
            while n_total_page is None or n_page < n_total_page:
                n_page += 1
                time.sleep(2)
                url = self.API_RANKING_URL_FORMAT_.format(key=key, page=n_page, per_page=per_page)

                if users is not None:
                    urls = [f'{url}&search={user}' for user in users]
                else:
                    urls = [url]

                for url in urls:
                    delay = 10
                    for _ in range(10):
                        try:
                            page = REQ.get(url)
                            data = json.loads(page)
                            break
                        except Exception:
                            traceback.print_exc()
                            delay = min(300, delay * 2)
                            sys.stdout.write(f'Sleep {delay}... ')
                            sys.stdout.flush()
                            time.sleep(delay)
                            sys.stdout.write('Done\n')
                    else:
                        raise ExceptionParseStandings(f'Failed getting {n_page} by url {url}')

                    if 'status' in data and data['status'] != 'success':
                        raise ExceptionParseStandings(json.dumps(data))

                    if n_total_page is None:
                        for p in data['problems']:
                            d = problems_info
                            if 'division' in contest_info:
                                d = d.setdefault('division', {})
                                d = d.setdefault(contest_info['division'], [])
                            d.append({
                                'short': p['code'],
                                'name': p['name'],
                            })
                        n_total_page = data['availablePages']
                        pbar = tqdm.tqdm(total=n_total_page * len(urls))
                        contest_type = data['contest_info'].get('type')

                    unscored_problems = data['contest_info']['unscored_problems']

                    for d in data['list']:
                        handle = d.pop('user_handle')
                        d.pop('html_handle', None)
                        if d['score'] < 1e-9:
                            LOG.warning(f'Skip handle = {handle}: {d}')
                            continue
                        row = result.setdefault(handle, {})

                        row['member'] = handle
                        row['place'] = d.pop('rank')
                        row['solving'] = d.pop('score')

                        problems = row.setdefault('problems', {})
                        solved, upsolved = 0, 0
                        problems_status = d.pop('problems_status')
                        if problems_status:
                            for k, v in problems_status.items():
                                t = 'upsolving' if k in unscored_problems else 'result'
                                v[t] = v.pop('score')
                                solved += 1 if v.get('result', 0) > 0 else 0
                                upsolved += 1 if v.get('upsolving', 0) > 0 else 0
                                row['solved'] = {'solving': solved, 'upsolving': upsolved}

                                if contest_type == '1' and 'penalty' in v:
                                    penalty = v.pop('penalty')
                                    if v[t] > 0:
                                        v[t] = f'+{"" if penalty == 0 else penalty}'
                                    else:
                                        v[t] = f'-{penalty}'

                                problems[k] = v

                        row.update(d)
                        row.update(contest_info)
                    pbar.set_description(f'key={key} url={url}')
                    pbar.update()
            if pbar is not None:
                pbar.close()

        standings = {
            'result': result,
            'url': self.url,
            'problems': problems_info,
        }
        return standings


if __name__ == "__main__":
    statictic = Statistic(
        name='August Challenge 2019',
        url='https://www.codechef.com/AUG19?utm_source=contest_listing&utm_medium=link&utm_campaign=AUG19',
        key='AUG19',
        standings_url=None,
    )
    pprint(statictic.get_result('luma'))
    statictic = Statistic(
        url='https://www.codechef.com/COOK109?utm_source=contest_listing&utm_medium=link&utm_campaign=COOK109',
        key='COOK109',
        standings_url=None,
    )
    pprint(statictic.get_result('uwi'))
    # statictic = Statistic(
    #     name='February Cook-Off 2015',
    #     url='https://www.codechef.com/COOK55?utm_source=contest_listing&utm_medium=link&utm_campaign=COOK55',
    #     key='COOK55',
    #     standings_url=None,
    # )
    # pprint(statictic.get_result('aropan', 'mateusz95', 'ridowan007'))
