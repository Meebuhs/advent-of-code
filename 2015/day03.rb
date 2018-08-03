# Assumes input consists only of ^>v<
class Day03
  santa_position = [0, 0]
  team_position = [0, 0, 0, 0] # [santa x, santa y, robo x, robo y]
  robo_turn = false

  solo_houses = {santa_position => 1}
  team_houses = {team_position[0, 2] => 1}

  gets.chomp.split('').each do |char|
    case char
      when '^'
        santa_position[1] += 1
        robo_turn ? team_position[3] += 1 : team_position[1] += 1
      when 'v'
        santa_position[1] -= 1
        robo_turn ? team_position[3]-= 1 : team_position[1] -= 1
      when '>'
        santa_position[0] += 1
        robo_turn ? team_position[2] += 1 : team_position[0] += 1
      when '<'
        santa_position[0] -= 1
        robo_turn ? team_position[2] -= 1 : team_position[0] -= 1
    end

    if solo_houses[santa_position].nil?
      solo_houses[santa_position] = 1 # New house receives first present
    else
      solo_houses[santa_position] += 1
    end

    current_team_position = robo_turn ? team_position[2, 2] : team_position[0, 2]

    if team_houses[current_team_position].nil?
      team_houses[current_team_position] = 1
    else
      team_houses[current_team_position] += 1
    end

    robo_turn = !robo_turn
  end

  puts "santa alone delivered at least one present to #{solo_houses.size} houses"
  puts "the santa team delivered at least one present to #{team_houses.size} houses"
end