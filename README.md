# Learning Log

## Day 0

I loved Advent of Code since my first participation in 2017 and I've been meaning to continue it year after year. Obviously, I have failed to do so thus far. I believe the reason why it was so much easier that first year vs all the subsequent ones is because I didn't have a job back then, so I could just spend the entire day figuring out these puzzles, if I wanted to. I would like to believe that after several years in the industry, I don't need as much time as I used to for these puzzles. On the other hand, the skills I need for work are very different than the skills I need for this. I also barely remember Python b/c I don't use it at work, but hopefully I'll pick it back up quick and learn some new stuff along the way.

## Day 1

Some quick thoughts. I don't know any more algorithms & data structures than I did before, so my initial solutions are very similar to what I would have came up with that first year. On the other hand, I can get to the solution a bit quicker just because I've been a dev long enough now that I don't need to print every line to see what I'm doing. I did still add a print statement here or there for debugging. What took the most time in this first puzzle was simply lots of Googling how to do things in Python, b/c while I had a rough idea, I forgot the exact syntax for certain things. I also spent time exploring using an object instead of a dictionary, but found that was more complex than what I really needed for the first iteration. I'm positive my solution is not the most elegant and I will look at how others solved it in the morning. Not really sure why I'm attempting these puzzles close to midnight when I have no intention of speed running this.

Morning update: yeah, even my dict was too complicated. I stored more data than I really needed and I could have done this more simply by just adding up the totals into a list and then sorting. I didn't know if part 2 needed knowledge of which elf or individual calories, not just the total. But next time, I should just refactor as needed and only store what I need to solve the problem.

## Day 2

There were not that many possible outcomes so I just wrote them all out. I'm pretty sure there's a concept that I'm missing that would help me solve this without doing that. It is late though, so I will research more tomorrow.

## Day 3

Easiest day for me thus far. I did keep making "off by one" type mistakes. Also, I knew that I could just import the alphabet instead of typing it all out, but I figured that would be faster than looking up how to do it. I still had to look up a bunch of basic stuff that I used to know but forgot b/c it's been a long time since I've coded in Python. The good thing is, my vague memory of how Python works still made it easy to Google what I needed. As usual, I'm sure there's an even better way of solving this, so I'll go study other people's solutions this weekend and see what else I can learn. I will also finally have the time to go back and fix some of our prior solutions to make them a bit more elegant.

## Day 4

I feel really good about today's puzzle. I took the time to refactor functions as needed and it paid off as I needed very little extra time to get the answer for part 2. After several days of reading other people's solutions, I think I know what I'm aiming for as I continue these puzzles:

* I have no intention of getting on the leaderboard, but I like doing the puzzles at midnight, when possible, because it's easier to see how much time I spend on each puzzle. If I am too tired, then I'll just make sure I time myself. Anyway, while I don't care for the competitive aspect, I do care that I'm spending less time solving these puzzles than I used to (relative to complexity), as a measurable method of seeing improvement in my coding.
* I have no intention to solve puzzles in as few lines as possible. I find those really hard to understand, and at work, when I code review stuff, I always comment on readability. That said, this isn't work and it is for fun. I do understand why others do it, but I still prefer readability. That said, I do care about making my solutions more elegant (defined here as "as concise as possible while maintaining readability"). When the puzzles get more complex, I will also have to pay more attention to performance. So far, it hasn't really mattered, which is typical for week 1 of Advent of Code.
