# Parent class
class hero:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


# sub class inheriting from hero
class good_guy(hero):
    def speak(self):
        return f"{self.name} says 'Hulk Smash!'"


# sub class inheriting from hero
class bad_guy(hero):
    def speak(self):
        return f"{self.name} says 'I am inevitable!'"


def main():
    # Creating instances of good_guy and bad_guy classes
    gg = good_guy("Hulk")
    bg = bad_guy("Thanos")

    # Calling speak() method on instances
    print(gg.speak())  # Output: Hulk says 'Hulk Smash!'
    print(bg.speak())  # Output: Thanos says 'I am inevitable!'


if __name__ == "__main__":
    main()
