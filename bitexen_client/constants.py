class BuySellType():
    BUY = "B"
    SELL = "S"


class OrderStatus():
    NEW = "N"
    PARTIALFILLED = "P"
    FILLED = "F"
    CANCELED = "C"
    REJECTED = "R"


class OrderType():
    LIMIT_ORDER = "limit"
    STOP_ORDER = "stop"
    MARKET_ORDER = "market"
    CANCEL_ORDER = "cancel"
    CANCEL_ALL_ORDER = "cancel_all"
