from password import check_length, \
    check_four_requirements, check_special_characters,\
    secure_password


def test_check_length():
    assert(check_length('001', 9, 12) is False)
    assert(check_length('111111111', 9, 12))
    assert(check_length('222222222222', 9, 12))
    assert(check_length('123456789987654321', 9, 12) is False)


def test_check_four_requirements():
    assert(check_four_requirements("Aa$1", 1, ['$', '#', '@', '!']))
    assert(check_four_requirements("aa$1", 1, ['$', '#', '@', '!']))
    assert(check_four_requirements("Aaa1", 1, ['$', '#', '@', '!']))
    assert(check_four_requirements("Aaa$", 1, ['$', '#', '@', '!']))
    assert(check_four_requirements("$1#22$", 1, ['$', '#', '@', '!']) is False)
    assert(check_four_requirements("1111", 1, ['$', '#', '@', '!']) is False)
    assert(check_four_requirements("AAA", 1, ['$', '#', '@', '!']) is False)
    assert(check_four_requirements("aa", 1, ['$', '#', '@', '!']) is False)
    assert(check_four_requirements("$", 1, ['$', '#', '@', '!']) is False)


def test_check_special_characters():
    assert(check_special_characters("1234^67(", ['$', '#', '@', '!']) is False)
    assert(check_special_characters("abc!!$$##@@", ['$', '#', '@', '!']))
    assert(check_special_characters("%^&$#@", ['$', '#', '@', '!']) is False)


def test_secure_password():
    assert(secure_password('a') is False)
    assert(secure_password('1234567812345678') is False)
    assert(secure_password('a1234B567!'))
    assert(secure_password('a1234b5678') is False)
    assert(secure_password('123456789') is False)
    assert(secure_password('***32444!Bb') is False)
