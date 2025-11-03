import pandas as pd
import numpy as np

def read_rope_file(filepath):
    
    df = pd.read_csv(filepath)
    df['dx'] = df['x'].diff().fillna(0)
    df['dy'] = df['y'].diff().fillna(0)
    df['dz'] = df['z'].diff().fillna(0)
    df['SegmentLength'] = (df['dx']**2 + df['dy']**2 + df['dz']**2).pow(0.5)
    df['CumulativeLength'] = df['SegmentLength'].cumsum()
    return df

def resample_rope(df, resolution):
    
    length = df['CumulativeLength'].iloc[-1]
    u = np.linspace(0, length, num=resolution)
    x = np.interp(u, df['CumulativeLength'], df['x'])
    y = np.interp(u, df['CumulativeLength'], df['y'])
    z = np.interp(u, df['CumulativeLength'], df['z'])
    result_df = pd.DataFrame({'u': u, 'x': x, 'y': y, 'z': z})
    return result_df