from datetime import date, datetime

DATE_FORMATS = ["%Y-%m-%d", "%d-%m-%Y", "%Y/%m/%d", "%d/%m/%Y"]


def str_to_date(date_str: str | date):
    if isinstance(date_str, date):
        return date_str
    for date_format in DATE_FORMATS:
        try:
            return datetime.strptime(date_str, date_format).date()
        except ValueError:
            pass
    return None
