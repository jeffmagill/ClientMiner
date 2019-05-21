
# The guy that that takes the raw gems and turns them into something people want
# I.e. The class that formats the raw data into the format we need
class Jeweler:

    tmp_file_location = 'tmp.csv'

    def __init__(self):
        pass

    @staticmethod
    def polish(data):

        if not isinstance(data, list) :
            raise AttributeError("`data` must be an array of dictionaries.")
        
        headers = Jeweler.get_all_headers(data)

        markup = ",".join(headers) 

        for item in data:
            markup += "\n"
            for key in headers:
                if key in item.keys():
                    markup += str(item[key]) + ","
                else:                
                    markup += ','

        return markup
        return "Look at the pretty gems: \n" + str(data)

    @staticmethod
    def get_all_headers(data):
        headers = []
        for item in data:
            for key in item: 
                if not key in headers:
                    headers.append(key)
        return headers
#   def render_results(items)
#     headers = []
#     result = ""
#     items.each do |url, fields|
#       # byebug
#
#       # headers.each do |field|
#       #
#       # end
#
#
#
#       fields.each do |key, value|
#         headers << key unless headers.include?(key)
#         result += ",#{value}"
#       end
#       result += "\n"
#     end
#     puts JSON.generate(items)
#     puts headers.join(",")
#     puts result
#
#   end
