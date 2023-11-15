# Python Steam 市场自动购买
本项目基于 steampy 开发
## 安装依赖
pip 安装 [steampy](https://github.com/bukson/steampy) 需要 python 3.8 或更新
```
pip install steampy
```
## Steam API 获取
[点击此处](https://steamcommunity.com/dev/apikey)获取你的Steam API
## 使用
```
python autobuy.py
```
## Steam 验证器
[获取Steam验证](https://github.com/SteamTimeIdler/stidler/wiki/Getting-your-%27shared_secret%27-code-for-use-with-Auto-Restarter-on-Mobile-Authentication)(英文)
### Android Root 设备
使用MT管理器或其他文件浏览软件访问以下目录提取你的 Steam 验证
```
/data/data/com.valvesoftware.android.steam.community/f/Steamguard-STEAMID64
```
### Windows 使用 Steam Desktop Authenticator(SDA)
添加SDA之前需要移除手机验证器

[Steam Desktop Authenticator(SDA)](https://github.com/Jessecar96/SteamDesktopAuthenticator)
## 货币

| Currency class | Description                 |
| ---            | ---                         |
| Currency.USD   | United States Dollar        |
| Currency.GBP   | United Kingdom Pound        |
| Currency.EURO  | European Union Euro         |
| Currency.CHF   | Swiss Francs                |
| Currency.RUB   | Russian Rouble              |
| Currency.PLN   | Polish Złoty                |
| Currency.BRL   | Brazilian Reals             |
| Currency.JPY   | Japanese Yen                |
| Currency.NOK   | Norwegian Krone             |
| Currency.IDR   | Indonesian Rupiah           |
| Currency.MYR   | Malaysian Ringgit           |
| Currency.PHP   | Philippine Peso             |
| Currency.SGD   | Singapore Dollar            |
| Currency.THB   | Thai Baht                   |
| Currency.VND   | Vietnamese Dong             |
| Currency.KRW   | South Korean Won            |
| Currency.TRY   | Turkish Lira                |
| Currency.UAH   | Ukrainian Hryvnia           |
| Currency.MXN   | Mexican Peso                |
| Currency.CAD   | Canadian Dollars            |
| Currency.AUD   | Australian Dollars          |
| Currency.NZD   | New Zealand Dollar          |
| Currency.CNY   | Chinese Renminbi (yuan)     |
| Currency.INR   | Indian Rupee                |
| Currency.CLP   | Chilean Peso                |
| Currency.PEN   | Peruvian Sol                |
| Currency.COP   | Colombian Peso              |
| Currency.ZAR   | South African Rand          |
| Currency.HKD   | Hong Kong Dollar            |
| Currency.TWD   | New Taiwan Dollar           |
| Currency.SAR   | Saudi Riyal                 |
| Currency.AED   | United Arab Emirates Dirham |
| Currency.SEK   | Swedish Krona               |
| Currency.ARS   | Argentine Peso              |
| Currency.ILS   | Israeli New Shekel          |
| Currency.BYN   | Belarusian Ruble            |
| Currency.KZT   | Kazakhstani Tenge           |
| Currency.KWD   | Kuwaiti Dinar               |
| Currency.QAR   | Qatari Riyal                |
| Currency.CRC   | Costa Rican Colón           |
| Currency.UYU   | Uruguayan Peso              |
| Currency.BGN   | Bulgarian Lev               |
| Currency.HRK   | Croatian Kuna               |
| Currency.CZK   | Czech Koruna                |
| Currency.DKK   | Danish Krone                |
| Currency.HUF   | Hungarian Forint            |
| Currency.RON   | Romanian Leu                |

