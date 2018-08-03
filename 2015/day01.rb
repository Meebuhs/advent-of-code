# Assumes input consists only of () to eliminate a second check
# Errant characters will result in an incorrect (low) result
class Day01
  floor = 0
  position = 1
  basement_position = 0

  gets.chomp.split('').each do |char|
    if char == '('
      floor += 1
    else
      floor -= 1
    end
    if floor == -1 && basement_position == 0
      basement_position = position
    end
    position += 1
  end

  puts "floor: #{floor}"
  puts basement_position == 0 ? 'basement never reached' : "basement reached at: #{basement_position}"
end