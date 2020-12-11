class Observable:
    """
       This is an observable superclass. It registers and unregisters
       bserver objects to and from a list and sends notifications to
       all registered observers.
    """

    def __init__(self):
        """
           This method initializes self with an empty list of
           observers and sets the changed variable to false.
        """
        self._observers = []
        self._changed = False

    def register_observer(self, observer):
        """
           This method registers an observer object with
           the observable class.
        """
        self._observers.append(observer)

    def unregister_observer(self, observer):
        """
           This method unregisters and observer object with
           the observable class.
        """
        self._observers.remove(observer)

    def notify_observers(self, *args, **kwargs):
        """
           This method sends a notification to all registered observers
           if the changed state is true. The notification includes
           the originating observable object and any arguments or
           keyword arguments (note: this is agnostic regarding arguments
           and keyword arguments, leaving it up to concrete classes
           to parse the data). After notification it sets the
           observable's changed state to False.
        """
        if self.has_changed():
            for observer in self._observers:
                observer.notify(self, *args, **kwargs)
            self.clear_changed()
        else:
            return

    def has_changed(self):
        """
           This method checks whether the observable object has changed
           and returns a boolean value.
        """
        if self._changed:
            return True
        else:
            return False

    def set_changed(self):
        """
           This method sets the observable's changed state to True.
        """
        self._changed = True

    def clear_changed(self):
        """
           This method sets the observable's changed state to False/
        """
        self._changed = False
