## Loseless Compression Theory 

Suppose we have this string of text 'aaa' and because we have limited space, we need to make it smaller.

We can make this smaller by rewriting this string as '3a' making it smaller by one character.

If we ever want to go back to the original we can rewrite '3a' as 3 x a or 'aaa'

Lets consider the tradeoffs.

Pros: (Less Space)
- This occupies less space giving more room to store even more data.
- We can use loseless compression to share larger files over the internet without putting much strain on resources.
- With smaller occupation of storage it can speed up internet speeds that are slow versus decompressing which could be faster.

Cons: (More Work)
- Making a true loseless decompressor can be significantly challenging, though theoretically possible
- Storage → RAM → CPU → RAM → Storage
    - There is more works on keeping everything small, having slow components on large data can be time consuming.
