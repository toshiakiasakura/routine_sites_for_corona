import webbrowser 
import argparse 


number_urls = {
    "Johns Hopkins" : "https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6",
    "world meter" : "https://www.worldometers.info/coronavirus/",
    "NHK": "https://www3.nhk.or.jp/news/special/coronavirus/data/",
    "stop covid19": "https://www.stopcovid19.jp/",
}

knowledge_urls = {
    "新型コロナウイルス感染症対策アドバイザリーボード" : "https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/0000121431_00093.html",
    "新型コロナウイルス感染症対策分科会" : "https://www.cas.go.jp/jp/seisaku/ful/yusikisyakaigi.html",
    "中澤港" : "http://minato.sip21c.org/2019-nCoV-im3r.html", 
    "imperial college": "https://www.imperial.ac.uk/mrc-global-infectious-disease-analysis/covid-19/",
    "CDC" : "https://www.cdc.gov/mmwr/Novel_Coronavirus_Reports.html", 
    "WHO" : "https://www.who.int/emergencies/diseases/novel-coronavirus-2019",
}

# see also journal citation report. 
journal_urls = {
    "NEJM" : "https://www.nejm.org/coronavirus",
    "LANCET": "https://www.thelancet.com/coronavirus",
    "BMJ" : "https://www.bmj.com/coronavirus",
    "nature" : "https://www.nature.com/collections/hajgidghjb",
    "science": "https://www.sciencemag.org/collections/coronavirus",
    "elsevier" : "https://www.elsevier.com/connect/coronavirus-information-center",
    "oxford" : "https://academic.oup.com/journals/pages/coronavirus",
}


def parse_args():
    parser = argparse.ArgumentParser(description="Open urls")
    parser.add_argument("--number","-n", action="store_true", 
                        help="""For check the situation of covid-19.""")
    parser.add_argument("--knowledge","-k", action="store_true", 
                        help="""For check latest information about covid-19.""")
    parser.add_argument("--journals","-j", action="store_true", 
                        help="""Major journal searching. """)


    args = parser.parse_args()
    return(args)

def open_urls(dic_):
    """Open urls. 

    Args: 
        dic_ (dict) : values are explanations, keys are urls. 
    """
    for k,v in dic_.items():
        webbrowser.open(v, new=2)

def main():
    args = parse_args()
    if args.number:
        open_urls(number_urls)
    if args.knowledge:
        open_urls(knowledge_urls)
    if args.journals:
        open_urls(journal_urls)


if __name__ == "__main__":
    main()
