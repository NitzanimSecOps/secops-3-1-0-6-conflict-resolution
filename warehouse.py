from pathlib import Path

from warehouse_setup import WarehouseSetup
from warehouse_log import WarehouseLog
from inventory_db import InventoryDB
from integrity_checker import IntegrityChecker
from permission_auditor import PermissionAuditor

class Warehouse:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.setup = WarehouseSetup(root)
        self.log = WarehouseLog(root / "logs" / "warehouse.log")
        self.db = InventoryDB(root / "inventory" / "inventory.db")
        self.integrity = IntegrityChecker(root)
        self.permissions = PermissionAuditor(root)
