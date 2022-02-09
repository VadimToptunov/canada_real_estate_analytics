from realtor_scripts import scrape_realtor_ca, zillow_scrape


def gather_rent_data():
    scrape_realtor_ca.run_scraping()
    zillow_scrape.run_zillow_scraping()


if __name__ == '__main__':
    gather_rent_data()
