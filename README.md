# UDCT v7.12 Post-registration Results

**Anisotropy and Screening-Length Boundaries of Signed Jeans Solutions in Hydrus I**

Won Shik Paik — Independent Researcher, Auckland, New Zealand. 11 October 2026 (Auckland).

## Records

- Results repository: https://github.com/wspaik5/UDCT_v7.12_Postregistration_Results
- Results DOI: https://doi.org/10.5281/zenodo.23296444 **Reserved; registered when this results upload is published.**
- Public preregistration: https://doi.org/10.5281/zenodo.23280972
- Registered source: https://github.com/wspaik5/UDCT_v7.12_Preregistration_Jeans_Transitions
- Motivating v7.11 results: https://doi.org/10.5281/zenodo.23263099

## Completed experiment

The frozen protocol was executed once after observed public preregistration. Fixed design: Hydrus I unsoftened tapered cusp; five screened laws; screening lengths 1, 1.2, 1.5, 2, 2.5, 3 pc; eleven constant anisotropies beta=0 to 0.5; three QUMOND controls; three grids and two inner limits.

| Fixed cases | N | P | I | Total |
| --- | ---: | ---: | ---: | ---: |
| Screened models | 274 | 23 | 33 | 330 |
| QUMOND controls | 0 | 25 | 8 | 33 |
| Total | 274 | 48 | 41 | 363 |

All screened cases at 2.5 and 3 pc are N. Some shorter-length, higher-anisotropy settings retain P candidates. A-f1/2 has no P case. Of 575 adjacent intervals, 24 have strict raw sign changes: 12 stop at endpoint numerical margins and 12 at midpoint margins. None reaches the registered coordinate precision. These stops are completed prescribed decisions, not resource failures.

Fixed counts: 198 fields and 2,178 pressure records. With 18 adaptive cases: 246 fields, 2,286 pressure records, 381 decisions. All 246 isotropic reproduction gates passed. Filter case_decisions.csv to stage1/stage2 for primary counts.

## Interpretation, progress and future work

N means incompatibility with the specified stationary Jeans closure. P is a positive sampled second-moment candidate; it does not prove a nonnegative distribution function, equilibrium, stability or agreement with observations. I retains numerical uncertainty. The advance is a denser, reproducible conditional sign map and a model comparison with explicitly unresolved boundaries. No exact critical coordinate, universal Hessian threshold or general MOND exclusion is established. Changing beta does not change the field/Hessian at fixed model and length.

Future directions in the PDF include predefined resolution checks, distribution-function admissibility, stability and observational/cross-target checks. They were not executed here. A new public specification should precede confirmatory follow-up; no criteria were relaxed to obtain favorable cases.

## Contents and upload size

The linked PDF, this README, the post-registration launcher, all four unchanged scientific Python sources, pinned requirements, case/bracket CSVs, console log, original registration-evidence sidecar, later verified public API response and SHA256SUMS.txt are included in the lightweight ZIP. Extract the ZIP before uploading its files to GitHub.

**The full original compressed result and incremental journal are retained separately and are excluded from this small code-and-tables ZIP.** It is not a full raw-data archive. This prevents another approximately 49 MB mobile upload. The original full-result SHA-256 is:

`2ed68841f3ada9427b9200e5f8c05f0c743af5dc60c131306643ed3e84b7be54`

## Reproduce the registered calculation

Use Python 3.12 (original execution: 3.12.14). Keep every Python file below in the same folder:

- UDCT_v7_12_Postregistration_Run.py (convenience launcher)
- UDCT_v7_12_Preregistration_Jeans_Transition.py (unchanged registered runner)
- UDCT_v7_11_Preregistration_Anisotropic_Jeans.py
- UDCT_v7_10_Postregistration_run.py
- UDCT_v7_06_Hessian_Term_Sign_Audit_reproduce.py

```bash
python -m pip install -r requirements.txt
python UDCT_v7_12_Postregistration_Run.py --selftest
python UDCT_v7_12_Postregistration_Run.py --run \
  --registration-url https://doi.org/10.5281/zenodo.23280972 \
  --registration-published-utc 2026-10-10T13:24:19Z \
  --confirm-public-registration \
  --output UDCT_v7_12_reproduction.json.gz
```

The registration URL in this command is deliberately the **preregistration DOI**, not the results DOI. The timestamp is the original observed-public-status upper bound, retained to reproduce historical invocation; it is not an exact publication-button timestamp. Use a new output path: the runner refuses overwrites. Reruns have different timing/provenance bytes, so their full-file checksum need not equal the original; compare scientific values and decisions instead.

## Timing and provenance

Production started 2026-10-10T13:24:40.435703Z (11 October, 02:24:40 Auckland). Calculations completed at 13:25:01.785279Z; final installation at 13:25:11.985649Z. Initial network checks failed; screenshots supported public status and the CLI used 13:24:19Z as an upper bound. This departure from the original timestamp instruction remains disclosed; raw provenance has not been rewritten.

A later successful public API retrieval confirmed published/done/submitted=true for preregistration record 23280972. API created=2026-10-10T12:09:24.904006Z (11 October, 01:09:24.904006 Auckland), modified=2026-10-10T12:09:27.242302Z. Production began 1h15m15.531697s after recorded creation. The created field is record creation, not a separately exposed publication-button event; publication_date=2026-10-11 has no clock time.

API: https://zenodo.org/api/records/23280972

The original registration_evidence.json records the initial verification situation; preregistration_api_verified.json supplies the later supplement. Historical preparation-status text in unchanged scientific sources describes preparation, not the status of this completed run. All four scientific source files retain their registered hashes; the launcher only delegates execution.
