## Enrich track

This track is based on [es-enrich-testdata](https://github.com/mjmbischoff/es-enrich-testdata) which uses [open pagerank](https://www.domcop.com/openpagerank/what-is-openpagerank).

* Applied number to IP conversion as suggested in the original readme
* Removed illegal characters in "object_mappings.sort"
* Transformed the source data to a bulk-friendly JSON format (ignoring all entries that
  contained unrecognised / problematic characters and invalid IP addresses like "0";
  around 0.001% of the source data was lost due to this approach)

### Example Documents

Enrich source data
```json
{"rank":1,"domain":"facebook.com","openPageRank":10.0}
```

Data to be enriched
```json
{ "@timestamp": "2021-12-09T13:45:59.657", "clientIp": "93.210.130.35", "domain": "partners.propellerads.com" }
```

After the enrich policy runs as part of the ingest pipeline the document should look like so:
```json
{
  "@timestamp": "2021-12-09T13:45:59.657",
  "clientIp": "93.210.130.35",
  "domain": {
    "name": "partners.propellerads.com",
    "openpagerank": 210129
  }
}
```
### Parameters

This track allows to overwrite the following parameters with Rally 0.8.0+ using `--track-params`:

* `bulk_size` (default: 5000)
* `bulk_indexing_clients` (default: 8): Number of clients that issue bulk indexing requests.
* `ingest_percentage` (default: 100): A number between 0 and 100 that defines how much of the document corpus should be ingested.
* `number_of_replicas` (default: 0)
* `number_of_shards` (default: 3)
* `source_enabled` (default: true): A boolean defining whether the `_source` field is stored in the index.
* `index_settings`: A list of index settings. Index settings defined elsewhere (e.g. `number_of_replicas`) need to be overridden explicitly.
* `cluster_health` (default: "green"): The minimum required cluster health.

### Acknoledgements
- [open pagerank](https://www.domcop.com/openpagerank/what-is-openpagerank)
- [es-enrich-testdata](https://github.com/mjmbischoff/es-enrich-testdata) 
