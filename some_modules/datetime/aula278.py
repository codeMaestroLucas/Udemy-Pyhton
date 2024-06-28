# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela


def main() -> None:
    """Function used to run the main code."""
    from datetime import datetime
    from dateutil.relativedelta import relativedelta

    init_date = datetime(2020, 12, 20)
    delta = relativedelta(years= 5)
    end_date = init_date + delta

    delta_month = relativedelta(months= 1)
    installment_value = 1_000_000 /  (5 * 12)
    p: int = 1

    print('-' * 30)
    while init_date < end_date:
        print(f"""\033[1;33m{p}ª)\033[m\
 \033[1;36m{init_date.strftime("%d/%m/%Y")}\033[m\
 \033[1;32m${installment_value:.2f}\033[m
              """)
        print('-' * 30)
        init_date += delta_month
        p += 1

if __name__ == '__main__':
    main()
