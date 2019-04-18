# require 'json'
# require 'byebug'
# require 'google/apis/pagespeedonline_v2'


class PageSpeedHammer:
    # @@api_key = "AIzaSyDISZM8zEFtQ0DkS5iXe-tmwfQFSR8_Sis"
    # @@strategy = "desktop"
    # @@service = Google::Apis::PagespeedonlineV2::PagespeedonlineService.new

    @staticmethod
    def hit(url):
        print(f"Hitting '{url}' with Page Speed")
        # run_pagespeed(url,
        #               filter_third_party_resources: nil,
        #               locale: nil,
        #               rule: nil,
        #               screenshot: nil,
        #               strategy: nil,
        #               fields: nil,
        #               quota_user: nil,
        #               user_ip: nil,
        #               options: nil,
        #               &block)
        #
        #     response = @@service.run_pagespeed(url)
        #
        #     # puts "page speed response: "
        #     # puts response
        #     # puts "---"
        #     data = {}
        #     data["Page Speed Score"] = response.rule_groups["SPEED"].score
        #     data["Page Size"] = response.page_stats.total_request_bytes
        #     data["Resource Count"] = response.page_stats.number_resources
        #     return data
        #     # return [{
        #     #     name: "Page Speed Score",
        #     #     value: response.rule_groups["SPEED"].score
        #     #   },
        #     #   {
        #     #       name: "Page Size",
        #     #       value: response.page_stats.total_request_bytes
        #     #   },
        #     #   {
        #     #       name: "Resource Count",
        #     #       value: response.page_stats.number_resources
        #     #   }]
        #   end
        # end
        #
        #
        # # API response
        # #
        # # {
        # #  "kind": "pagespeedonline#result",
        # #  "id": "http://unhingedweb.com/",
        # #  "responseCode": 200,
        # #  "title": "Home - Unhinged Web Studio » Unhinged Web Studio",
        # #  "ruleGroups": {
        # #   "SPEED": {
        # #    "score": 81
        # #   }
        # #  },
        # #  "pageStats": {
        # #   "numberResources": 45,
        # #   "numberHosts": 7,
        # #   "totalRequestBytes": "4868",
        # #   "numberStaticResources": 32,
        # #   "htmlResponseBytes": "62324",
        # #   "cssResponseBytes": "210784",
        # #   "imageResponseBytes": "70942",
        # #   "javascriptResponseBytes": "615806",
        # #   "otherResponseBytes": "186498",
        # #   "numberJsResources": 15,
        # #   "numberCssResources": 10
        # #  },
        # #  "formattedResults": {
        # #   "locale": "en_US",
        # #   "ruleResults": {
        # #    "AvoidLandingPageRedirects": {
        # #     "localizedRuleName": "Avoid landing page redirects",
        # #     "ruleImpact": 0,
        # #     "groups": [
        # #      "SPEED"
        # #     ],
        # #     "summary": {
        # #      "format": "Your page has no redirects. Learn more about {{BEGIN_LINK}}avoiding landing page redirects{{END_LINK}}.",
        # #      "args": [
        # #       {
        # #        "type": "HYPERLINK",
        # #        "key": "LINK",
        # #        "value": "https://developers.google.com/speed/docs/insights/AvoidRedirects"
        # #       }
        # #      ]
        # #     }
        # #    },
        # #    "EnableGzipCompression": {
        # #     "localizedRuleName": "Enable compression",
        # #     "ruleImpact": 0.07640000000000001,
        # #     "groups": [
        # #      "SPEED"
        # #     ],
        # #     "summary": {
        # #      "format": "Compressing resources with gzip or deflate can reduce the number of bytes sent over the network."
        # #     },
        # #     "urlBlocks": [
        # #      {
        # #       "header": {
        # #        "format": "{{BEGIN_LINK}}Enable compression{{END_LINK}} for the following resources to reduce their transfer size by {{SIZE_IN_BYTES}} ({{PERCENTAGE}} reduction).",
        # #        "args": [
        # #         {
        # #          "type": "HYPERLINK",
        # #          "key": "LINK",
        # #          "value": "https://developers.google.com/speed/docs/insights/EnableCompression"
        # #         },
        # #         {
        # #          "type": "BYTES",
        # #          "key": "SIZE_IN_BYTES",
        # #          "value": "764B"
        # #         },
        # #         {
        # #          "type": "PERCENTAGE",
        # #          "key": "PERCENTAGE",
        # #          "value": "51%"
        # #         }
        # #        ]
        # #       },
        # #       "urls": [
        # #        {
        # #         "result": {
        # #          "format": "Compressing {{URL}} could save {{SIZE_IN_BYTES}} ({{PERCENTAGE}} reduction).",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://widgets.twimg.com/j/2/widget.js?ver=4.8.3"
        # #           },
        # #           {
        # #            "type": "BYTES",
        # #            "key": "SIZE_IN_BYTES",
        # #            "value": "764B"
        # #           },
        # #           {
        # #            "type": "PERCENTAGE",
        # #            "key": "PERCENTAGE",
        # #            "value": "51%"
        # #           }
        # #          ]
        # #         }
        # #        }
        # #       ]
        # #      }
        # #     ]
        # #    },
        # #    "LeverageBrowserCaching": {
        # #     "localizedRuleName": "Leverage browser caching",
        # #     "ruleImpact": 1.5555555555555556,
        # #     "groups": [
        # #      "SPEED"
        # #     ],
        # #     "summary": {
        # #      "format": "Setting an expiry date or a maximum age in the HTTP headers for static resources instructs the browser to load previously downloaded resources from local disk rather than over the network."
        # #     },
        # #     "urlBlocks": [
        # #      {
        # #       "header": {
        # #        "format": "{{BEGIN_LINK}}Leverage browser caching{{END_LINK}} for the following cacheable resources:",
        # #        "args": [
        # #         {
        # #          "type": "HYPERLINK",
        # #          "key": "LINK",
        # #          "value": "https://developers.google.com/speed/docs/insights/LeverageBrowserCaching"
        # #         }
        # #        ]
        # #       },
        # #       "urls": [
        # #        {
        # #         "result": {
        # #          "format": "{{URL}} ({{LIFETIME}})",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "https://syndication.twitter.com/settings"
        # #           },
        # #           {
        # #            "type": "DURATION",
        # #            "key": "LIFETIME",
        # #            "value": "10 minutes"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}} ({{LIFETIME}})",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "https://platform.twitter.com/widgets.js"
        # #           },
        # #           {
        # #            "type": "DURATION",
        # #            "key": "LIFETIME",
        # #            "value": "30 minutes"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}} ({{LIFETIME}})",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://www.google-analytics.com/analytics.js"
        # #           },
        # #           {
        # #            "type": "DURATION",
        # #            "key": "LIFETIME",
        # #            "value": "2 hours"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}} ({{LIFETIME}})",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://widgets.twimg.com/j/2/widget.js?ver=4.8.3"
        # #           },
        # #           {
        # #            "type": "DURATION",
        # #            "key": "LIFETIME",
        # #            "value": "8 hours"
        # #           }
        # #          ]
        # #         }
        # #        }
        # #       ]
        # #      }
        # #     ]
        # #    },
        # #    "MainResourceServerResponseTime": {
        # #     "localizedRuleName": "Reduce server response time",
        # #     "ruleImpact": 9.57,
        # #     "groups": [
        # #      "SPEED"
        # #     ],
        # #     "urlBlocks": [
        # #      {
        # #       "header": {
        # #        "format": "In our test, your server responded in {{RESPONSE_TIME}}. There are many factors that can slow down your server response time. {{BEGIN_LINK}}Please read our recommendations{{END_LINK}} to learn how you can monitor and measure where your server is spending the most time.",
        # #        "args": [
        # #         {
        # #          "type": "DURATION",
        # #          "key": "RESPONSE_TIME",
        # #          "value": "1.2 seconds"
        # #         },
        # #         {
        # #          "type": "HYPERLINK",
        # #          "key": "LINK",
        # #          "value": "https://developers.google.com/speed/docs/insights/Server"
        # #         }
        # #        ]
        # #       }
        # #      }
        # #     ]
        # #    },
        # #    "MinifyCss": {
        # #     "localizedRuleName": "Minify CSS",
        # #     "ruleImpact": 0.5611,
        # #     "groups": [
        # #      "SPEED"
        # #     ],
        # #     "summary": {
        # #      "format": "Compacting CSS code can save many bytes of data and speed up download and parse times."
        # #     },
        # #     "urlBlocks": [
        # #      {
        # #       "header": {
        # #        "format": "{{BEGIN_LINK}}Minify CSS{{END_LINK}} for the following resources to reduce their size by {{SIZE_IN_BYTES}} ({{PERCENTAGE}} reduction).",
        # #        "args": [
        # #         {
        # #          "type": "HYPERLINK",
        # #          "key": "LINK",
        # #          "value": "https://developers.google.com/speed/docs/insights/MinifyResources"
        # #         },
        # #         {
        # #          "type": "BYTES",
        # #          "key": "SIZE_IN_BYTES",
        # #          "value": "4.7KiB"
        # #         },
        # #         {
        # #          "type": "PERCENTAGE",
        # #          "key": "PERCENTAGE",
        # #          "value": "21%"
        # #         }
        # #        ]
        # #       },
        # #       "urls": [
        # #        {
        # #         "result": {
        # #          "format": "Minifying {{URL}} could save {{SIZE_IN_BYTES}} ({{PERCENTAGE}} reduction) after compression.",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/themes/gentle/css/theme.css?ver=4.8.3"
        # #           },
        # #           {
        # #            "type": "BYTES",
        # #            "key": "SIZE_IN_BYTES",
        # #            "value": "2.8KiB"
        # #           },
        # #           {
        # #            "type": "PERCENTAGE",
        # #            "key": "PERCENTAGE",
        # #            "value": "23%"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "Minifying {{URL}} could save {{SIZE_IN_BYTES}} ({{PERCENTAGE}} reduction) after compression.",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/themes/gentle/css/style.css?ver=4.8.3"
        # #           },
        # #           {
        # #            "type": "BYTES",
        # #            "key": "SIZE_IN_BYTES",
        # #            "value": "1.9KiB"
        # #           },
        # #           {
        # #            "type": "PERCENTAGE",
        # #            "key": "PERCENTAGE",
        # #            "value": "19%"
        # #           }
        # #          ]
        # #         }
        # #        }
        # #       ]
        # #      }
        # #     ]
        # #    },
        # #    "MinifyHTML": {
        # #     "localizedRuleName": "Minify HTML",
        # #     "ruleImpact": 0.0671,
        # #     "groups": [
        # #      "SPEED"
        # #     ],
        # #     "summary": {
        # #      "format": "Compacting HTML code, including any inline JavaScript and CSS contained in it, can save many bytes of data and speed up download and parse times."
        # #     },
        # #     "urlBlocks": [
        # #      {
        # #       "header": {
        # #        "format": "{{BEGIN_LINK}}Minify HTML{{END_LINK}} for the following resources to reduce their size by {{SIZE_IN_BYTES}} ({{PERCENTAGE}} reduction).",
        # #        "args": [
        # #         {
        # #          "type": "HYPERLINK",
        # #          "key": "LINK",
        # #          "value": "https://developers.google.com/speed/docs/insights/MinifyResources"
        # #         },
        # #         {
        # #          "type": "BYTES",
        # #          "key": "SIZE_IN_BYTES",
        # #          "value": "671B"
        # #         },
        # #         {
        # #          "type": "PERCENTAGE",
        # #          "key": "PERCENTAGE",
        # #          "value": "11%"
        # #         }
        # #        ]
        # #       },
        # #       "urls": [
        # #        {
        # #         "result": {
        # #          "format": "Minifying {{URL}} could save {{SIZE_IN_BYTES}} ({{PERCENTAGE}} reduction) after compression.",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/"
        # #           },
        # #           {
        # #            "type": "BYTES",
        # #            "key": "SIZE_IN_BYTES",
        # #            "value": "671B"
        # #           },
        # #           {
        # #            "type": "PERCENTAGE",
        # #            "key": "PERCENTAGE",
        # #            "value": "11%"
        # #           }
        # #          ]
        # #         }
        # #        }
        # #       ]
        # #      }
        # #     ]
        # #    },
        # #    "MinifyJavaScript": {
        # #     "localizedRuleName": "Minify JavaScript",
        # #     "ruleImpact": 0.1758,
        # #     "groups": [
        # #      "SPEED"
        # #     ],
        # #     "summary": {
        # #      "format": "Compacting JavaScript code can save many bytes of data and speed up downloading, parsing, and execution time."
        # #     },
        # #     "urlBlocks": [
        # #      {
        # #       "header": {
        # #        "format": "{{BEGIN_LINK}}Minify JavaScript{{END_LINK}} for the following resources to reduce their size by {{SIZE_IN_BYTES}} ({{PERCENTAGE}} reduction).",
        # #        "args": [
        # #         {
        # #          "type": "HYPERLINK",
        # #          "key": "LINK",
        # #          "value": "https://developers.google.com/speed/docs/insights/MinifyResources"
        # #         },
        # #         {
        # #          "type": "BYTES",
        # #          "key": "SIZE_IN_BYTES",
        # #          "value": "1.7KiB"
        # #         },
        # #         {
        # #          "type": "PERCENTAGE",
        # #          "key": "PERCENTAGE",
        # #          "value": "25%"
        # #         }
        # #        ]
        # #       },
        # #       "urls": [
        # #        {
        # #         "result": {
        # #          "format": "Minifying {{URL}} could save {{SIZE_IN_BYTES}} ({{PERCENTAGE}} reduction) after compression.",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/plugins/rotatingtweets/js/rotating_tweet.js?ver=1.9.3"
        # #           },
        # #           {
        # #            "type": "BYTES",
        # #            "key": "SIZE_IN_BYTES",
        # #            "value": "1.1KiB"
        # #           },
        # #           {
        # #            "type": "PERCENTAGE",
        # #            "key": "PERCENTAGE",
        # #            "value": "34%"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "Minifying {{URL}} could save {{SIZE_IN_BYTES}} ({{PERCENTAGE}} reduction) after compression.",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/plugins/contact-form-7/includes/js/scripts.js?ver=4.9.1"
        # #           },
        # #           {
        # #            "type": "BYTES",
        # #            "key": "SIZE_IN_BYTES",
        # #            "value": "663B"
        # #           },
        # #           {
        # #            "type": "PERCENTAGE",
        # #            "key": "PERCENTAGE",
        # #            "value": "18%"
        # #           }
        # #          ]
        # #         }
        # #        }
        # #       ]
        # #      }
        # #     ]
        # #    },
        # #    "MinimizeRenderBlockingResources": {
        # #     "localizedRuleName": "Eliminate render-blocking JavaScript and CSS in above-the-fold content",
        # #     "ruleImpact": 8,
        # #     "groups": [
        # #      "SPEED"
        # #     ],
        # #     "summary": {
        # #      "format": "Your page has {{NUM_SCRIPTS}} blocking script resources and {{NUM_CSS}} blocking CSS resources. This causes a delay in rendering your page.",
        # #      "args": [
        # #       {
        # #        "type": "INT_LITERAL",
        # #        "key": "NUM_SCRIPTS",
        # #        "value": "7"
        # #       },
        # #       {
        # #        "type": "INT_LITERAL",
        # #        "key": "NUM_CSS",
        # #        "value": "10"
        # #       }
        # #      ]
        # #     },
        # #     "urlBlocks": [
        # #      {
        # #       "header": {
        # #        "format": "None of the above-the-fold content on your page could be rendered without waiting for the following resources to load. Try to defer or asynchronously load blocking resources, or inline the critical portions of those resources directly in the HTML."
        # #       }
        # #      },
        # #      {
        # #       "header": {
        # #        "format": "{{BEGIN_LINK}}Remove render-blocking JavaScript{{END_LINK}}:",
        # #        "args": [
        # #         {
        # #          "type": "HYPERLINK",
        # #          "key": "LINK",
        # #          "value": "https://developers.google.com/speed/docs/insights/BlockingJS"
        # #         }
        # #        ]
        # #       },
        # #       "urls": [
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-includes/js/jquery/jquery.js?ver=1.12.4"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-includes/js/jquery/jquery-migrate.min.js?ver=1.4.1"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/plugins/rotatingtweets/js/jquery.cycle.all.min.js?ver=4.8.3"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/plugins/rotatingtweets/js/rotating_tweet.js?ver=1.9.3"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/plugins/google-analytics-for-wordpress/assets/js/frontend.min.js?ver=6.2.4"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://widgets.twimg.com/j/2/widget.js?ver=4.8.3"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/themes/gentle/js/minified-theme.min.js?ver=4.8.3"
        # #           }
        # #          ]
        # #         }
        # #        }
        # #       ]
        # #      },
        # #      {
        # #       "header": {
        # #        "format": "{{BEGIN_LINK}}Optimize CSS Delivery{{END_LINK}} of the following:",
        # #        "args": [
        # #         {
        # #          "type": "HYPERLINK",
        # #          "key": "LINK",
        # #          "value": "https://developers.google.com/speed/docs/insights/OptimizeCSSDelivery"
        # #         }
        # #        ]
        # #       },
        # #       "urls": [
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/plugins/captcha/css/front_end_style.css?ver=4.3.6"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-includes/css/dashicons.min.css?ver=4.8.3"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/plugins/captcha/css/desktop_style.css?ver=4.3.6"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/plugins/contact-form-7/includes/css/styles.css?ver=4.9.1"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/plugins/rotatingtweets/css/style.css?ver=4.8.3"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/plugins/wordpress-popular-posts/public/css/wpp.css?ver=4.0.12"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/themes/gentle/css/theme.css?ver=4.8.3"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/themes/gentle/css/style.css?ver=4.8.3"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://fonts.googleapis.com/css?family=Lato:300,400,700|Arvo:400,700|Titillium+Web:400,200,700"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "{{URL}}",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://fonts.googleapis.com/css?family=Quicksand:300"
        # #           }
        # #          ]
        # #         }
        # #        }
        # #       ]
        # #      }
        # #     ]
        # #    },
        # #    "OptimizeImages": {
        # #     "localizedRuleName": "Optimize images",
        # #     "ruleImpact": 1.5191000000000001,
        # #     "groups": [
        # #      "SPEED"
        # #     ],
        # #     "summary": {
        # #      "format": "Properly formatting and compressing images can save many bytes of data."
        # #     },
        # #     "urlBlocks": [
        # #      {
        # #       "header": {
        # #        "format": "{{BEGIN_LINK}}Optimize the following images{{END_LINK}} to reduce their size by {{SIZE_IN_BYTES}} ({{PERCENTAGE}} reduction).",
        # #        "args": [
        # #         {
        # #          "type": "HYPERLINK",
        # #          "key": "LINK",
        # #          "value": "https://developers.google.com/speed/docs/insights/OptimizeImages"
        # #         },
        # #         {
        # #          "type": "BYTES",
        # #          "key": "SIZE_IN_BYTES",
        # #          "value": "14.8KiB"
        # #         },
        # #         {
        # #          "type": "PERCENTAGE",
        # #          "key": "PERCENTAGE",
        # #          "value": "53%"
        # #         }
        # #        ]
        # #       },
        # #       "urls": [
        # #        {
        # #         "result": {
        # #          "format": "Compressing {{URL}} could save {{SIZE_IN_BYTES}} ({{PERCENTAGE}} reduction).",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/themes/gentle/images/ui/icons/social.jpg"
        # #           },
        # #           {
        # #            "type": "BYTES",
        # #            "key": "SIZE_IN_BYTES",
        # #            "value": "10KiB"
        # #           },
        # #           {
        # #            "type": "PERCENTAGE",
        # #            "key": "PERCENTAGE",
        # #            "value": "70%"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "Compressing {{URL}} could save {{SIZE_IN_BYTES}} ({{PERCENTAGE}} reduction).",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/themes/gentle/images/bg-lime-leather-tile.jpg"
        # #           },
        # #           {
        # #            "type": "BYTES",
        # #            "key": "SIZE_IN_BYTES",
        # #            "value": "2.7KiB"
        # #           },
        # #           {
        # #            "type": "PERCENTAGE",
        # #            "key": "PERCENTAGE",
        # #            "value": "39%"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "Compressing {{URL}} could save {{SIZE_IN_BYTES}} ({{PERCENTAGE}} reduction).",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/themes/gentle/images/bg-sky-leather-tile.jpg"
        # #           },
        # #           {
        # #            "type": "BYTES",
        # #            "key": "SIZE_IN_BYTES",
        # #            "value": "1.2KiB"
        # #           },
        # #           {
        # #            "type": "PERCENTAGE",
        # #            "key": "PERCENTAGE",
        # #            "value": "33%"
        # #           }
        # #          ]
        # #         }
        # #        },
        # #        {
        # #         "result": {
        # #          "format": "Compressing {{URL}} could save {{SIZE_IN_BYTES}} ({{PERCENTAGE}} reduction).",
        # #          "args": [
        # #           {
        # #            "type": "URL",
        # #            "key": "URL",
        # #            "value": "http://unhingedweb.com/wp-content/themes/gentle/images/bg-brown-leather-tile.jpg"
        # #           },
        # #           {
        # #            "type": "BYTES",
        # #            "key": "SIZE_IN_BYTES",
        # #            "value": "922B"
        # #           },
        # #           {
        # #            "type": "PERCENTAGE",
        # #            "key": "PERCENTAGE",
        # #            "value": "39%"
        # #           }
        # #          ]
        # #         }
        # #        }
        # #       ]
        # #      }
        # #     ]
        # #    },
        # #    "PrioritizeVisibleContent": {
        # #     "localizedRuleName": "Prioritize visible content",
        # #     "ruleImpact": 0,
        # #     "groups": [
        # #      "SPEED"
        # #     ],
        # #     "summary": {
        # #      "format": "You have the above-the-fold content properly prioritized. Learn more about {{BEGIN_LINK}}prioritizing visible content{{END_LINK}}.",
        # #      "args": [
        # #       {
        # #        "type": "HYPERLINK",
        # #        "key": "LINK",
        # #        "value": "https://developers.google.com/speed/docs/insights/PrioritizeVisibleContent"
        # #       }
        # #      ]
        # #     }
        # #    }
        # #   }
        # #  },
        # #  "version": {
        # #   "major": 1,
        # #   "minor": 15
        # #  }
        # # }
