
# The guy that that takes the raw gems and turns them into something people want
# I.e. The class that formats the raw data into the format we need
class Jeweler:

    def __init__(self):
        pass

    @staticmethod
    def polish(data):
        return "Look at the pretty gems: \n" + str(data)

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
