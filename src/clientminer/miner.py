
class Miner:

    def __init__(self):
        self.hammers = []

    def add_hammer(self, hammer):
        if hasattr(hammer, "hit"):
            self.hammers.append(hammer)
        else :
            raise AttributeError("Object cannot be used as a hammer.")

    def hit(self, urls):
        results = []
        for url in urls:
            single_result = { "url": url }
            for hammer in self.hammers:
                gem = hammer.hit(url)
                if gem is not None:
                    # print("Found gem:")
                    # print(gem)
                    single_result.update(gem)
                else:
                    # print("No gem.")
                    pass
            results.append(single_result)
        return results
#   @urls = []
#   def initialize(args)
#     @urls = process_args(args)
#   end
#
#   def run
#     results = process_urls(@urls)
#     puts render_results(results)
#   end
#
#   def process_urls(urls)
#       #process the urls
#       results = {}
#       @urls.each do |url|
#         puts "Loading: #{url}"
#         results[url] ||= {}
#         # pp MobileTestHammer.hit(url)
#         # return null
#         results[url] = results[url].merge(WappalyzerHammer.hit(url))
#         results[url] = results[url].merge(PageSpeedHammer.hit(url))
#         results[url] = results[url].merge(WgetHammer.hit(url))
#         # results[url] = results[url].merge(MobileTestHammer.hit(url))
#
#         # results[url] += PageSpeedHammer.hit(url)
#         # results[url] += WgetHammer.hit(url)
#         # results[url] += MobileTestHammer.hit(url)
#       end
#       return results
#   end
#
#
#   def process_args(args)
#     urls = []
#     args.each do |arg|
#       if File.exists? arg
#         #load csv and extract URLs
#         CSV.foreach(arg) do |row|
#           urls << normalize_url(row[0])
#         end
#       else
#         urls << normalize_url(arg)
#       end
#     end
#     return urls
#   end
#
#   def normalize_url(value)
#     if value != nil && !value.start_with?("http://") && !value.start_with?("https://")
#       #add protocol, assume http
#       return "http://#{value}"
#     else
#       return value
#     end
#   end
#
#
# end
