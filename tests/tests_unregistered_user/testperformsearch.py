import pytest


@pytest.mark.usefixtures('initialize')
class TestPerformSearch:
    def test_search_title(self):
        assert self.searchpage.is_title_matches("Search")

    def test_items_found(self):
        assert self.searchpage.is_product_matches("mac")
