import json
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
EXAMPLE = ROOT / "examples" / "01-mapfile-basics"


class MapfileContractTests(unittest.TestCase):
    def test_mapfile_has_wms_and_ogr_layer_contract(self):
        mapfile = (EXAMPLE / "demo.map").read_text(encoding="utf-8")
        for token in (
            'NAME "zqm_mapserver_demo"',
            '"wms_title" "ZQM MapServer Cookbook Demo"',
            '"wms_srs" "EPSG:4326 EPSG:3857"',
            'CONNECTIONTYPE OGR',
            'CONNECTION "sample_points.geojson"',
            'DATA "sample_points"',
            'NAME "sample_points"',
        ):
            with self.subTest(token=token):
                self.assertIn(token, mapfile)

    def test_geojson_fixture_is_valid_and_has_two_epsg4326_points(self):
        data = json.loads((EXAMPLE / "data" / "sample_points.geojson").read_text(encoding="utf-8"))
        self.assertEqual(data["type"], "FeatureCollection")
        self.assertEqual(data["crs"]["properties"]["name"], "urn:ogc:def:crs:OGC:1.3:CRS84")
        self.assertEqual(len(data["features"]), 2)
        for feature in data["features"]:
            self.assertEqual(feature["geometry"]["type"], "Point")
            self.assertIn("id", feature["properties"])


    def test_readme_pattern_table_has_consistent_columns(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        section = readme.split("## Patterns", 1)[1].split("## Repository layout", 1)[0]
        rows = [line for line in section.splitlines() if line.startswith("|")]
        self.assertEqual(len(rows), 6)
        self.assertTrue(all(len(row.strip("|").split("|")) == 4 for row in rows))

if __name__ == "__main__":
    unittest.main()
