#!/usr/bin/env ruby
# puts ARGV[0].scan(/\[\+(\w+)]\,\[\+(\w+)]\,[+]/).join

# Define the regular expression pattern to capture sender, receiver, and flags
pattern = /\[from:(\S+)\] \[to:(\S+)\] \[flags:(.*?)\]/

# Read the input log file line by line
File.readlines(ARGV[0]).each do |line|
  match_data = line.match(pattern)
  if match_data
    sender = match_data[1]
    receiver = match_data[2]
    flags = match_data[3]
    puts "#{sender},#{receiver},#{flags}"
  end
end
