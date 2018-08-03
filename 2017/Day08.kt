import java.io.File

fun main(args: Array<String>) {
    var max = Integer.MIN_VALUE
    var maxRegister = ""
    val registers: MutableMap<String, Int> = mutableMapOf()

    File(".\\input.txt").useLines { lines -> lines.forEach {
        val input = it.split(" if ")
        val condition = input[1].split(" ")
        val instruction = input[0].split(" ")

        var add = 1
        if (instruction[1] == "dec") {
            add = -1
        }

        if (registers[condition[0]] == null) {
            registers[condition[0]] = 0
        }

        if (registers[instruction[0]] == null) {
            registers[instruction[0]] = 0
        }

        when (condition[1]) {
            "<" -> if (registers[condition[0]] !!< condition[2].toInt()) {
                registers[instruction[0]] = registers[instruction[0]] !!+ add * instruction[2].toInt()
            }
            ">" -> if (registers[condition[0]] !!> condition[2].toInt()) {
                registers[instruction[0]] = registers[instruction[0]] !!+ add * instruction[2].toInt()
            }
            "<=" -> if (registers[condition[0]] !!<= condition[2].toInt()) {
                registers[instruction[0]] = registers[instruction[0]] !!+ add * instruction[2].toInt()
            }
            ">=" -> if (registers[condition[0]] !!>= condition[2].toInt()) {
                registers[instruction[0]] = registers[instruction[0]] !!+ add * instruction[2].toInt()
            }
            "!=" -> if (registers[condition[0]] !!!= condition[2].toInt()) {
                registers[instruction[0]] = registers[instruction[0]] !!+ add * instruction[2].toInt()
            }
            "==" -> if (registers[condition[0]] == condition[2].toInt()) {
                registers[instruction[0]] = registers[instruction[0]] !!+ add * instruction[2].toInt()
            }
        }

        if (registers[instruction[0]]!! > max) {
            max = registers[instruction[0]]!!
            maxRegister = instruction[0]
        }
    }  }

    println("The maximum value currently stored in a register is ${registers.maxBy( { it.value } ) }")
    println("The maximum value encountered by a register was $maxRegister=$max")

}