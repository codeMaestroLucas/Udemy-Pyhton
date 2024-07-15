# Builder

Construct complex objects step by step.

Every step need to be extracted of it own class and move it to separate objects called **builders**.

    - Ex.: In an HOUSE class u might have buildWalls, buildDoor, etc.

The DIRECTOR is used to call the constructor of each class.

    Having an DIRECTOR isn't strictly necessary. However, the directo class might be a good place to put various construction routines so y can reuse them across your program.