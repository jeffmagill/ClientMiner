# require 'google/apis/searchconsole_v1'


# google api endpoint appears to be broken as their samples dont work and
# the endpoint is listed as "alpha"

class MobileHammer:
    # @@api_key = "AIzaSyDISZM8zEFtQ0DkS5iXe-tmwfQFSR8_Sis"
    # @@service_url = 'https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run'

    @staticmethod
    def hit(url):
        print(f"Hitting '{url}' with mobile")
        # puts "Getting MobileTest for #{url}"
        #
        # # response = @@service.run_mobile_friendly_test(nil)
        #
        # uri = URI("#{@@service_url}?key=#{@@api_key}&url=#{url}")
        # # res = Net::HTTP.post_form(uri, :url => url, :key => @@api_key)
        #
        #
        # req = Net::HTTP::Post.new(uri)
        # req.set_form_data('url' => url, 'key' => @@api_key,'apikey' => @@api_key,'api_key' => @@api_key)
        #
        # res = Net::HTTP.start(uri.hostname, uri.port, :use_ssl => uri.scheme == 'https') do |http|
        #   http.request(req)
        # end
        #
        #
        # byebug
        # puts res
        # # puts res.body if res.is_a?(Net::HTTPSuccess)
        #
        # return [{
        #     name: "Foo",
        #     value: "Bar"
        #   }]
