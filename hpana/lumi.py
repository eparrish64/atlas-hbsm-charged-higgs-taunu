__all__ = [ "LUMI", "LUMI_UNCERT"]

# - - - - - - - - lumi [pb]
LUMI = {
    "2011": 4523.35,
    "2012": 20274.2,
    "2015": 3316.68,
    "2016": 32784,
    "2017": 44307.40,
    "2018": 58450.10, 
}
# - - - - - - - - lumi uncert %.
LUMI_UNCERT = {
    "2011": 0.018,
    "2012": 0.028,
    "2015": 0.021,
    "2016": 0.022,
    "2017": 0.024,
    "2018": 0.020,
}

def get_lumi_uncert(year):
    return LUMI_UNCERT[year]
