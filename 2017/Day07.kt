import java.io.File

fun main(args: Array<String>) {
    var nodes = populateNodes()
    nodes = addParents(nodes)
    val treeRoot = findRoot(nodes)
    println("The name of the bottom program is $treeRoot")

    val levels = splitIntoLevels(nodes, treeRoot)
    nodes = updateWeights(nodes, levels)
    findUnbalancedElement(nodes, levels)
}

fun populateNodes(): Map<String, Node> {
    val nodes: MutableMap<String, Node> = mutableMapOf()
    File(".\\input.txt").useLines { lines -> lines.forEach {
        val args = it.split(" ")
        val size = args.size
        if (size <= 2) {
            nodes[args[0]] = (Node(args[0], emptyList(), parseWeight(args[1])))
        } else {
            val children: MutableList<String> = mutableListOf()
            for (i in 3 until size) {
                children.add(args[i].removeSuffix(","))
            }
            nodes[args[0]] = (Node(args[0], children, parseWeight(args[1])))
        }
    } }
    return nodes
}

fun parseWeight(weight: String): Int {
    return weight.substring(1, weight.length - 1).toInt()
}

fun addParents(input: Map<String, Node>): Map<String, Node> {
    val nodes = input.toMutableMap()
    File(".\\input.txt").useLines { lines -> lines.forEach {
        val args = it.split(" ")
        val size = args.size
        if (size > 2) {
            for (i in 3 until size) {
                nodes[args[i].removeSuffix(",")]!!.updateParent(args[0])
            }
        }
    } }
    return nodes
}

fun findRoot(nodes: Map<String, Node>): String {
    var element = nodes.keys.elementAt(0)
    while (nodes[element]!!.parent != "") {
        element = nodes[element]!!.parent
    }
    return(element)
}

fun splitIntoLevels(nodes: Map<String, Node>, treeRoot: String): List<List<String>> {
    var level: MutableList<String> = mutableListOf(treeRoot)
    val levels: MutableList<MutableList<String>> = mutableListOf()

    while (true) {
        levels.add(level)
        if (nodes[level[0]]!!.children.isEmpty()) {
            break
        } else {
            val nextLevel: MutableList<String> = mutableListOf()
            for (node in level) {
                nextLevel.addAll(nodes[node]!!.children)
            }
            level = nextLevel
        }
    }
    return levels
}

fun updateWeights(nodes: Map<String, Node>, levels: List<List<String>>): Map<String, Node> {
    for (level in levels.reversed()) {
        for (node in level) {
            var weight = 0
            for (child in nodes[node]!!.children) {
                weight += nodes[child]!!.weight
            }
            nodes[node]!!.updateWeight(weight + nodes[node]!!.weight)
        }
    }
    return nodes
}

fun findUnbalancedElement(nodes: Map<String, Node>, levels: List<List<String>>) {
    var element = ""
    var neighbour = ""
    for (level in levels) {
        for (node in level) {
            val children = nodes[node]!!.children
            for (index in 0 until children.size) {
                if (nodes[children[index]]!!.weight != nodes[children[(index + 1) % (children.size - 1)]]!!.weight) {
                    if (nodes[children[index]]!!.weight != nodes[children[(index + 2) % (children.size - 1)]]!!.weight) {
                        element = children[index]
                        neighbour = children[(index + 1) % (children.size - 1)]
                    }
                }
            }
        }
    }

    val unbalancedChildren = nodes[element]!!.children
    var weightOfChildren = 0
    for (child in unbalancedChildren) {
        weightOfChildren += nodes[child]!!.weight
    }
    val weightDifference = nodes[element]!!.weight - nodes[neighbour]!!.weight
    val requiredWeight = nodes[element]!!.weight - weightOfChildren - weightDifference
    println("Unbalanced element is $element requires a weight of $requiredWeight to balance")
}

class Node(name: String, children: List<String>, weight: Int) {
    val name: String
    val children: List<String>
    var weight: Int
    var parent: String

    init {
        this.name = name
        this.children = children
        this.weight = weight
        this.parent = ""
    }

    fun updateWeight(weight: Int) {
        this.weight = weight
    }

    fun updateParent(parent: String) {
        this.parent = parent
    }
}
