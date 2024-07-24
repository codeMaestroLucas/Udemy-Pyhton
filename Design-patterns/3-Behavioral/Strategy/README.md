# Strategy

Lets u define a family of algorithms, put each of them into a separate class,
and make their objects interchangeable.

- Each class is called **Strategies**.

- The original class is called *Context*. It delegates the work to a linked
strategy object instead of executing it on its own.