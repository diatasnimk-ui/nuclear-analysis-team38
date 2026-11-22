"""phase1_baseline.py - LEAD ONLY, run once.
Reads raw/*.xlsx and writes phase1_outputs/phase1_country_baseline.csv and fleet_ts.csv."""
import sys
import pandas as pd
from pathlib import Path

PROJECT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/content/drive/MyDrive/nuclear_isotope_project')
RAW = PROJECT / 'raw'
OUT = PROJECT / 'phase1_outputs'
OUT.mkdir(exist_ok=True)

FOCUS = ['China', 'United States of America', 'Korea, Republic of',
         'Russian Federation', 'France']

# --- Country baseline: data (4) = fleet totals, data (10) = first construction / grid dates
a = pd.read_excel(RAW / 'data (4).xlsx')
a = a[a['Country'].isin(FOCUS)].copy()
b = pd.read_excel(RAW / 'data (10).xlsx')
b = b[b['Country'].isin(FOCUS)].copy()

a['Capacity_GW'] = a['Operated capacity MW(e)'] / 1000
a['Lifetime_TWh'] = a['Lifetime generation GWh'] / 1000
a['Avg_age_yrs'] = a['Age'] / a['Number of reactors']          # Age = summed reactor-years
a['Productivity_TWh_per_GW'] = a['Lifetime_TWh'] / a['Capacity_GW']

cd = pd.to_datetime(b['Construction Date'])
gd = pd.to_datetime(b['Grid Date'])
b['First_construction_year'] = cd.dt.year
b['First_grid_year'] = gd.dt.year
b['First_unit_lead_time_yrs'] = (gd - cd).dt.days / 365.25     # earliest unit per country only

baseline = (a[['Country', 'Number of reactors', 'Capacity_GW', 'Lifetime_TWh',
               'Avg_age_yrs', 'Productivity_TWh_per_GW']]
            .merge(b[['Country', 'First_construction_year', 'First_grid_year',
                      'First_unit_lead_time_yrs']], on='Country')
            .sort_values('Country').round(2))
baseline['Number of reactors'] = baseline['Number of reactors'].astype(int)
assert len(baseline) == 5, f'expected 5 countries, got {len(baseline)}'

# --- Fleet time series: data (1)
c = pd.read_excel(RAW / 'data (1).xlsx', header=None, skiprows=3,
                  names=['Year', 'Status', 'Value'])
c = c[pd.to_numeric(c['Year'], errors='coerce').notna()].copy()
c['Year'] = c['Year'].astype(int)
t = (c.pivot_table(index='Year', columns='Status', values='Value', aggfunc='sum')
       .fillna(0).sort_index())
fleet_ts = pd.DataFrame({'Operational_GW': t['Operational'] / 1000,
                         'Suspended_GW': t['Suspended operation'] / 1000}).round(3)

baseline.to_csv(OUT / 'phase1_country_baseline.csv', index=False)
fleet_ts.to_csv(OUT / 'fleet_ts.csv')
print(baseline.to_string(index=False))
print('fleet_ts rows:', len(fleet_ts), '| years', fleet_ts.index.min(), '-', fleet_ts.index.max())
