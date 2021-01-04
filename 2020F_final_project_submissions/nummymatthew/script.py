import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('injury_data.tsv', sep='\t')
df['2020/21 proj'] = df['2020/21'] * 3

COLS = ["2016/17", "2017/18", "2018/19",  "2019/20",  "2020/21"]
PRIOR_YEARS = ["2016/17", "2017/18", "2018/19",  "2019/20"]

# Injuries this year
res = df[['Country', 'Club', '2020/21']].loc[(df['Type'] == 'Injuries')].sort_values(by='2020/21')
fig = res.set_index('Club')['2020/21'].plot(kind='bar', figsize=(12,8), ylabel='Injuries 2020/21').get_figure()
fig.savefig('injuries_2020_21.pdf', bbox_inches='tight', pad_inches=2)

# Injuries vs time
def vs_time_plot(df, inj_type, clubs=None, countries=None):
    clubs = clubs if clubs else []
    countries = countries if countries else []

    if clubs:
        fltr = df['Club'].isin(clubs)
    elif countries:
        fltr = df['Country'].isin(countries)
    else:
        fltr = ~df.index.isna()
    
    res = df[
        ['Club', "2016/17", "2017/18", "2018/19",  "2019/20",  "2020/21"]
    ].loc[
        (df['Type'] == inj_type) & fltr
    ].set_index('Club')
    res.T.plot(figsize=(12,8), ylabel=f'{inj_type} vs Time')

fig = vs_time_plot(df, 'Injuries', clubs=['FC Bayern', 'Juventus FC', 'Real Madrid']).get_figure()
fig.savefig('injuries_vs_time_clubs.pdf', bbox_inches='tight', pad_inches=2)

fig = vs_time_plot(df, 'Repeat', countries=['England']).get_figure()
fig.savefig('england_repeat_injuries_vs_time.pdf', bbox_inches='tight', pad_inches=2)


# Most and Least of
def who_has_the_most_of(df, inj_type, year=None):
    if year:
        res = df[['Club', year]].loc[(df['Type'] == inj_type)]
        return res.iloc[res[year].argmax()]
    else:
        res = df[
            ['Club'] + COLS
        ].loc[(df['Type'] == inj_type)]
        rr = pd.concat([res.set_index('Club').idxmax(), res.set_index('Club').max()], axis=1)
        return rr[0].loc[rr[1].idxmax()], rr[1].max(), rr[1].idxmax()
    
def who_has_the_least_of(df, inj_type, year=None):
    if year:
        res = df[['Club', year]].loc[(df['Type'] == inj_type)]
        return res.iloc[res[year].argmin()]
    else:
        res = df[
            ['Club'] + COLS
        ].loc[(df['Type'] == inj_type)]
        rr = pd.concat([res.set_index('Club').idxmax(), res.set_index('Club').min()], axis=1)
        return rr[0].loc[rr[1].idxmin()], rr[1].min(), rr[1].idxmin()

print(who_has_the_most_of(df, 'Concurrent', year='2019/20'))
print(who_has_the_most_of(df, 'Concurrent', year=None))
print(who_has_the_least_of(df, 'Injuries', year='2019/20'))

def compare_countries(df, inj_type):
    res = df.loc[(df['Type'] == inj_type)].groupby('Country')[COLS + ['2020/21 proj']].mean()
    res.plot(kind='bar', ylabel=f'Average {inj_type}', figsize=(12,8))
    
fig = compare_countries(df, 'Injuries').get_figure()
fig.savefig('country_comparison.pdf', bbox_inches='tight', pad_inches=2)
