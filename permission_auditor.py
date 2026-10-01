from pathlib import Path


class PermissionAuditor:
    def __init__(self, root: Path):
        pass

    def audit(self) -> dict[str, list[str]]:
        pass

    def harden(self) -> None:
        pass
