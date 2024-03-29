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
<p dir='rtl' align='right'>
* מחפש פינות של כלים לידם אפשר להניח כלי חדש.
<p dir='rtl' align='right'>
- מודד את המרחק לקצוות הלוח עבור כל נקודה חוקית.
<p dir='rtl' align='right'>
- מחזיר את הסכום המרחקים המינימלי.
<p dir='rtl' align='right'>
* סוכם את גודל הכלים הפנויים למשחק.
<p dir='rtl' align='right'>
- אם הסכום קטן מהמרחק המינימלי שמצאנו מגדירים את המרחק לפתרון הבעיה כאינסוף.
</p>
</p>
</p>
</p>
</p>

**Expanded nodes: 2726, score: 24**

![CORNERSH](https://i.imgur.com/dONwQng.png)

### Optimal solution
`python3 game.py -p tiny_set_2.txt -f ucs -s 8 8 -z corners`

**Expanded nodes: 2538354, score: 24**

![CORNEROPT](https://i.imgur.com/fSHTHNy.png)

## BlokusCoverProblem (2 points)
`python3 game.py -p small_set.txt -f astar -s 6 6 -H null_heuristic -z cover -x 3 3 "[(2,2), (5, 5), (1, 4)]"`

**Expanded nodes: 10974, score: 8**

![COVER](https://i.imgur.com/N3wVgh9.png)

## Blokus Cover Heuristic (6 points)
`python3 game.py -p small_set.txt -f astar -s 10 10 -H blokus_cover_heuristic -z cover -x 3 3 "[(2,2), (5, 5), (6, 7)]"`
<p dir='rtl' align='right'>
* מחפש פינות של כלים לידם אפשר להניח כלי חדש.
<p dir='rtl' align='right'>
* מודד את המרחק לנקודות הכיסוי עבור כל נקודה התחלה חוקית.
<p dir='rtl' align='right'>
* שומר את המרחקים המינימליים לכל נקודת כיסוי.
<p dir='rtl' align='right'>
* מחזיר את המרחק המקסימלי מבין אלה שנמצאו.
<p dir='rtl' align='right'>
בגלל שנקודות הכיסוי יכולות להתחבא אחת מאחורי השנייה, סכימה של המרחקים יכולה להוביל להיוריסטיקה לא להיות אדמיסבילית. כדי לפתור את הבעיה, פשוט נשתמש במרחק לנקודת הכיסוי הכי רחוקה.
</p>
</p>
</p>
</p>
</p>

**Expanded nodes: 29, score: 8**

![COVER_HEU](https://i.imgur.com/Wp4NxoE.png)

### OPTIMAL
`python3 game.py -p small_set.txt -f ucs -s 10 10 -z cover -x 3 3 "[(2,2), (5, 5), (6, 7)]"`

**Expanded nodes: 25811, score: 8**

![COVER_OPT](https://i.imgur.com/aQJKOmP.png)

## Closest point (2 points)
`python3 game.py -p valid_pieces.txt -s 10 10 -z sub-optimal -x 7 7 "[(5,5), (8,8), (4,9)]"`

<p dir='rtl' align='right'>* מחפש את הנקודת הכיסוי הקרובה לנקודת ההתחלה המוגדרת.</p>
<p dir='rtl' align='right'>* מגדיר בעיית כיסוי חדשה בעלת נקודת כיסוי אחת ונקודת התחלה.</p>
<p dir='rtl' align='right'>* פותר את הבעיה עם ucs ומקבל רשימה של פעולות.</p>
<p dir='rtl' align='right'>* יוצר state חדש עם הפעולות ומחפש נקודת התחלה חוקית ואת הנקודת הכיסוי הקרובה אליה.</p>
<p dir='rtl' align='right'>* חוזר חלילה עד שנגמרו נקודות הכיסוי.</p>


**Expanded nodes: 21, score: 9**

Time: _13.30s user 0.22s system_

![CLOSE_PT_1](https://i.imgur.com/hYqPyOn.png)

`python3 game.py -p valid_pieces.txt -s 10 10 -z sub-optimal -x 5 5 "[(3,4), (6,6), (7,5)]"`

**Expanded nodes: 17, score: 9**

Time: _15.59s user 0.16s system_

![CLOSE_PT_2](https://i.imgur.com/8YkbBOr.png)
##  Mini Contest (2 points extra credit) 
TODO
