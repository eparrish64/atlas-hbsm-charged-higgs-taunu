__all__ = [ "LUMI", "LUMI_UNCERT"]

# - - - - - - - - lumi [pb]
LUMI = {
    "2011": 4523.35,
    "2012": 20274.2,
    "2015": 3316.68,
    "2016": 32784, #>! 2015 + 2016
}
# - - - - - - - - lumi [pb] uncert.
LUMI_UNCERT = {
    "2011": 0.018,
    "2012": 0.028,
    "2015": 0.30,
    "2016": 0.04,
}

def get_lumi_uncert(year):
    return LUMI_UNCERT[year]
