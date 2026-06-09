import logging

from lightstreamer.client import LightstreamerClient  # Subscription, ClientListener

from trading_ig.rest_api.responses.login import SessionDetailsResponse

logger = logging.getLogger(__name__)


class IGStreamService(LightstreamerClient):
    def __init__(self, session_details: SessionDetailsResponse, ls_password: str):
        # Establishing a new connection to Lightstreamer Server
        logger.info("Starting connection with %s", session_details["lightstreamerEndpoint"])

        super.__init__(session_details["lightstreamerEndpoint"])
        self.connectionDetails.setUser(session_details["accountId"])
        self.connectionDetails.setPassword(ls_password)

    def __del__(self):
        self.disconnect()
        super().__del__()

    def unsubscribe_all(self):
        for sub in self.getSubscriptions():
            self.unsubscribe(sub)

    def disconnect(self):
        self.unsubscribe_all()
        super().disconnect()
