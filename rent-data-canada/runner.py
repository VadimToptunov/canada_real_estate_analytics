from realtor_scripts import rentfast, scrape_realtor_ca, zillow_scrape
from circlemap_generator import circlemap_generator


def scrape_and_generate_map():
    rentfast.scrape_rent_fast()
    scrape_realtor_ca.run_scraping()
    zillow_scrape.run_zillow_scraping()
    circlemap_generator.get_circlemap()


if __name__ == '__main__':
    scrape_and_generate_map()
