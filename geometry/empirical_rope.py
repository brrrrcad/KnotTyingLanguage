import pandas as pd
import numpy as np

def read_rope_raw(filepath):
    
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
    result_df = pd.DataFrame({'u': u, 'x': x, 'y': y, 'z': z, 'CumulativeLength': u})
    return result_df

def read_rope(filepath, resolution):
    df_raw = read_rope_raw(filepath)
    df = resample_rope(df_raw, resolution)
    return df