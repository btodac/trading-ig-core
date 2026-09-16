import datetime as dt
import json
from pathlib import Path

from trading_ig_core import IGAccountDetails, IGSession, rest_api
from trading_ig_core.rest_api.base_rest_api_call import RestApiCall

DEFAULT_OUTPUT_DIR = Path(__file__).parent / "payloads" / "rest"

REQUESTS: list[RestApiCall] = [
	rest_api.FetchAccounts(),
	rest_api.FetchAccountActivityByDate(
		rest_api.FetchAccountActivityByDateArguments(
			fromDate=dt.datetime(year=2026, month=1, day=1, tzinfo=dt.UTC),
			toDate=dt.datetime.now(tz=dt.UTC),
		),
	),
	rest_api.CreateOpenPosition(
		rest_api.CreateOpenPositionData(
            currencyCode=currency_code,
            epic=trading_parameters.epic,
            direction="BUY",
            expiry="-",
            forceOpen=True,
            size=1,
            guaranteedStop=False,
            limitDistance=None,
            stopDistance=None,
            trailingStop=None,
            trailingStopIncrement=None,
		)
	),
	rest_api.CloseOpenPosition(
		rest_api.CloseOpenPositionData(
			dealId=position.dealId,
			direction="SELL",
			size=1,
		)
	),
	rest_api.FetchDealByDealReference(deal_reference='S'),
	rest_api.GetMarketDetailsV4(),
	

]


def capture_rest_payloads(
	session: IGSession,
	output_dir: Path = DEFAULT_OUTPUT_DIR,
) -> list[Path]:
	"""Write one raw REST API response JSON file for each endpoint factory."""
	output_dir.mkdir(parents=True, exist_ok=True)

	for request in REQUESTS:
		payload = session.request(request, return_raw=True)
		output_path = output_dir / f"{request.__class__}.json"
		with output_path.open("w", encoding="utf-8") as payload_file:
			json.dump(payload, payload_file, indent=2, sort_keys=True)
			payload_file.write("\n")

		
def main(account_details: IGAccountDetails):
	session = IGSession(account_details)
	capture_rest_payloads(session)


if __name__ == "__main__":
	from trading_ig_interface import get_account_manager

	account_manager = get_account_manager()
	account = account_manager.get_account("DEMO")
	
	main(account)