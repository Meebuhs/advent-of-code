# Takes input from input.txt
class Day05
  part1_nice = 0
  part1_naughty = 0

  part2_nice = 0
  part2_naughty = 0

  # Cannot contain ab cd pq or xy
  # Must have at least one substring of length two made of the same character
  # Must have at least three vowels
  def self.part1_check(line)
    if not line =~ /(ab|cd|pq|xy)/ and line =~ /(.)\1/ and line =~ /[aieou].*[aieou].*[aeiou]/
      return true
    end
    return false
  end

  # Must have at least one substring of length two which appears twice while not overlapping
  # Must have at least one substring of length three of the format 'aba'
  def self.part2_check(line)
    if line =~ /(..).*\1/ and line =~ /(.).\1/
      return true
    else
      return false
    end
  end

  File.readlines('input.txt').each do |line|
    part1_check(line) ? part1_nice += 1 : part1_naughty += 1
    part2_check(line) ? part2_nice += 1 : part2_naughty += 1
  end

  puts "for part 1, santa's file has #{part1_nice} nice strings and #{part1_naughty} naughty strings"
  puts "for part 2, santa's file has #{part2_nice} nice strings and #{part2_naughty} naughty strings"
end
