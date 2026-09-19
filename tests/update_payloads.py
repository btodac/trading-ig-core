import datetime as dt
import json
from pathlib import Path

from trading_ig_core import IGAccountDetails, IGSession, rest_api
from trading_ig_core.rest_api.base_rest_api_call import RestApiCall

DEFAULT_OUTPUT_DIR = Path(__file__).parent / "payloads" / "rest"

EPIC = "IX.D.NASDAQ.IFS.IP"

REQUESTS: list[RestApiCall] = [
    rest_api.FetchAccounts(),
    rest_api.FetchAccountActivityByDate(
        rest_api.FetchAccountActivityByDateArguments(
            fromDate=dt.datetime(year=2026, month=1, day=1, tzinfo=dt.UTC),
            toDate=dt.datetime.now(tz=dt.UTC),
        ),
    ),
    rest_api.CloseOpenPosition(
        rest_api.CloseOpenPositionData(
            dealId=position.dealId,
            direction="SELL",
            size=1,
        )
    ),
    rest_api.FetchDealByDealReference(deal_reference='S'),
    ,
    

]

def _request_and_write_json(session: IGSession, request: RestApiCall):
    payload = session.request(request, return_raw=True)
    write_payload_to_JSON(request.__class__, payload)
    return request.process_payload(payload)


def get_market_details(session: IGSession, epic: str) -> rest_api.MarketDetailsV4:
    return session.request(rest_api.GetMarketDetailsV4(epic))


def _trading_payloads(session: IGSession):
    details_call = rest_api.GetMarketDetailsV4(EPIC)
    details: rest_api.MarketDetailsV4 = _request_and_write_json(session, details_call)
    open_position_call = rest_api.CreateOpenPosition(
        rest_api.CreateOpenPositionData(
            currencyCode=details.instrument.currencies[0].code,
            epic=details.instrument.epic,
            direction=rest_api.Direction.BUY,
            expiry=details.instrument.expiry,
            forceOpen=True,
            size=1,
            guaranteedStop=False,
            limitDistance=None,
            stopDistance=None,
            trailingStop=None,
            trailingStopIncrement=None,
        )
    )
    deal_reference: str = _request_and_write_json(session, open_position_call)

    confirmation_call = rest_api.FetchDealByDealReference(deal_reference)
    confirmation: rest_api.DealConfirmation = _request_and_write_json(session, confirmation_call)

    close_position_call = rest_api.CloseOpenPosition(
        rest_api.CloseOpenPositionData(
            dealId=confirmation.dealId,
            direction=rest_api.Direction.SELL,
            size=confirmation.size,
        )
    )
    deal_reference = _request_and_write_json(session, close_position_call)



def write_payload_to_JSON(request_name: str, payload: dict):
    DEFAULT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = DEFAULT_OUTPUT_DIR / f"{request_name}.json"
    with output_path.open("w", encoding="utf-8") as payload_file:
            json.dump(payload, payload_file, indent=2, sort_keys=True)
            payload_file.write("\n")


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