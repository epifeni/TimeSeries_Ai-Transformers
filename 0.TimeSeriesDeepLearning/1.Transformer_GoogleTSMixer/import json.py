import json
from pathlib import Path

nb_path = Path("/Users/tanojudawattage/1_tanoj/0.00_Cloud_Computing_and_Streaming_Tech/Python_Time_Series_Repo/0.TimeSeriesDeepLearning/0.Transformer_GoogleTSMixer/GoogleTSMixer.ipynb")

nb = json.loads(nb_path.read_text(encoding="utf-8"))

# Ensure top-level metadata.widgets has "state": {}
meta = nb.setdefault("metadata", {})
if "widgets" in meta:
    widgets = meta["widgets"]
    if not isinstance(widgets, dict):
        widgets = {}
        meta["widgets"] = widgets
    widgets.setdefault("state", {})

# Ensure each cell.metadata.widgets has "state": {} if widgets exists
for cell in nb.get("cells", []):
    cell_meta = cell.setdefault("metadata", {})
    if "widgets" in cell_meta:
        w = cell_meta["widgets"]
        if not isinstance(w, dict):
            w = {}
            cell_meta["widgets"] = w
        w.setdefault("state", {})

