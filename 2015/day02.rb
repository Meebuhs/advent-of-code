# Takes input from input.txt
class Day02
  # Sorted input {(l, w, h) st l <= w <= h}
  # Surface area {2lw + 2lh + 2wh} + Area of smallest side {lw}
  def self.calculate_paper(sides)
    return 3*sides[0]*sides[1] + 2*sides[0]*sides[2] + 2*sides[1]*sides[2]
  end

  # Perimeter of smallest side {2l + 2w} + volume of present {lwh}
  def self.calculate_ribbon(sides)
    return (2*sides[0] + 2*sides[1]) + (sides[0] * sides[1] * sides[2])
  end

  paper = 0
  ribbon = 0

  File.readlines('input.txt').each do |line|
    sides = line.split('x').map(&:to_i).sort
    paper += calculate_paper(sides)
    ribbon += calculate_ribbon(sides)
  end

  puts "paper required: #{paper}"
  puts "ribbon required: #{ribbon}"

end