from address import Address
from mailing import Mailing

to_addr = Address("173014", "Великий Новгород", "Студенческая", "13", "1")
from_addr = Address("606002", "Дзержинск", "Сухаренко", "22", "3")

mail = Mailing(to_address=to_addr, from_address=from_addr, track="CA123456789RU", cost=1452.0)

track_info = f"отправление {mail.track} из "
from_info = f"{from_addr.format_address()}"
to_info = f" в {to_addr.format_address()}"
cost_info = f". Стоимость {mail.cost} рублей."
print(track_info + from_info + to_info + cost_info)