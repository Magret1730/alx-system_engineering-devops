#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:([\w\s\+]+)\] \[to:([\w\s\+]+)\] \[flags:([^\]]+)\]/).map { |match| match.join(",") }.join(",")
