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
* I have no intention to solve puzzles in as few lines as possible. I find those really hard to understand, and at work, when I code review stuff, I always comment on readability. Of course, this isn't work and it is for fun. I do understand why others do it, but I still prefer readability. That said, I do care about making my solutions more elegant (defined here as "as concise as possible while maintaining readability"). When the puzzles get more complex, I will also have to pay more attention to performance. So far, it hasn't really mattered, which is typical for week 1 of Advent of Code.

## Day 5

First day I didn't start the puzzles at midnight. Took ~2 hours for part 1 and ~1 hour for part 2. Honestly, part 2 should have been really quick, except I spent ~90% of that time struggling b/c I didn't realize that I needed to deep copy the dict or else I'm not starting from the initial stacks, but rather the ending stacks from part 1, even though I created a new variable to store the initial stacks. Lesson learned. For part 1, I also wasted a lot of time debugging, but mostly b/c I debugged in the wrong place. I had two incorrect assumptions: (1) that the boxes I move from one stack to the other are single digits and (2) that my mistake was in the actual moving part and not in the instruction part. Other than that, honestly, this puzzle wasn't hard, just took awhile to parse.

## Day 6

Since it's already past midnight and I just wrapped up Day 5, I'm not about to start another puzzle. I will do this during the day tomorrow (technically, later today). Ideally, I would like to finish my puzzles before the 24 hour mark.

Later: Maybe I should have just done this puzzle right after I wrapped up day 5. It's a good balance to yesterday's puzzle that took hours. I did both parts under 15 mins and would have been faster if I didn't actually read the entire story and went straight to what they were looking for. Since I'm not trying to speed code, I actually enjoy reading everything. That said, I still got it wrong on the first try, because I took the index of the first character instead of the final one in the four-character marker. Once I realized my mistake, I got the answer so fast, AoC made me wait before resubmitting. Heh.

## Day 7

Alright, we've come to it - the first puzzle I need to get back to later. The minute I saw this puzzle, I recognized it as a tree traversal puzzle. In 2017, this type of puzzle was the first I really struggled with, if I remember correctly. The obvious way of solving this is using recursion, which I hate. At some point, I finally learned it for interviews, and in fact, was tested on it during a mock one that ended up going so well that I got a real job offer from it. THat said, I really haven't needed to do any type of recursion at work so basically, it's something I'm rusty at doing and I was never really good at it in the first place. Anyway, I did figure out how I wanted to solve the puzzle pretty quickly after reading the prompt, but I really wasn't in the mood to implement my plan, so I decided to play with chatGPT last night. Instead of feeding it the puzzle description directly, I gave it my interpretion of it and my plans for solving it, which it implemented not entirely correctly, but definitely gave me a good foundation to build on. I have since decided not to use recursion though. Someone gave me the hint that I didn't really need to think of these directories as directories and I could simplify in a way that doesn't require recursion at all. I think it'll be weekend before I'll have time to implement, so for now, I'll just save the code that chatGPT gave. I may or may not end up using some of it for my second plan, but it's nice to keep as a memory of my trial with it.

## Day 8

The way I'm going about solving the puzzle is definitely not great, but I did manage to complete part 1 after lots of trial & error. Started on part 2, but there's so much to refactor that I'm giving up for tonight.

# Day 9

Feverish from covid vaccine, so not thinking straight. Still, I wanted to attempt today's puzzle. Need to come back to this later. I'm not handling the diagonals correctly and I know that, but my brain cannot focus anymore.

Realistically, going forward, the puzzles are only going to get harder. So, my intention is to try and solve what I can within the 24 hour period, but if I don't succeed, I will get back to it in January. Unfortunately, December is always a busy time so I can't just dedicate hours to AoC like I did in 2017. I'm already proud of myself for keeping up with it longer than I have previous years. As of right now, I have more total stars from 2018, but I gave up after day 5 and just sporadically went back to it. 
