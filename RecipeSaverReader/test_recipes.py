from recipes import menu_validation, trans_to_ingredients_list, \
    ingredients_validation, time_validation, convert_recipe_name, contents


def test_menu_validation():
    assert(menu_validation(1) is True)
    assert(menu_validation(-1) is False)
    assert(menu_validation('lmao') is False)
    assert(menu_validation('') is False)


def test_trans_to_ingredients_list():
    assert(trans_to_ingredients_list('') == [''])
    assert(trans_to_ingredients_list(',') == ['', ''])
    assert(trans_to_ingredients_list('abc, cba') == ['abc', 'cba'])
    assert(trans_to_ingredients_list(',abc') == ['', 'abc'])
    assert(trans_to_ingredients_list('abc, cba, ,ccc') ==
           ['abc', 'cba', '', 'ccc'])


def test_ingredients_validation():
    assert(ingredients_validation(['']) is False)
    assert(ingredients_validation(['', 'a']) is True)
    assert(ingredients_validation(['a']) is True)
    assert(ingredients_validation(['', '']) is False)
    assert(ingredients_validation(['', '', 'a']) is True)
    assert(ingredients_validation(['a', 'b', 'c']) is True)


def test_time_validation():
    assert(time_validation(-10) is False)
    assert(time_validation(10) is True)
    assert(time_validation(0) is True)
    assert(time_validation('lmao') is False)
    assert(time_validation('') is False)


def test_convert_recipe_name():
    assert(convert_recipe_name('') == '.txt')
    assert(convert_recipe_name('Hello Word') == 'hello_word.txt')
    assert(convert_recipe_name('he11o!!@@word') == 'he11oword.txt')
    assert(convert_recipe_name('  baby back rib%$') == 'baby_back_rib.txt')


def test_content():
    assert(contents('Tomato Soup', ['1 can tomato soup'], 'Heat it', '10') ==
           'Tomato Soup' + 2 * '\n' + 'Ingredients:\n1 can tomato soup' +
           2 * '\n' + 'Time: 10 minutes' + 2 * '\n' + 'Directions:\nHeat it')
