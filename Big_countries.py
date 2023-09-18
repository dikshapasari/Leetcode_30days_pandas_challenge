import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    
    if world.empty or len(world)== 1:
        return world[['name','area','population']]
    
    big_countries= world[(world['area']> 3000000) | (world['population']>= 25000000)]
    return big_countries[['name', 'population','area']]
