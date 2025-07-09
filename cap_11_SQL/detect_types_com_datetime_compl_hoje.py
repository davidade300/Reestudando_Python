import datetime
import sqlite3


def adapt_date_iso(val):
    """Adapt datetime.date to ISO 8601 date."""
    return val.isoformat()


def adapt_datetime_iso(val):
    """Adapt datetime.datetime to timezone-naive ISO 8601 date."""
    return val.isoformat()


def adapt_datetime_epoch(val):
    """Adapt datetime.datetime to Unix timestamp."""
    return int(val.timestamp())


sqlite3.register_adapter(datetime.date, adapt_date_iso)
sqlite3.register_adapter(datetime.datetime, adapt_datetime_iso)
sqlite3.register_adapter(datetime.datetime, adapt_datetime_epoch)


def convert_date(val):
    """Convert ISO 8601 date to datetime.date object."""
    return datetime.date.fromisoformat(val.decode())


def convert_datetime(val):
    """Convert ISO 8601 datetime to datetime.datetime object."""
    return datetime.datetime.fromisoformat(val.decode())


def convert_timestamp(val):
    """Convert Unix epoch timestamp to datetime.datetime object."""
    return datetime.datetime.fromtimestamp(int(val))


sqlite3.register_converter("date", convert_date)
sqlite3.register_converter("datetime", convert_datetime)
sqlite3.register_converter("timestamp", convert_timestamp)

hoje = datetime.date(2024, 1, 1)
hoje60dias = hoje + datetime.timedelta(days=420)
with sqlite3.connect(
    "brasil.db", detect_types=sqlite3.PARSE_DECLTYPES
) as conexão:
    conexão.row_factory = sqlite3.Row
    for feriado in conexão.execute(
        "select * from feriados where data >= ? and data <= ?",
        (hoje, hoje60dias),
    ):
        print(f"{feriado['data']:%d/%m} {feriado['descrição']}")
