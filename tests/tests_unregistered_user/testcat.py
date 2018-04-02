from pages.home import HomePage


def test_elements_dropdown_desktops():
    page = HomePage()
    list_desktops = page.navigate_to_home_page().list_category_desktops()
    for list in list_desktops:
        assert (list.is_displayed())


def test_pc():
    page = HomePage()
    page.navigate_to_home_page().select_pc_product()
    assert ('PC' == page.title())


def test_mac():
    page = HomePage()
    page.navigate_to_home_page().select_mac_product()
    assert ('Mac' == page.title())


def test_count_subcategories_desktops():
    page = HomePage()
    count = page.navigate_to_home_page().list_category_desktops()
    assert (len(count) == 2)


def test_show_all_desktops():
    page = HomePage()
    page.navigate_to_home_page().show_all_desktops()
    assert ('Desktops' == page.title())
