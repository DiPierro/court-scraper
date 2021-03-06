class SeleniumSiteSearchMixIn():
    
    def search(self, search_terms=[], headless=True):
        portal_page = PortalPage(self.driver)
        portal_page.go_to_smart_search()
        results = []
        CaseInfoKls = self._get_case_info_mapped_class()
        try:
            for term in search_terms:
                search_page = SearchPage(self.driver)
                search_page.search_box = term
                search_page.submit_search(self.timeout)
                results_page = SearchResultsPage(self.driver)
                if results_page.results_found():
                    for case_row in results_page.results:
                        row_data = case_row.metadata
                        case_row.detail_page_link.click()
                        detail_page = CaseDetailPage(self.driver)
                        row_data['page_source'] = detail_page.page_source
                        ci = CaseInfoKls(row_data)
                        results.append(ci)
                        results_page.back_to_search_results()
                results_page.back_to_smart_search_tab()
            return results
        finally:
            self.driver.quit()

    def _get_case_info_mapped_class(self):
        mapping = {
            'case_num': 'number',
            'file_date': 'filing_date',
        }
        CaseInfo._map = mapping
        return CaseInfo