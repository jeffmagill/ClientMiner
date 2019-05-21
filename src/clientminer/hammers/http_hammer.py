import scrapy
import pdb; 
class HTTPHammer:

    def __init(self):
        pass

    @staticmethod
    def hit(url):
        print (f"Hitting '{url}' with HTTP")
        yield scrapy.Request(url=url, callback=HTTPHammer.parse)

    @staticmethod
    def parse(response):
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
            # f.write(response.body)
        # self.log('Saved file %s' % filename)
        text = response.body

        print (f"This is what we captured: {text}")