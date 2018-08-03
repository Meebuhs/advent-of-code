import java.io.File

fun main(args: Array<String>) {

    var input = mutableListOf<Int>()
    File(".\\input.txt").useLines { lines -> lines.forEach { input.add(it.toInt()) } }

    println("With part 1 rules, exit takes ${calculateFirstSteps(input)} steps to reach")
    println("With part 2 rules, exit takes ${calculateSecondSteps(input)} steps to reach")
}

    fun calculateFirstSteps(input: List<Int>): Int {
        var maze = input.toMutableList()
        val bound = maze.size
        var index = 0
        var steps = 0
        while (index < bound) {
            index += maze[index]++
            steps++
        }
        return steps
    }

    fun calculateSecondSteps(input: List<Int>): Int {
        var maze = input.toMutableList()
        val bound = maze.size
        var index = 0
        var steps = 0
        while (index < bound) {
            if (maze[index] >= 3) {
                index += maze[index]--
            } else {
                index += maze[index]++
            }
            steps++
        }
        return steps
    }