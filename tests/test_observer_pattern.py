from observer.Observer import Observer, Subject, ConcreteObserver

def test_observer_pattern(capsys):
    subject = Subject()
    observer = ConcreteObserver()

    subject.subscribe(observer)
    subject.notify()

    captured = capsys.readouterr()
    assert captured.out.strip() == "Observer notified!"