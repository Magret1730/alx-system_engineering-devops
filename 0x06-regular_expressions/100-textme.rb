#!/usr/bin/env ruby
puts ARGV[0].scan(/\[(\w\s)+]\] \[[(\w\s)+]\] \[[-+]]/).join
