import hashlib
import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")
ACCESS_LOG_PATH = Path("/app/access.log")

# Ground truth for the fixed access.log baked into the image. Hardcoded (not
# recomputed at verify time) so an agent can't pass by editing its own copy
# of the input log to match whatever it wrote.
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"
EXPECTED_KEYS = {"total_requests", "unique_ips", "top_path"}
EXPECTED_ACCESS_LOG_SHA256 = "e83c0cb8dd9c33cbe0954cc038bd0ff90834cf48747e257d931dce5b2408d38e"


def _load_report():
    assert REPORT_PATH.exists(), "no report.json found at /app/report.json"
    return json.loads(REPORT_PATH.read_text())


def test_criterion_1_report_exists_and_valid_json():
    """Criterion 1: /app/report.json exists and contains valid JSON."""
    data = _load_report()
    assert isinstance(data, dict), "report.json is not a JSON object"


def test_criterion_2_exact_keys():
    """Criterion 2: the JSON object has exactly the required keys, no others."""
    data = _load_report()
    assert set(data.keys()) == EXPECTED_KEYS


def test_criterion_3_total_requests_correct():
    """Criterion 3: total_requests equals the true number of requests in access.log."""
    data = _load_report()
    assert data["total_requests"] == EXPECTED_TOTAL_REQUESTS


def test_criterion_4_unique_ips_correct():
    """Criterion 4: unique_ips equals the true count of distinct client IPs."""
    data = _load_report()
    assert data["unique_ips"] == EXPECTED_UNIQUE_IPS


def test_criterion_5_top_path_correct():
    """Criterion 5: top_path equals the true most-requested path."""
    data = _load_report()
    assert data["top_path"] == EXPECTED_TOP_PATH


def test_criterion_6_access_log_unmodified():
    """Criterion 6: /app/access.log was left unmodified."""
    digest = hashlib.sha256(ACCESS_LOG_PATH.read_bytes()).hexdigest()
    assert digest == EXPECTED_ACCESS_LOG_SHA256
