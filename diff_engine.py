
import json

def load_schema(path):
    with open(path) as f:
        return json.load(f)

def compare(old_path, new_path):
    old = load_schema(old_path)
    new = load_schema(new_path)

    changes = []

    for table in old:
        if table in new:
            old_cols = old[table]
            new_cols = new[table]

            for col in old_cols:
                if col not in new_cols:
                    changes.append({"type":"removed_column","table":table,"column":col})

            for col in new_cols:
                if col not in old_cols:
                    changes.append({"type":"added_column","table":table,"column":col})

    return changes
