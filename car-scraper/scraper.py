# Importing in each cell because of the kernel restarts.
import scrapy
import logging
from scrapy.crawler import CrawlerProcess


class CarGurusScraper(scrapy.Spider):
    # Naming the spider is important if you are running more than one spider of
    # this class simultaneously.
    name = "CarGurus"

    # URL(s) to start with.
    start_urls = [
        "https://www.cargurus.com/Cars/inventorylisting/viewDetailsFilterViewInventoryListing.action?sourceContext=carGurusHomePageModel&newSearchFromOverviewPage=true&inventorySearchWidgetType=AUTO&entitySelectingHelper.selectedEntity=d2230&entitySelectingHelper.selectedEntity2=&zip=02563&distance=50000&searchChanged=true&modelChanged=false&filtersModified=true",
    ]

    # Use XPath to parse the response we get.
    def parse(self, response):
        # Iterate over every car item on the page to get info on it
        xpath_string = "//main/div[@id='listingResultsContentBody']/div[@id='wideDealFinderVersion']/div[@id='listingsContent']/div[@class='cg-listingResults-wrap']/div[@id='listingsOverviewContainer']/div[@id='mainSearchResultsContainer']/div[@id='searchResultsContainer2']/div/div[@id='listingsDivParent']/div[@id='listingsDiv']/div[contains(@id, 'listing_')]"
        import pudb; pudb.set_trace()
        for listing in response.xpath(xpath_string):
            print("HI!")
            print(listing)
            #             //main/div[@id='listingResultsContentBody']/div[@id='wideDealFinderVersion']/div[@id='listingsContent']/div[@class='cg-listingResults-wrap']/div[@id='listingsOverviewContainer']/div[@id='mainSearchResultsContainer']/div[@id='searchResultsContainer2']/div/div[@id='listingsDivParent']/div[@id='listingsDiv']/div[contains(@id, 'listing_')]
            #             //main/div[@id='listingResultsContentBody']/div[@id='wideDealFinderVersion']/div[@id='listingsContent']/div[@class='cg-listingResults-wrap']/div[@id='listingsOverviewContainer']/div[@id='mainSearchResultsContainer']/div[@id='searchResultsContainer2']/div/div[@id='listingsDivParent']/div[@id='listingsDiv']
            # //main/div[@id='listingResultsContentBody']/div[@id='wideDealFinderVersion']/div[@id='listingsContent']/div[@class='cg-listingResults-wrap']/div[@id='listingsOverviewContainer']/div[@id='mainSearchResultsContainer']

            # # Yield a dictionary with the values we want.
            # yield {
            #     # This is the code to choose what we want to extract
            #     # You can modify this with other Xpath expressions to extract other information from the site
            #     'name': car.xpath('header/h2/a/@title').extract_first(),
            #     'date': car.xpath('header/section/span[@class="entry-date"]/text()').extract_first(),
            #     'text': car.xpath('section[@class="entry-content"]/p/text()').extract(),
            #     'tags': car.xpath('*/span[@class="tag-links"]/a/text()').extract()
            # }

# Tell the script how to run the crawler by passing in settings.
process = CrawlerProcess({
    'FEED_FORMAT': 'json',         # Store data in JSON format.
    'FEED_URI': 'cars.json',  # Name our storage file.
    'LOG_ENABLED': True           # Turn off logging for now.
})

# Start the crawler with our spider.
process.crawl(CarGurusScraper)
process.start()
print('Scraped!')
