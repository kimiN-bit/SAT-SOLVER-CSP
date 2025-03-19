class CNF:
    def __init__(self, variables, hard_clauses, soft_clauses):
        """
        Initializes a Conjunctive Normal Form (CNF) object.

        Args:
            variables (list): List of variable names.
            hard_clauses (list): List of hard clauses.
            soft_clauses (list): List of soft clauses with weights at the end.
        """
        self.hard_clauses = hard_clauses
        self.soft_clauses = soft_clauses
        self.variables = variables

    def evaluate_clause(self, clause, assignments):
        """Checks if a single clause is satisfied given the assignments."""

    def evaluate_negation(self, clause, assignments):
        """Checks if a negated variable assignment is satisfied."""

    def calculate_weight(self, assignments):
        """
        Calculates the weight of a given set of assignments.

        Args:
            assignments (dict): Assignments where keys are variable names and values are boolean.

        Returns:
            int: The sum of weights for all satisfied soft clauses.
        """
