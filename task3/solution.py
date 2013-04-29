class Person:

    """ Model of a person with parents and children. """
    MALE = 'M'
    FEMALE = 'F'

    def __init__(self, name, birth_year, gender, mother=None, father=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender

        self.mother = mother
        self.father = father

        self._children = list()

        for parent in self._get_known_parents():
            parent._add_child(self)

    def _add_child(self, child):
        # Add a new child to the current person.
        self._children.append(child)

    def _get_known_parents(self):
        # A helper function that returns the parents of the current person,
        # which are not `null`.
        return [parent for parent in [self.mother, self.father] if
                parent is not None]

    def _get_siblings(self, gender):
        """ Return all siblings of this person.

        Siblings are considered to be people with at least one common parent

        """
        siblings = set()
        for parent in self._get_known_parents():
            siblings |= set(parent.children(gender))
        siblings -= {self}
        return siblings

    def get_brothers(self):
        """ Return a list of all brothers of this person. """
        return list(self._get_siblings(self.MALE))

    def get_sisters(self):
        """ Return a list of all sisters of this person. """
        return list(self._get_siblings(self.FEMALE))

    def children(self, gender=None):
        """ Return all children of this person, optionally filtered by gender.

        """
        if gender:
            return [child for child in self._children if
                    child.gender == gender]
        else:
            return self._children

    def is_direct_successor(self, person):
        """ Check if `person` is a child of this person. """
        return person.mother is self or person.father is self
