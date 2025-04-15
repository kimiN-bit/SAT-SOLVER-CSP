from cnf import CNF


class CSP:
    def __init__(self, cnf: CNF, use_mcv=True, use_mrv=True, use_lcv=True):
        """
        Initializes a Constraint Satisfaction Problem (CSP) solver.

        Args:
            cnf (CNF): The Conjunctive Normal Form representation of the problem.
            use_mcv (bool): Whether to use Most Constraining Variable (MCV) or not. Defaults to True.
            use_mrv (bool): Whether to use Minimum Remaining Value (MRV) or not. Defaults to True.
            use_lcv (bool): Whether to use Least Constraining Value (LCV) or not. Defaults to True.
        """
        self.cnf = cnf
        self.use_mcv = use_mcv
        self.use_mrv = use_mrv
        self.use_lcv = use_lcv
        self.degree_variables = {}
        self.variables = {}
        self.assigned_variables = {}
        self.constraints = []
        self.var_constraints = {}

    def add_variable(self, variable, domain):
        """
        Adds a new variable with its given domain to the CSP solver.

        Args:
            variable (str): The name of the variable.
            domain ([bool]): The domain of the variable (in this case, [False, True]).
        """

    def add_constraint(self, constraint_function, variables):
        """
        Adds a new constraint to the CSP solver.

        Args:
            constraint_function (function): A function that takes two arguments (a clause and assigned values) and returns True if the constraint is satisfied, False otherwise.
            variables ([str]): The list of variables involved in the constraint.
        """

    def assign(self, variable, value):
        """
         Assigns a specific value to a variable.

         Args:
             variable (str): The name of the variable.
             value (bool): The assigned value for the variable.
         """

    def unassign(self, variable):
        """
        Unassigns a previously assigned value from a variable.

        Args:
            variable (str): The name of the variable.
        """

    def is_constraint_satisfied(self, constraint):
        """
        Checks if a specific constraint is satisfied given the current assignment of variables.

        Args:
            constraint: A tuple containing the constraint function and the list of involved variables.

        Returns:
            bool: True if the constraint is satisfied, False otherwise.
        """

    def is_consistent(self, variable, value):
        """
        Checks if assigning a specific value to a variable would violate any constraints.

        Args:
            variable (str): The name of the variable.
            value (bool): The assigned value for the variable.

        Returns:
            bool: True if the assignment does not violate any constraints, False otherwise.
        """

    def is_complete(self):
        """
        Checks if all variables have been assigned a value.

        Returns:
            bool: True if the assignment is complete, False otherwise.
        """

    def select_unassigned_variable(self):
        """
        Selects an unassigned variable to assign a value to next.

        If Most Constraining Variable (MCV) selection is used, it returns the most constrained variable.
        Otherwise, it simply returns the first unassigned variable.

        Returns:
            str: The name of the selected variable.
        """

    def solve(self):
        """
        Solves the CSP problem using backtracking search with MCV/LCV.

        Returns:
            tuple: A tuple containing the solution (a dictionary mapping variables to their assigned values)
                   and the best weight (the minimum weight of all possible solutions).
        """

    def minimum_remaining_value(self):
        """
            Returns the variable with the smallest domain size and a value that satisfies the given constraints.
        """

    def most_constraining_variable(self, unassigned_variables):
        """
        Returns the variable that would violate the most constraints when assigned a value.

        Args:
            variables ([str]): The list of variables to consider.

        Returns:
            str: The name of the most constraining variable.
        """

    def least_constraining_value(self, var):
        """
        Returns the value that would violate the fewest constraints when assigned to a variable.

        Args:
            variable (str): The name of the variable.

        Returns:
            bool: The least constraining value for the variable.
        """
