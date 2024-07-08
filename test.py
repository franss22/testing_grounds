from typing import Sequence
from chlib.DatabaseConnection import DatabaseConnection as db

from tipos_bdd import GenCometido


conn = db.fromConf({"": ""})

res: Sequence[int] = conn.getRowsByCol("", "", "")
