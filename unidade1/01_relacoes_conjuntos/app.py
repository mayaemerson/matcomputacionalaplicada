from typing import Set

class AccessControlSystem:
    """
    Represents an access control system using set theory relations
    and mapping functions.
    """
    def __init__(self, users: Set[str], resources: Set[str]):
        self.users = users
        self.resources = resources
        # Relation P is a subset of U x R, represented as a set of tuples (user, resource)
        self.permissions = set()

    def grantPermission(self, user: str, resource: str) -> None:
        """
        Grants a user access to a resource.
        Mathematical operation: P = P U {(user, resource)}
        """
        if user in self.users and resource in self.resources:
            self.permissions.add((user, resource))

    def revokePermission(self, user: str, resource: str) -> None:
        r"""
        Revokes a user's access to a resource.
        Mathematical operation: P = P \ {(user, resource)}
        """
        self.permissions.discard((user, resource))

    def getAuthorizedResources(self, user: str) -> Set[str]:
        """
        Represents the mapping function f: U -> P(R).
        Returns the set of resources a user has access to.
        """
        if user not in self.users:
            return set()
        return {r for (u, r) in self.permissions if u == user}

    def hasAccess(self, user: str, resource: str) -> bool:
        """
        Checks membership of the pair in the relation: (user, resource) in P.
        """
        return (user, resource) in self.permissions


if __name__ == "__main__":
    # Define sets U (users) and R (resources)
    systemUsers = {"u1", "u2", "u3"}
    systemResources = {"r1", "r2", "r3"}

    # Initialize the Access Control System
    authSystem = AccessControlSystem(systemUsers, systemResources)

    # 1. Grant permissions (Populate Relation P)
    authSystem.grantPermission("u1", "r1")
    authSystem.grantPermission("u1", "r2")
    authSystem.grantPermission("u2", "r2")

    # 2. Check individual access
    print("--- Access Checks ---")
    print(f"Can u1 access r1? {authSystem.hasAccess('u1', 'r1')}")
    print(f"Can u2 access r1? {authSystem.hasAccess('u2', 'r1')}")
    print(f"Can u3 access r2? {authSystem.hasAccess('u3', 'r2')}")

    # 3. Map user to authorized resources: f(u)
    print("\n--- Authorized Resources Mapping f(u) ---")
    for user in sorted(list(systemUsers)):
        authorized = authSystem.getAuthorizedResources(user)
        print(f"f({user}) = {authorized}")

    # 4. Revoke a permission and check again
    print("\n--- Revoking Permission (u1, r2) ---")
    authSystem.revokePermission("u1", "r2")
    print(f"f(u1) after revocation = {authSystem.getAuthorizedResources('u1')}")
