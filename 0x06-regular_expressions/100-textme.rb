#!/usr/bin/env ruby
puts ARGV[0].scan(/([A-Z][a-z][0-9]/s)+/).join
