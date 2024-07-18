# Chain-of-responsibility

Pass your requests along a chain of handlers. Upon receiving a request, each
**handler** decides either to process the request or to pass it to the next
handler in the chain.

    Every Handler can decide not to pass the request further down the chain and,
    effectively, stop any further processing.

    **OBS:** Its crucial that all handler classes implement the same interface.
    Each concrte handle should only cara about the following one having the
    execute method.


