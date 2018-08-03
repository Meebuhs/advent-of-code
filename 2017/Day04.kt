import java.io.File

fun main(args: Array<String>) {
    val linesList = mutableListOf<String>()
    File(".\\input.txt").useLines { lines -> lines.forEach { linesList.add(it) } }
    var correctFirstPasswords = linesList.size
    var correctSecondPasswords = linesList.size

    linesList.forEach {
        val words = it.split(" ").sorted()
        for (i in 0 until words.size - 1) {
            if (words[i] == words[i + 1]) {
                correctFirstPasswords--
                break
            }
        }

        val sortedWords = mutableListOf<String>()
        words.forEach {
            val sortedWord = it.toCharArray().sorted()
            sortedWords.add(sortedWord.joinToString(""))
        }
        sortedWords.sort()

        for (i in 0 until sortedWords.size - 1) {
            if (sortedWords[i] == sortedWords[i + 1]) {
                correctSecondPasswords--
                break
            }
        }
    }
    println("With part 1 definitions, there are $correctFirstPasswords correct passwords")
    println("With part 2 definitions, there are $correctSecondPasswords correct passwords")
}