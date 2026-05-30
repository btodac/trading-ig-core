import logging

from lightstreamer.client import LightstreamerClient  # Subscription, ClientListener

from trading_ig.igsession import IGSession
from trading_ig.rest_api.accounts import GetSession

logger = logging.getLogger(__name__)


class IGStreamService(LightstreamerClient):
    def __init__(self, ig_session: IGSession):
        session_details = ig_session.request(GetSession(fetch_session_tokens=False))
        
        lightstreamerEndpoint = session_details["lightstreamerEndpoint"]

        cst = ig_session.session.headers["CST"]
        xsecuritytoken = ig_session.session.headers["X-SECURITY-TOKEN"]
        ls_password = f"CST-{cst}|XST-{xsecuritytoken}" 

        # Establishing a new connection to Lightstreamer Server
        logger.info("Starting connection with %s", self.lightstreamerEndpoint)
        
        super.__init__(lightstreamerEndpoint)
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
