# Command

Turns a request into a stand-alone object that contains all information about
the request. This transformation lets you pass requests as a method arguments,
delay or queue a request's execution, and support undoable operations.

Invoker: an object that knows how to execute a command but is decoupled from the
command and receiver.