from realtor_ca import scrape_realtor_ca
from rent_fast import rentfast
from rent_fast import heatmap
from zillow import zillow_scrape


def scrape_and_generate_map():
    rentfast.scrape_rent_fast()
    scrape_realtor_ca.run_scraping()
    zillow_scrape.run_zillow_scraping()
    heatmap.get_heatmap()

if __name__ == '__main__':
    scrape_and_generate_map()