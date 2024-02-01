# Assignment 1: Python Refresher 

### echo.py
Here is my echo.py code. The comments I wrote were mostly to help myself, since I haven't used python for a couple of semesters. It took me a while to remember the coding conventions of Python, but once that was cleared up, the logic was easy. Looking at the output, I start with printing the original text then ir iterates through repetitions, stepping -1 each iteration to achieve the echoing effect. It was a short, simple, and a great first Python code to begin the semester with!
![Image Alt Text](https://i.imgur.com/1TGi2Yi.png)

### fib.py
Here is my fib.py code. Again, the comments are basic and are just there to help me work through the code properly. I initially did not want to use recursion in my function, which made the process take a lot longer than it should have. When I was running the code iteratively, the function did not call itself in fib() so I had a for loop in __name__ instead. This method did get the desired output, but it did not match the screenshot that the professor had on ICON so I changed fib() to be a recusive function so that __name__ only had to call fib. Another difficult aspect of this code was working with decorators. I have never used decorators in my previous experience in Python, so I had to take my time to learn about how they work. I also had to learn a lot about the time module in order to create the timer decorator. I initially was using time.time() for the time calculations, but that had the unwanted effect of adding a comma and extra parentheses when printing the output. While trying to figure out how to troubleshoot that, I came across an article saying that per_counter() is better than time() for benchmarking so I tried using it, and it seems to have fixed the issue with no compromises. I tried different combinations for the printed string and I think the final product matches the screenshot of the output the professor has on ICON. Another difficult aspect of this code with using lru_cache. I wasn't sure if it was meant to be implemented in the code, or if it runs properly as a decorator for fib as is. Either way, I am happy with the final outcome of this code and its output.  
(first image showing code with partial output)
![Image Alt Text](https://i.imgur.com/RsqivcQ.png)
(second image showing extended output)
![Image Alt Text](https://i.imgur.com/Ee19nW9.png)

For the graph, I used Canva to create a simple line graph and input the output data. It's simple but effective for conveying the linear progression of execution times.
![Image Alt Text](https://i.imgur.com/mpPu1GY.jpg)
