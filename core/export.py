import csv
import os
import re

from qgis.PyQt.QtCore import QDate, QDateTime, QTime
from qgis.core import QgsVectorLayer


def _format_value(val):
    if val is None:
        return ""
    if isinstance(val, QDateTime):
        return val.toString("yyyy-MM-dd HH:mm:ss") if val.isValid() else ""
    if isinstance(val, QDate):
        return val.toString("yyyy-MM-dd") if val.isValid() else ""
    if isinstance(val, QTime):
        return val.toString("HH:mm:ss") if val.isValid() else ""
    return val


def _safe_filename(name: str) -> str:
    """Turn a layer name into a safe filename (no path separators, etc.)."""
    return re.sub(r'[^\w\s\-()]', '_', name).strip()


def export_results_to_csv(
    result_layers: list[QgsVectorLayer],
    output_dir: str,
) -> list[str]:
    """Export each result layer as a separate CSV file inside output_dir.

    Creates output_dir if it doesn't exist. Returns the list of written file paths.
    """
    os.makedirs(output_dir, exist_ok=True)

    written = []
    for layer in result_layers:
        layer_name = layer.name().removesuffix(" — résultat")
        filename = _safe_filename(layer_name) + ".csv"
        filepath = os.path.join(output_dir, filename)

        field_names = [field.name() for field in layer.fields()]

        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(field_names)
            for feat in layer.getFeatures():
                row = [_format_value(v) for v in feat.attributes()]
                writer.writerow(row)

        written.append(filepath)

    return written
