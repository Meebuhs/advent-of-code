# Takes input from input.txt
class Day07
  translate = {
      " AND " => '&', " OR " => '|', "NOT " => '~', " LSHIFT " => '<<', " RSHIFT " => '>>'
  }

  def self.create_wire(circuit, line)
    elements = line.split(" -> ").map(&:strip)
    circuit[elements[1]] = elements[0]
  end

  def self.evaluate_signal(circuit, translate, element)
    value = circuit[element]
    inputs = value.split(" ")
    puts "#{value}, #{inputs}"
    if inputs.size == 1
      numeric_value = Integer(inputs[0]) rescue nil
      if numeric_value != nil
        return numeric_value
      else
        return evaluate_signal(circuit, translate, inputs[0])
      end
    elsif inputs.size == 2
      return eval "~#{evaluate_signal(circuit, translate, inputs[1])}"
    else
      value = value.sub(Regexp.union(translate.keys), translate)
      puts "#{value}, #{inputs}, #{eval "#{evaluate_signal(circuit, translate, inputs[0])}#{value.split(/([a-z]+)/)[2]}#{evaluate_signal(circuit, translate, inputs[2])}"}"
      return eval "#{evaluate_signal(circuit, translate, inputs[0])}#{value.split(/([a-z]+)/)[2]}#{evaluate_signal(circuit, translate, inputs[2])}"
    end
  end



  circuit = Hash.new

  File.readlines('input.txt').each do |line|
    create_wire(circuit, line)
  end

  puts evaluate_signal(circuit, translate, 'a')

  puts circuit
end
