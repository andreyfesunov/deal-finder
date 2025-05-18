class ProductModel:
    def __init__(
        self,
        name: str,
        sub_category: str,
        m_video_link: str,
        m_video_price: float,
        eldorado_link: str,
        eldorado_price: float,
        dns_link: str,
        dns_price: float,
        citylink_link: str,
        citylink_price: float,
        yandex_link: str,
        yandex_price: float,
    ):
        self.__name = name
        self.__sub_category = sub_category
        self.__m_video_link = m_video_link
        self.__m_video_price = m_video_price
        self.__eldorado_link = eldorado_link
        self.__eldorado_price = eldorado_price
        self.__dns_link = dns_link
        self.__dns_price = dns_price
        self.__citylink_link = citylink_link
        self.__citylink_price = citylink_price
        self.__yandex_link = yandex_link
        self.__yandex_price = yandex_price

    @property
    def name(self) -> str:
        return self.__name

    @property
    def sub_category(self) -> str:
        return self.__sub_category

    @property
    def m_video_link(self) -> str:
        return self.__m_video_link

    @property
    def m_video_price(self) -> float:
        return self.__m_video_price

    @property
    def eldorado_link(self) -> str:
        return self.__eldorado_link

    @property
    def eldorado_price(self) -> float:
        return self.__eldorado_price

    @property
    def dns_link(self) -> str:
        return self.__dns_link

    @property
    def dns_price(self) -> float:
        return self.__dns_price

    @property
    def citylink_link(self) -> str:
        return self.__citylink_link

    @property
    def citylink_price(self) -> float:
        return self.__citylink_price

    @property
    def yandex_link(self) -> str:
        return self.__yandex_link

    @property
    def yandex_price(self) -> float:
        return self.__yandex_price
