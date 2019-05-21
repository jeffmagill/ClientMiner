import subprocess
import re

class WgetHammer:

    wall_clock_regex = re.compile(r"Total wall clock time: ([\d+\.]+\w*)")
    resource_count_regex = re.compile(r"Downloaded: (\d+) files")
    file_size_regex = re.compile(r"Downloaded: \d+ files, ([\d+\.KMG]+\w*)")
    

    @staticmethod
    def hit(url):
        print (f"Hitting '{url}' with Wget")

        proc = subprocess.Popen(["wget", "-p", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()
        body = stderr.decode('utf-8')
        
        result = {
            "download-duration": WgetHammer.capture(WgetHammer.wall_clock_regex, body),
            "download-resource-count": WgetHammer.capture(WgetHammer.resource_count_regex, body),
            "download-file-size": WgetHammer.capture(WgetHammer.file_size_regex, body)
        }
        return result
        
    
    @staticmethod
    def capture(regex, value):
        match = regex.search(value)
        if match:
            return match.group(1)
        else:
            return ""

        #
        #     stdout, stderr, status = Open3.capture3("wget -p #{url}")
        #     output = stderr
        #
        #     response = {}
        #     response["Wget Load Time"] = capture_regex(output, /Total wall clock time: ([\d+\.]+\w*)/).to_s
        #     response["Wget Resource Count"] = capture_regex(output, /Downloaded: (\d+) files/).to_s
        #     response["Wget File Size"] = capture_regex(output, /Downloaded: \d+ files, ([\d+\.]+\w*)/).to_s
        #     return response
        #   end
        #
        #   def self.capture_stdout
        #     old_stdout = $stdout
        #     $stdout = StringIO.new
        #     yield
        #     $stdout.string
        #   ensure
        #     $stdout = old_stdout
        #   end
        #
        #   def self.capture_regex(value, regex)
        #     matches = regex.match(value)
        #     if matches.nil? || matches.length == 0
        #       return nil
        #     else
        #       return matches[0]
        #     end
        #   end
        # end
