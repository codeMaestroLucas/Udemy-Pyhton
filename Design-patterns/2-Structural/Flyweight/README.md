# Flyweight

Let u fit more objects into the available amount of RAM by sharing common parts
of state between multiple objects instead of keeping all of the data in each
object.

    Flyweight suggests that u stop storing the extrinsic stat inside the object.
Instead, u should pass this state to specific methods wich rely on it.

    - The object should store **only** the essential values.