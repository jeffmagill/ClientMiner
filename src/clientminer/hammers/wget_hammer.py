import scrapy

class WgetHammer:

    @staticmethod
    def hit(url):
        print (f"Hitting '{url}' with Wget")

        proc = subprocess.Popen(["wget", url], stdout=subprocess.PIPE)
        out = proc.communicate()[0]
        text = out.upper()

        print (f"This is what we captured: {text}")
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
