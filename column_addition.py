def add_column(numb1, numb2):
    if numb1 > numb2:
        x = numb1
        y = numb2
    else:
        x = numb2
        y = numb1
    res = ''
    while x != 0:
        x1 = x % 10
        y1 = y % 10
        z = x1 + y1
        if z > 9:
            z %= 10
            res += str(z)
            x = int((x - x1) // 10 + 1)
            y = int((y - y1) // 10)
        else:
            res += str(z)
            x = int((x - x1) // 10)
            y = int((y - y1) // 10)
    return int(res[::-1])


# print(add_column(123489787563376678080878676465354808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453562543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535677687565234897875633766780808786764653548087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535625435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356776875652348978756337667808087867646535480878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453567768756523489787563376678080878676465354808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453562543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535677687565234897875633766780808786764653548087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535625435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356776875652348978756337667808087867646535480878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453567768756523489787563376678080878676465354808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453562543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535677687565234897875633766780808786764653548087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535625435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356776875652348978756337667808087867646535480878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453567768756523489787563376678080878676465354808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453562543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535677687565234897875633766780808786764653548087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535625435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356776875652348978756337667808087867646535480878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453568087867646535425435676897097875654454343245356254356768970978756544543432453568087867646535425435676897097875654454343245356808786764653542543567689709787565445434324535680878676465354254356768970978756544543432453567768756534234,
#                  8756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543387565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433875654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354338756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543387565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433875654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354338756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543387565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433875654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354338756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543387565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433875654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354338756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543387565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433875654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354338756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543387565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433875654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354333365465465476476576576575654543423432354338756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543333654654654764765765765756545434234323543387565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657565454342343235433336546546547647657657657587678))


'https://tehtab.ru/Guide/GuideMathematics/GuideMathematicsNumericalSystems/GuideMathematicsNumericalSystemsDecimalBinaryHexadecimal/'
'https://www.youtube.com/watch?v=5vlXq2uuh4Q'
'https://pythoner.name/another-numeral-system'

print(int('255',16))
print(hex(597))