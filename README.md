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

**Status:** Active, public — seeding. Pattern passes land in follow-up work from fleet-verified setups; the tables below list what is planned, not what is already written.

**What this repository is:** MapServer patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Platform engineers who want a lean, fast map server next to GeoServer.

## Prerequisites

- MapServer 5.2.0 via MS4W
- PostGIS-backed Postgres for the layer pass (see postgis-cookbook)
- Bash

## Patterns (planned)

| # | Example | What it will demonstrate |
|---|---------|--------------------------|
| 01 | `01-mapfile-basics` | Writing a mapfile: layers, classes, and projections |
| 02 | `02-wms-service` | Serving WMS and validating GetCapabilities |
| 03 | `03-postgis-layer` | PostGIS layers with connection pooling notes |
| 04 | `04-performance` | Tiling, caching, and shapefile-vs-database trade-offs |

## Repository layout

```text
mapserver-cookbook/
├── examples/          # pattern passes, landing in follow-up work
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: the first two table rows
- Second pass: the remaining rows, from fleet-verified setups

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [geoserver-cookbook](https://github.com/ZQM-Computing/geoserver-cookbook) — Publishing, styling, federation, and securing OGC services
- [postgis-cookbook](https://github.com/ZQM-Computing/postgis-cookbook) — Spatial indexing, joins & KNN, SRID management, vector tiles
- [martin-cookbook](https://github.com/ZQM-Computing/martin-cookbook) — Vector tiles from PostGIS, function sources, tile serving
