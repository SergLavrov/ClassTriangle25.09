
def set_password(password):

    if password == '' or len(password) < 8:
        return 'The length of password is too short'

    cnt = 0
    for item in password:
        if item.isalpha():
            cnt += 1
    if cnt < 3:
        return 'The quantity of letters must be more than three'
    else:
        return password


passw = input('Enter password: ')

print(set_password(passw))


# for i in range(5):
#     print(i)

# Дано 3-х значеное сисло. Верно ли что все его цифры одинаковые!

# DELIMITER $$
#
# CREATE FUNCTION get_result(number int)
#
# RETURNS varchar(10)
#
# DETERMINISTIC
#     BEGIN
#         DECLARE n1, n2, n3 int;
#         set n1 = number div 100;
#         set n2 = (number mod 100) div 10;
#         set n3 = number mod 10;
#
#         if n1 = n2 = n3 then
#             return 'Yes';
#         else
#             return 'No';
#         end if;
#
#     END $$
# DELIMITER;
#
# # DROP FUNCTION IF EXISTS get_result;
#
# SELECT get_result(121) as result;
#
#
#
# # 4.37. Проверить, принадлежит ли число, введенное с клавиатуры, интервалу (–5, 3)
#
# DELIMITER $$
#
# CREATE FUNCTION get_space(number int)
#
# RETURNS varchar(10)
#
# DETERMINISTIC
#     BEGIN
#         DECLARE n1 int;
#         set n1 = number;
#         if n1 < -5 OR n1 >= 3 then
#             return 'No';
#         else
#             return 'Yes';
#         end if;
#
#     END $$
# DELIMITER;
#
# # DROP FUNCTION IF EXISTS get_space;
#
# SELECT get_space(2) as result;
#
#
# # 4.35.*Имеется стол прямоугольной формы с размерами a и b (a и b — целые числа, a > b).
# # В каком случае на столе можно разместить большее количество каротонных прямоугольников с размерами
# # c и d (c и d — целые числа, c > d): при размещении их длинной стороной вдоль длинной стороны стола или вдоль
# # короткой. Прямоугольники не должны лежать один на другом и не должны свисать со стола.
#
# DELIMITER $$
#
# CREATE FUNCTION get_quantity_rectangle (a int, b int, c int, d int)
#
# RETURNS varchar(100)
#
# DETERMINISTIC
#     BEGIN
#         DECLARE a1, b1, c1, d1  int;
#         set a1 = a;
#         set b1 = b;
#         set c1 = c;
#         set d1 = d;
#
#         if a1 div c1 > b1 div c1 then
#             return 'При размещении их длинной стороной вдоль длинной стороны стола';
#         else
#             return 'При размещении их длинной стороной вдоль короткой стороны стола';
#         end if;
#
#     END $$
# DELIMITER;
#
# # DROP FUNCTION IF EXISTS get_quantity_rectangle;
#
# SELECT get_quantity_rectangle(5, 4, 3, 1) as result;
#
