class Observer:
    """
       This is an observer superclass. It registers itself to
       receive notifications from an observable object, and contains a
       default 'notify' method for an observable to call.
    """

    def __init__(self, observable):
        """
           This method initializes and observer object, registering
           it with a provided observable and remembers which
           observable it is registered to.
        """
        self._observable = observable
        self._observable.register_observer(self)

    def notify(self, observable, *args, **kwargs):
        """
           This method is a default notify method that prints the
           observer, arguments, keyword arguments and observable
           passed to it. It should be overwritten in a concrete
           observer class.
        """
        print(f'{self} got {args} and {kwargs} from {observable}')
