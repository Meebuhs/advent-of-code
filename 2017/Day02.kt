import java.io.File

// Takes input from input.txt
fun main(args: Array<String>) {
    val checksums = intArrayOf(0, 0)
    val linesList = mutableListOf<String>()
    File(".\\input.txt").useLines { lines -> lines.forEach { linesList.add(it) } }
    linesList.forEach {
        for ((index, value) in calculateChecksum(it).withIndex()) {
            checksums[index] += value
        }
    }

    println("The checksum is ${checksums[0]}")
    println("The sum of evenly divisible values is ${checksums[1]}")
}

fun calculateChecksum(line: String): IntArray {
    val results = intArrayOf(0, 0)
    val numbers = line.split("\\s+".toRegex()).map { it.toInt() }.sorted()

    // Part One
    results[0] = numbers[numbers.lastIndex] - numbers[0]

    // Part Two
    for (i in (0 .. numbers.lastIndex)) {
        for (j in (i + 1 .. numbers.lastIndex)) {
            if (numbers[j].rem(numbers[i]) == 0) {
                results[1] = (numbers[j] / numbers[i])
            }
        }
    }

    return results
}