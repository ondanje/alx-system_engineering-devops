#!/usr/bin/env ruby
#This exercise was prepared for you by Guillaume Plessis,
#VP of Infrastructure at TextMe.
#It is something he uses daily. You can thank Guillaume for his project on Twitter.

puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
