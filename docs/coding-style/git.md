# GIT
## Commit Style

In order to achieve a uniform naming for commit messages the following **commit style** should be used when creating a new commit message.

| Keyword | Description                                                                                                                                   |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| ADD     | Is used if there is a new change in the code. **e.g.** `git commit -m "ADD function XY()"`                                                    |
| REMOVE  | Is used whenever a major part of the code is removed. This scenario should be rater infrequent. **e.g.** `git commit -m "REMOVE variable XY"` |
| FIX     | Used for minor changes of an already existing part of the code. **e.g** `git commit -m "FIX functionality of XY"`                             |
| UPDATE  | Is used when there is a major change in multiple code-segments. **e.g** `git commit -m "UPDATE setup of analog sensors"`                      |
