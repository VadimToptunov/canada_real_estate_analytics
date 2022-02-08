from realtor_scripts import scrape_realtor_ca, zillow_scrape
from map_generator import map_generator


def scrape_and_generate_map():
    scrape_realtor_ca.run_scraping()
    zillow_scrape.run_zillow_scraping()
    map_generator.get_map()


if __name__ == '__main__':
    scrape_and_generate_map()
