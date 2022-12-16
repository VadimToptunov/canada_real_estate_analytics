import asyncio

from realtor_scripts import scrape_realtor_ca, zillow_scrape


async def gather_rent_data():
    scrape_realtor_ca.run_scraping()
    await zillow_scrape.run_zillow_scraping()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(gather_rent_data())
