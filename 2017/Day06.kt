fun main(args: Array<String>) {
    val input = readLine()!!.split("\t").map { it.toInt() }
    var state = input.toMutableList()
    val states = mutableListOf<List<Int>>()
    val bound = input.size
    var cycles = 0
    var recurrence = 0

    while (true) {
        val nextToRedistribute = state.indexOf(state.max())
        var index = nextToRedistribute
        val numberToRedistribute = state[nextToRedistribute]
        state[index] = 0
        for (i in 0 until numberToRedistribute) {
            if (++index == bound) {
                index = 0
            }
            state[index]++
        }
        cycles++
        if (states.contains(state)) {
            recurrence = cycles - states.indexOf(state) - 1
            break
        } else {
            states.add(state.toMutableList())
        }
    }

    println("The number of redistribution cycles to produce a known state is $cycles")
    println("The infinited loop is $recurrence cycles long")
}