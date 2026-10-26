# MapServer Cookbook

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Computing — Geospatial Engineering & Scientific Computing</strong><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A **MapServer cookbook** for fast OGC services from mapfiles, via MS4W. Patterns are drawn from the ZQM fleet's MapServer 5.2.0 installs via MS4W on all three Windows nodes. It is intended for Platform engineers who want a lean, fast map server next to GeoServer. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public — first mapfile pattern written with a local synthetic GeoJSON fixture. CI validates the mapfile contract and fixture; serving behavior still requires a MapServer/MS4W runtime check.

**What this repository is:** MapServer patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Platform engineers who want a lean, fast map server next to GeoServer.

## Prerequisites

- MapServer 5.2.0 via MS4W
- PostGIS-backed Postgres for the layer pass (see postgis-cookbook)
- Bash

## Patterns

| # | Example | Status | What it demonstrates |
|---|---------|--------|---------------------|
| 01 | [01-mapfile-basics](examples/01-mapfile-basics/README.md) | Written; runtime check pending | Minimal WMS-ready mapfile with an OGR GeoJSON point layer |
| 02 | `02-wms-service` | Planned | Serving WMS and validating GetCapabilities |
| 03 | `03-postgis-layer` | Planned | PostGIS layers with connection pooling notes |
| 04 | `04-performance` | Planned | Tiling, caching, and shapefile-vs-database trade-offs |

## Repository layout

```text
mapserver-cookbook/
├── examples/01-mapfile-basics/  # mapfile and synthetic GeoJSON fixture
├── tests/             # mapfile/fixture contract tests
├── .github/workflows/ # CI
├── README.md
└── LICENSE
```

## Roadmap

- Validate `demo.map` with the target MS4W/MapServer build and confirm `GetCapabilities` lists `sample_points`.
- Add WMS image requests and PostGIS layers after local service configuration and access controls are verified.

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [geoserver-cookbook](https://github.com/ZQM-Computing/geoserver-cookbook) — Publishing, styling, federation, and securing OGC services
- [postgis-cookbook](https://github.com/ZQM-Computing/postgis-cookbook) — Spatial indexing, joins & KNN, SRID management, vector tiles
- [martin-cookbook](https://github.com/ZQM-Computing/martin-cookbook) — Vector tiles from PostGIS, function sources, tile serving
