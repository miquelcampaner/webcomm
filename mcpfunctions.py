from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar
import pandas as pd


def calcula_label(stringmes, stringany, nummesos):
    stripinici = stringany + '-' + stringmes + '-01'
    datainici = datetime.strptime(stripinici, '%Y-%b-%d')
    datafin = datainici+relativedelta(months=int(nummesos)-1)
    datafin =datafin.replace(day =(calendar.monthrange(datafin.year, datafin.month)[1]))
    if datainici.month == 1 and datafin.month == 12 and datainici.year == datafin.year:
        label = 'CAL' + str(datainici.year-2000)
    elif datainici.month == 1 and datafin.month == 6 and datainici.year == datafin.year:
        label = '1H' + str(datainici.year-2000)
    elif datainici.month == 7 and datafin.month == 12 and datainici.year == datafin.year:
        label = '2H' + str(datainici.year-2000)
    elif datainici.month == 1 and datafin.month == 3 and datainici.year == datafin.year:
        label = '1Q' + str(datainici.year-2000)
    elif datainici.month == 4 and datafin.month == 6 and datainici.year == datafin.year:
        label = '2Q' + str(datainici.year-2000)
    elif datainici.month == 7 and datafin.month == 9 and datainici.year == datafin.year:
        label = '3Q' + str(datainici.year-2000)
    elif datainici.month == 10 and datafin.month == 12 and datainici.year == datafin.year:
        label = '4Q' + str(datainici.year-2000)
    else:
        label = stringmes + str(datainici.year-2000) + '-'+ \
                datafin.strftime('%b%y').upper()
    return label


def calcula_dates(stringmes, stringany, nummesos):
    stripinici = stringany + '-' + stringmes + '-01'
    datainici = datetime.strptime(stripinici, '%Y-%b-%d')
    datafin = datainici+relativedelta(months=int(nummesos)-1)
    datafin =datafin.replace(day =(calendar.monthrange(datafin.year, datafin.month)[1]))
    datesarray = pd.date_range(start=datainici,
                               end=datafin,
                               freq='M')
    return datesarray
