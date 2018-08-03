fun main(args: Array<String>) {
    val input = readLine()!!.toDouble()
    println("Distance to the access port: ${calculateDistance(input)}")
    println("First value which is larger: ${calculateValue(input)}")
}

// Accepts input > 1
fun calculateDistance(input: Double): Double {
    val sideLength = Math.ceil(Math.sqrt(input))
    val corner = sideLength * sideLength

    val distanceToNearestCorner = Math.min((corner - input) % (sideLength - 1), Math.abs((sideLength - 1 - (corner - input)) % (sideLength - 1)))
    val distanceToMiddleOfSide = Math.abs(Math.floor(sideLength/2) - distanceToNearestCorner)
    return Math.floor(sideLength / 2) + distanceToMiddleOfSide
}

fun calculateValue(input: Double): Int {
    var sideLength = 3
    val board = Array(30, { IntArray(30) })
    board[15][15] = 1
    board[16][15] = 1
    var xpos = 16
    var ypos = 15
    while (true) { // one ring traversal
        // up side length - 2
        for (i in 1..(sideLength - 2)) {
            ypos -= 1
            if (processMove(board, input, xpos, ypos)) {
                return board[xpos][ypos]
            }
        }
        // left side length - 1
        for (i in 1..(sideLength - 1)) {
            xpos -= 1
            if (processMove(board, input, xpos, ypos)) {
                return board[xpos][ypos]
            }
        }
        // down side length - 1
        for (i in 1..(sideLength - 1)) {
            ypos += 1
            if (processMove(board, input, xpos, ypos)) {
                return board[xpos][ypos]
            }
        }
        // right side length
        for (i in 1..(sideLength)) {
            xpos += 1
            if (processMove(board, input, xpos, ypos)) {
                return board[xpos][ypos]
            }
        }
        sideLength += 2
    }
}

fun processMove(board: Array<IntArray>, input: Double, xpos: Int, ypos: Int): Boolean {
    var value = 0
    for (x in -1..1) {
        for (y in -1..1) {
            if (x != 0 || y!= 0) {
                value += board[xpos + x][ypos + y]
            }
        }
    }
    board[xpos][ypos] = value
    return (value > input)
}