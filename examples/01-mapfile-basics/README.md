# Minimal MapServer mapfile with a GeoJSON layer

This pattern defines a small WMS-ready mapfile with a single point layer backed by a local GeoJSON fixture. It is intended as a starting point for a local MapServer/MS4W deployment; it is not a public endpoint and does not configure production authentication, TLS, or request limits.

## Prerequisites

- MapServer through MS4W or another compatible installation
- `mapserv`/CGI configured by the local administrator
- No external data download is required; `data/sample_points.geojson` is included

## Files

- `demo.map` — map extent, WMS metadata, and OGR-backed point layer
- `data/sample_points.geojson` — two synthetic points in EPSG:4326

## Validate

Review the `SHAPEPATH`, `CONNECTION`, layer name, and WMS metadata for your installation. Paths are relative to the mapfile directory. To test through a local CGI endpoint, request `SERVICE=WMS&REQUEST=GetCapabilities&VERSION=1.3.0` and verify that `sample_points` is listed. Keep the mapfile and data outside publicly writable directories.

## Validation boundary

CI checks mapfile contract fields and the GeoJSON fixture structure. It does not run MapServer or prove that a particular MS4W installation can serve the file. Validate against the target MapServer build before deployment.
