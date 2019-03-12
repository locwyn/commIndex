import quandl
from credentials import *

quandl.ApiConfig.api_key = quandlKey

data = quandl.get("LME/PR_CU", start_date="2019-03-01", 
       end_date="2019-03-12", returns="numpy")

print data

