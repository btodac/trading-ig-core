import json
from collections.abc import Callable, Mapping
from pathlib import Path
from typing import Any

from trading_ig_core import IGAccountDetails, IGSession
from trading_ig_core.rest_api import FetchAccounts, GetSession
from trading_ig_core.rest_api.base_rest_api_call import RestApiCall

EndpointFactory = Callable[[], RestApiCall]
RawPayload = dict[str, Any] | None
DEFAULT_OUTPUT_DIR = Path(__file__).parent / "payloads" / "rest"
DEFAULT_ENDPOINT_FACTORIES: dict[str, EndpointFactory] = {
	"fetch_accounts": FetchAccounts,
	"get_session": GetSession,
}


def capture_rest_payloads(
	session: IGSession,
	endpoint_factories: Mapping[str, EndpointFactory] = DEFAULT_ENDPOINT_FACTORIES,
	output_dir: Path = DEFAULT_OUTPUT_DIR,
) -> list[Path]:
	"""Write one raw REST API response JSON file for each endpoint factory."""
	output_dir.mkdir(parents=True, exist_ok=True)
	written_files: list[Path] = []

	for name, endpoint_factory in endpoint_factories.items():
		output_path = output_dir / f"{name}.json"

		def write_payload(
			_call: RestApiCall,
			payload: RawPayload,
			output_path: Path = output_path,
		) -> None:
			with output_path.open("w", encoding="utf-8") as payload_file:
				json.dump(payload, payload_file, indent=2, sort_keys=True)
				payload_file.write("\n")

		session.request(endpoint_factory(), return_raw=True)
		written_files.append(output_path)

	return written_files


def main() -> None:
	# Get account details from credentials.toml and create a live session.
	account_details = IGAccountDetails()
	session = IGSession(account_details)
	capture_rest_payloads(session)


if __name__ == "__main__":
	main()