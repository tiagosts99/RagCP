from django.db import connection
from django.shortcuts import render, redirect
from django.views import View



def RMTView(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT value FROM acc_reg_num WHERE account_id = %s AND `key` = '#RMTPOINTS'", [request.user.id])
        purchases = cursor.fetchone()

    if purchases:
        purchases = purchases[0]
    else:
        purchases = 0

    if request.method == 'POST':
        rmtpoints = int(request.POST.get('rmt', 0))
        updated_purchases = purchases + rmtpoints
        with connection.cursor() as cursor:
            cursor.execute("UPDATE acc_reg_num SET value = %s WHERE account_id = %s AND `key` = '#RMTPOINTS'", [updated_purchases, request.user.id])
            connection.commit()  # Salva as alterações no banco de dados

        return render(request, 'rmtpoints.html', {'purchases': updated_purchases})

    return render(request, 'rmtpoints.html', {'purchases': purchases})


def CASHView(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT value FROM acc_reg_num WHERE account_id = %s AND `key` = '#CASHPOINTS'", [request.user.id])
        cash = cursor.fetchone()

    if cash:
        cash = cash[0]
    else:
        cash = 0

    if request.method == 'POST':
        cashpoints = int(request.POST.get('cash', 0))
        updated_cash = cash + cashpoints
        with connection.cursor() as cursor:
            cursor.execute("UPDATE acc_reg_num SET value = %s WHERE account_id = %s AND `key` = '#CASHPOINTS'", [updated_cash, request.user.id])
            connection.commit() # Salva as alterações no banco de dados
        return render(request, 'cashpoints.html', {'cash': updated_cash})

    return render(request, 'cashpoints.html', {'cash': cash})