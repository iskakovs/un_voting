import pandas as pd

data = pd.read_excel('/content/sample_data/2014-21.xlsx')

data['vote_numeric'] = data['vote'].apply(lambda x: 1 if x == 'Y' else (0 if x == 'N' else 0.5))

