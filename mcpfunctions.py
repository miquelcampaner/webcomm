from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar

mesinici = 'JUL'
anyinici = '2021'
nummesos = '3'
stripinici = anyinici + '-' + mesinici + '-01'
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
    label = mesinici + str(datainici.year-2000) + '-'+ \
            datafin.strftime('%b%y').upper()
arraycalendari = []
for mesafegim in [0, int(nummesos)-1]:
    mesobserva = datainici+relativedelta(months=mesafegim)
    inicimes = mesobserva.replace(day=(calendar.monthrange(mesobserva.year,
                                                        mesobserva.month)[0]))
    finalmes = mesobserva.replace(day=(calendar.monthrange(mesobserva.year,
                                                        mesobserva.month)[1]))
    liquidacio =finalmes+relativedelta(days=5)

    mesopbservatobject = {'inicio': inicimes,
                          'vencimiento': finalmes,
                          'liquidacion': liquidacio}
    arraycalendari.append(mesopbservatobject)

print(arraycalendari)
