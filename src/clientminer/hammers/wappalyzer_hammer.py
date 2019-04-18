
class WappalyzerHammer:
    # @@lib_path = "/Users/Jeff/Sites/Unhinged/ClientMining/Wappalyzer"

    @staticmethod
    def hit(url):
        print(f"Hitting '{url}' with Wappalyzer")
        #docker run --rm wappalyzer/cli https://wappalyzer.com
        #     Dir.chdir(@@lib_path)
        #     value = %x(docker run --rm wappalyzer/cli #{url})
        #     json_val = []
        #     begin
        #       json_val = JSON.parse(value)
        #     rescue Exception
        #       STDERR.puts "Error parsing Wappalyzer JSON response: #{url}"
        #       STDERR.puts "Attempting alternate JSON extraction."
        #
        #       #try to extract some kind of JSON out of response
        #       matches = /([\[\{][\w\W]*[\]\}])/.match(value)
        #       json_val = JSON.parse(matches[0]) if !matches.nil? && matches.length > 0
        #     end
        #
        #     return json_val.map { |x| Hash[x["name"], x["version"].to_s.empty? ? "Yes" : x["version"]]  }.reduce({}, :merge)
        #   end
        # end
        #
        #
        # #
        # # {
        # #    "http://unhingedweb.com":[
        # #       {
        # #          "name":"Google Analytics",
        # #          "confidence":"100",
        # #          "version":"UA",
        # #          "icon":"Google Analytics.svg",
        # #          "website":"http://google.com/analytics",
        # #          "categories":[
        # #             {
        # #                "10":"Analytics"
        # #             }
        # #          ]
        # #       },
        # #       {
        # #          "name":"Google Font API",
        # #          "confidence":"100",
        # #          "version":"",
        # #          "icon":"Google Font API.png",
        # #          "website":"http://google.com/fonts",
        # #          "categories":[
        # #             {
        # #                "17":"Font Scripts"
        # #             }
        # #          ]
        # #       },
        # #       {
        # #          "name":"Modernizr",
        # #          "confidence":"100",
        # #          "version":"",
        # #          "icon":"Modernizr.png",
        # #          "website":"http://www.modernizr.com",
        # #          "categories":[
        # #             {
        # #                "12":"JavaScript Frameworks"
        # #             }
        # #          ]
        # #       },
        # #       {
        # #          "name":"Nginx",
        # #          "confidence":"100",
        # #          "version":"1.12.2",
        # #          "icon":"Nginx.svg",
        # #          "website":"http://nginx.org/en",
        # #          "categories":[
        # #             {
        # #                "22":"Web Servers"
        # #             }
        # #          ]
        # #       },
        # #       {
        # #          "name":"Raphael",
        # #          "confidence":"100",
        # #          "version":"",
        # #          "icon":"Raphael.png",
        # #          "website":"http://raphaeljs.com",
        # #          "categories":[
        # #             {
        # #                "25":"JavaScript Graphics"
        # #             }
        # #          ]
        # #       },
        # #       {
        # #          "name":"Twitter",
        # #          "confidence":"100",
        # #          "version":"",
        # #          "icon":"Twitter.svg",
        # #          "website":"http://twitter.com",
        # #          "categories":[
        # #             {
        # #                "5":"Widgets"
        # #             }
        # #          ]
        # #       },
        # #       {
        # #          "name":"Twitter Emoji (Twemoji)",
        # #          "confidence":"100",
        # #          "version":"",
        # #          "icon":"default.svg",
        # #          "website":"http://twitter.github.io/twemoji/",
        # #          "categories":[
        # #             {
        # #                "25":"JavaScript Graphics"
        # #             }
        # #          ]
        # #       },
        # #       {
        # #          "name":"WordPress",
        # #          "confidence":"100",
        # #          "version":" 4.8.3",
        # #          "icon":"WordPress.svg",
        # #          "website":"http://wordpress.org",
        # #          "categories":[
        # #             {
        # #                "1":"CMS"
        # #             },
        # #             {
        # #                "11":"Blogs"
        # #             }
        # #          ]
        # #       },
        # #       {
        # #          "name":"Yoast SEO",
        # #          "confidence":"100",
        # #          "version":"",
        # #          "icon":"Yoast SEO.png",
        # #          "website":"http://yoast.com",
        # #          "categories":[
        # #             {
        # #                "32":"Marketing Automation"
        # #             }
        # #          ]
        # #       },
        # #       {
        # #          "name":"jQuery",
        # #          "confidence":"100",
        # #          "version":"",
        # #          "icon":"jQuery.svg",
        # #          "website":"http://jquery.com",
        # #          "categories":[
        # #             {
        # #                "12":"JavaScript Frameworks"
        # #             }
        # #          ]
        # #       },
        # #       {
        # #          "name":"PHP",
        # #          "confidence":"0",
        # #          "version":"",
        # #          "icon":"PHP.svg",
        # #          "website":"http://php.net",
        # #          "categories":[
        # #             {
        # #                "27":"Programming Languages"
        # #             }
        # #          ]
        # #       }
        # #    ],
        # #    "http://bundybakingsolutions.com":[
        # #       {
        # #          "name":"Google Analytics",
        # #          "confidence":"100",
        # #          "version":"UA",
        # #          "icon":"Google Analytics.svg",
        # #          "website":"http://google.com/analytics",
        # #          "categories":[
        # #             {
        # #                "10":"Analytics"
        # #             }
        # #          ]
        # #       },
        # #       {
        # #          "name":"Nginx",
        # #          "confidence":"100",
        # #          "version":"",
        # #          "icon":"Nginx.svg",
        # #          "website":"http://nginx.org/en",
        # #          "categories":[
        # #             {
        # #                "22":"Web Servers"
        # #             }
        # #          ]
        # #       },
        # #       {
        # #          "name":"Plesk",
        # #          "confidence":"100",
        # #          "version":"",
        # #          "icon":"Plesk.png",
        # #          "website":"http://plesk.com",
        # #          "categories":[
        # #             {
        # #                "9":"Hosting Panels"
        # #             }
        # #          ]
        # #       },
        # #       {
        # #          "name":"Typekit",
        # #          "confidence":"100",
        # #          "version":"",
        # #          "icon":"Typekit.png",
        # #          "website":"http://typekit.com",
        # #          "categories":[
        # #             {
        # #                "17":"Font Scripts"
        # #             }
        # #          ]
        # #       },
        # #       {
        # #          "name":"WordPress",
        # #          "confidence":"100",
        # #          "version":" 4.8.3",
        # #          "icon":"WordPress.svg",
        # #          "website":"http://wordpress.org",
        # #          "categories":[
        # #             {
        # #                "1":"CMS"
        # #             },
        # #             {
        # #                "11":"Blogs"
        # #             }
        # #          ]
        # #       },
        # #       {
        # #          "name":"PHP",
        # #          "confidence":"0",
        # #          "version":"",
        # #          "icon":"PHP.svg",
        # #          "website":"http://php.net",
        # #          "categories":[
        # #             {
        # #                "27":"Programming Languages"
        # #             }
        # #          ]
        # #       }
        # #    ]
        # # }
