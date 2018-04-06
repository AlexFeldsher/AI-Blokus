# AI-Blokus

##  Depth first search (2 points)
`python3 game.py -p tiny_set.txt -s 4 7 -z fill`

**Expanded nodes: 1163, score: 17**
![DFS](https://i.imgur.com/JNUhuR2.png)

## Breadth first search (1 points)
`python3 game.py -p tiny_set.txt -f bfs -s 4 7 -z fill`

**Expanded nodes: 2114, score: 17**
![BFS](https://i.imgur.com/dmCM0R1.png)

## BlokusCornersProblem (2 points)
`python3 game.py -p tiny_set_2.txt -f bfs -s 6 6 -z corners`

**Expanded nodes: 9023, score: 17**
![BlokusCornersProblem](https://i.imgur.com/o9VGBAa.png)

## Uniform cost search (2 points)
`python3 game.py -p tiny_set_2.txt -f ucs -s 6 6 -z corners`

**Expanded nodes: 19070, score: 17**
![UCS1](https://i.imgur.com/jPCV5yV.png)

`python3 game.py -p small_set.txt -f ucs -s 5 5 -z corners`

**Expanded nodes: 22191, score: 13**
![UCS2](https://i.imgur.com/xdmqV0w.png)

## A* search (3 points)
`python3 game.py -p tiny_set_2.txt -f astar -s 6 6 -z corners -H null_heuristic`

**Expanded nodes: 19070, score: 17**
![ASTAR](https://i.imgur.com/16apZ9L.png)

## Blokus Corners Heuristic (4 points)
`python3 game.py -p tiny_set_2.txt -f astar -s 8 8 -z corners -H blokus_corners_heuristic `

**Expanded nodes: 4030, score: 24**
![CORNERSH](https://i.imgur.com/jplFr7n.png)

## BlokusCoverProblem (2 points)
`python3 game.py -p small_set.txt -f astar -s 6 6 -H null_heuristic -z cover -x 3 3 "[(2,2), (5, 5), (1, 4)]"`

**Expanded nodes: 10974, score: 8**
![COVER](https://i.imgur.com/N3wVgh9.png)

## Blokus Cover Heuristic (6 points)
TODO

## Closest point (2 points)
TODO

##  Mini Contest (2 points extra credit) 
TODO