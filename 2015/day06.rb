# Takes input from input.txt
class Day06
  def self.count_lights(lights)
    total_lights_on = 0
    total_brightness = 0
    lights.each_index do |x|
      lights[x].each_index do |y|
        if lights[x][y][0]
          total_lights_on += 1
        end
        total_brightness += lights[x][y][1]
      end
    end
    return [total_lights_on, total_brightness]
  end

  def self.toggle_lights(lights, top_left, bottom_right)
    (top_left[0]..bottom_right[0]).each do |x|
      (top_left[1]..bottom_right[1]).each do |y|
        lights[x][y][0] = !lights[x][y][0]
        lights[x][y][1] += 2
      end
    end
  end

  def self.turn_lights_on_or_off(lights, state, top_left, bottom_right)
    state == "on" ? (brightness = 1; value = true) : (brightness = -1; value = false)
    (top_left[0]..bottom_right[0]).each do |x|
      (top_left[1]..bottom_right[1]).each do |y|
        lights[x][y][0] = value
        lights[x][y][1] += brightness
        if lights[x][y][1] < 0
          lights[x][y][1] = 0
        end
      end
    end
  end

  def self.parse_instruction(lights, instructions)
    if instructions[0] == "toggle"
      top_left = instructions[1].split(",").map(&:to_i)
      bottom_right = instructions[3].split(",").map(&:to_i)
      toggle_lights(lights, top_left, bottom_right)
    else
      top_left = instructions[2].split(",").map(&:to_i)
      bottom_right = instructions[4].split(",").map(&:to_i)
      turn_lights_on_or_off(lights, instructions[1], top_left, bottom_right)
    end
  end

  def self.initialize_lights_array
    lights = Array.new(1000)
    lights.each_index do |x|
      lights[x] = Array.new(1000)
      lights[x].each_index do |y|
        lights[x][y] = [false, 0]
      end
    end
    return lights
  end

  lights = initialize_lights_array
  File.readlines('input.txt').each do |line|
    parse_instruction(lights, line.split(' '))
  end

  puts count_lights(lights)

end