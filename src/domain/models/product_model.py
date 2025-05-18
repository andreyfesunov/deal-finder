from pydantic import BaseModel


class ProductModel(BaseModel):
    name: str
    sub_category: str
    m_video_link: str
    m_video_price: float
    eldorado_link: str
    eldorado_price: float
    dns_link: str
    dns_price: float
    citylink_link: str
    citylink_price: float
    yandex_link: str
    yandex_price: float
