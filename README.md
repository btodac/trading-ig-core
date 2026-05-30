# Trading IG 3

This package started life as a fork of `trading_ig` but has since become its own beast with little of the original package present.
It provides the same functionality as `trading_ig`, but does so with an emphasis on python 3 features.
The main differences between the packages is a streamlined parent object (`IGService` -> `IGSession`) using an OOP style REST and Lightstreamer client interfaces.
This pattern involves converting the requests and subscriptions into classes that can be instantiated by the user as needed. 
This helps to keep the logic and the requests seperate, making it easier to follow the logic.
