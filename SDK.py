import sys
sys.path.append('/opt/homebrew/lib/python2.7/site-packages') # Replace this with the place you installed facebookads using pip
sys.path.append('/opt/homebrew/lib/python2.7/site-packages/facebook_business-3.0.0-py2.7.egg-info') # same as above

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount

my_app_id = '1302824299894917'
my_app_secret = 'de61215fbf16df9eb522f9244e770f11'
my_access_token = 'wB1Dw26KJoJVag5DpmNTIGJKsCQ'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token)
my_account = AdAccount('act_{1690817351}')
campaigns = my_account.get_campaigns()
print(campaigns)
