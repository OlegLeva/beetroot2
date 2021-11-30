class List_:

    def count_spec_digits(self, integers_list, digits_list):
        my_str = ''.join(str(e) for e in integers_list)
        res_list = []
        for d in digits_list:
            count = 0
            d = str(d)
            for l in my_str:
                if d == l:
                    count += 1
            res_list.append((d, count,))
        return res_list

ll = List_()
print(ll.count_spec_digits([-77, -65, 56, -79, 6666, 222], [1, 8, 4]))
print(ll.count_spec_digits([-18, -31, 81, -19, 111, -888], [1, 8, 4]))


