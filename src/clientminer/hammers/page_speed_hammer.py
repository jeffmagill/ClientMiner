import requests

# require 'json'
# require 'byebug'
# require 'google/apis/pagespeedonline_v2'


class PageSpeedHammer:
    # @@api_key = "AIzaSyDISZM8zEFtQ0DkS5iXe-tmwfQFSR8_Sis"
    # @@strategy = "desktop"
    # @@service = Google::Apis::PagespeedonlineV2::PagespeedonlineService.new

    @staticmethod
    def hit(url):
        x = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={url}&strategy=mobile'
        r = requests.get(x)
        data = r.json()

        if "error" in data:
            print(f"  Error. Unable to run page speed on {url}")
            return {}
        # print(str(data))
        # print("data:")
        # print(data["lighthouseResult"]["audits"]["time-to-first-byte"]["details"]["overallSavingsMs"])
        # print("property:")
        # print(PageSpeedHammer.property("lighthouseResult.audits.time-to-first-byte.details.overallSavingsMs", data))
        result = {
            "performance-score": PageSpeedHammer.property("lighthouseResult.categories.performance.score", data),
            "performance-score": PageSpeedHammer.property("lighthouseResult.categories.performance.score", data),
            "performance-score": PageSpeedHammer.property("lighthouseResult.categories.performance.score", data),
            "performance-score": PageSpeedHammer.property("lighthouseResult.categories.performance.score", data),
            "performance-score": PageSpeedHammer.property("lighthouseResult.categories.performance.score", data),
            "performance-score": PageSpeedHammer.property("lighthouseResult.categories.performance.score", data),
            "performance-score": PageSpeedHammer.property("lighthouseResult.categories.performance.score", data),
            "performance-score": PageSpeedHammer.property("lighthouseResult.categories.performance.score", data),


            "time-to-first-byte-score": PageSpeedHammer.property("lighthouseResult.audits.time-to-first-byte.score", data),
            "time-to-first-byte-potential-savings": PageSpeedHammer.property("lighthouseResult.audits.time-to-first-byte.details.overallSavingsMs", data),
            "render-blocking-resources-score": PageSpeedHammer.property("lighthouseResult.audits.render-blocking-resources.score", data),
            "render-blocking-resources-potential-savings": PageSpeedHammer.property("lighthouseResult.audits.render-blocking-resources.details.overallSavingsMs", data),
            "uses-optimized-images-score": PageSpeedHammer.property("lighthouseResult.audits.uses-optimized-images.score", data),
            "uses-optimized-images-potential-savings": PageSpeedHammer.property("lighthouseResult.audits.uses-optimized-images.details.overallSavingsMs", data),
            "uses-text-compression-score": PageSpeedHammer.property("lighthouseResult.audits.uses-text-compression.score", data),
            "uses-text-compression-potential-savings": PageSpeedHammer.property("lighthouseResult.audits.uses-text-compression.details.overallSavingsMs", data),
            "interactive-score": PageSpeedHammer.property("lighthouseResult.audits.interactive.score", data),
            "unminified-css-score": PageSpeedHammer.property("lighthouseResult.audits.unminified-css.score", data),
            "unminified-css-potential-savings": PageSpeedHammer.property("lighthouseResult.audits.unminified-css.details.overallSavingsMs", data),
            "bootup-time-score": PageSpeedHammer.property("lighthouseResult.audits.bootup-time.score", data),
            "bootup-time-wasted-time": PageSpeedHammer.property("lighthouseResult.audits.bootup-time.details.summary.wastedMs", data),
        }
        return result
    
    @staticmethod
    def property(qualifier, item):
        names = qualifier.split(".")
        current = item
        for name in names: 
            if name in current: 
                current = current[name]

        if current is item:
            return ""
        else:
            return current
