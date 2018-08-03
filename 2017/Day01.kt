// Assumes input consists of only 1-9
fun main(args: Array<String>) {
    val input = readLine()
    if (input != null) {
        val captchas = calculateCaptcha(input)
        println("Part 1 captcha is ${captchas[0]}")
        println("Part 2 captcha is ${captchas[1]}")
    }
}

fun calculateCaptcha(captcha: String): IntArray {
    val counts = intArrayOf(0, 0)

    for (i in 0 until captcha.length) {
        // Part One
        if (captcha[i] == captcha[(i + 1).rem(captcha.length)]) {
            counts[0] += (Character.getNumericValue(captcha[i]))
        }
        // Part Two
        if (captcha[i] == captcha[(i + captcha.length/2).rem(captcha.length)]) {
            counts[1] += (Character.getNumericValue(captcha[i]))
        }
    }

    return counts
}