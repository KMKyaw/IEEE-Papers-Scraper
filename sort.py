temp = 3
counter = 1
paper_no = 1
while temp <= 600:
    print("Temp = " + str(temp) + " Paper No. = " + str(paper_no))
    # if(paper_no == 10):
    #     temp -= 1
    temp += 3
    paper_no += 1
    
    # paper no.21 -> 62
    # //*[@id="container"]/micro-ui/document-search-results-page/div[1]/section[2]/div/div[2]/div/div[2]/div/els-results-layout/div[1]/table/tbody/tr[62]/td[2]/div/div/h4/a/span/span
    # paper no.31 -> 92
    # //*[@id="container"]/micro-ui/document-search-results-page/div[1]/section[2]/div/div[2]/div/div[2]/div/els-results-layout/div[1]/table/tbody/tr[92]/td[2]/div/div/h4/a/span/span
    # paper no.41 -> 122
    # //*[@id="container"]/micro-ui/document-search-results-page/div[1]/section[2]/div/div[2]/div/div[2]/div/els-results-layout/div[1]/table/tbody/tr[122]/td[2]/div/div/h4/a/span/span
    # paper no.148 -> 443
    # //*[@id="container"]/micro-ui/document-search-results-page/div[1]/section[2]/div/div[2]/div/div[2]/div/els-results-layout/div[1]/table/tbody/tr[443]/td[2]/div/div/h4/a/span/span
    # paper no.200 -> 599
    # //*[@id="container"]/micro-ui/document-search-results-page/div[1]/section[2]/div/div[2]/div/div[2]/div/els-results-layout/div[1]/table/tbody/tr[599]/td[2]/div/div/h4/a/span/span
    # paper no.201 -> 2
    # //*[@id="container"]/micro-ui/document-search-results-page/div[1]/section[2]/div/div[2]/div/div[2]/div/els-results-layout/div[1]/table/tbody/tr[2]/td[2]/div/div/h4/a/span/span
    # paper no.202 -> 5
    # //*[@id="container"]/micro-ui/document-search-results-page/div[1]/section[2]/div/div[2]/div/div[2]/div/els-results-layout/div[1]/table/tbody/tr[5]/td[2]/div/div/h4/a/span/span
    # paper no.400 -> 599
    # //*[@id="container"]/micro-ui/document-search-results-page/div[1]/section[2]/div/div[2]/div/div[2]/div/els-results-layout/div[1]/table/tbody/tr[599]/td[2]/div/div/h4/a/span/span
    # paper no.353 -> 458
    # //*[@id="container"]/micro-ui/document-search-results-page/div[1]/section[2]/div/div[2]/div/div[2]/div/els-results-layout/div[1]/table/tbody/tr[458]/td[2]/div/div/h4/a/span/span
    # paper no.401 -> 2
    # //*[@id="container"]/micro-ui/document-search-results-page/div[1]/section[2]/div/div[2]/div/div[2]/div/els-results-layout/div[1]/table/tbody/tr[2]/td[2]/div/div/h4/a/span/span
    # paper no.801 -> 2
    # //*[@id="container"]/micro-ui/document-search-results-page/div[1]/section[2]/div/div[2]/div/div[2]/div/els-results-layout/div[1]/table/tbody/tr[2]/td[2]/div/div/h4/a/span/span
    # paper no.1801 -> 2
    # //*[@id="container"]/micro-ui/document-search-results-page/div[1]/section[2]/div/div[2]/div/div[2]/div/els-results-layout/div[1]/table/tbody/tr[2]/td[2]/div/div/h4/a/span/span