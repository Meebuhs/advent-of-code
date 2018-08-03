# Will run until a collision is found
require 'digest'

class Day04
  input = gets.chomp
  i = 1
  five_found = false
  six_found = false

  while !six_found
    md5 = Digest::MD5.hexdigest(input + i.to_s)

    if five_found == false and md5 =~ /^(00000)/
      puts "#{i}: #{input}#{i} gives an md5 of #{md5}"
      five_found = true
    end

    if md5 =~ /^(000000)/
         puts "#{i}: #{input}#{i} gives an md5 of #{md5}"
         six_found = true
       end
    i += 1
  end
end

