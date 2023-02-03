#!/usr/bin/env python
from handler import lambda_handler
from pprint import PrettyPrinter

if __name__ == "__main__":
    snippet_arxiv = {
        "results":
            ['The European Particle Physics  Strategy recently identified precision studies of the Higgs boson as the main priority for the next high-energy collider with measurements\nfirst at the planned high luminosity upgrade of the LHC and, later, with a dedicated Higgs factory as a new facility.\nThis program involves essential interaction between experiment and theory.\nHow well does the discovered boson match the Standard Model Higgs and can we find hints for new physics beyond the Standard Model?', 'The long-sought Higgs boson(s) $h$ of electroweak symmetry breaking\nin particle physics may soon be observed at the CERN Large Hadron\nCollider (LHC) through the diphoton decay mode ($h\\rightarrow\\gamma\\gamma$).\nPurely hadronic standard model processes are a copious source of diphotons,\nand a narrow Higgs boson signal at relatively low masses will appear\nas a small peak above this considerable background. A precise theoretical\nunderstanding of the kinematic distributions for diphoton production\nin the standard model could provide valuable guidance in the search\nfor the Higgs boson signal and assist in the important measurement \nof Higgs boson coupling strengths.', "This article surveys \nHiggs boson physics with an outlook to future experiments.\n%\nIn Section \\ref{sec:higssth}\nwe discuss the role of the Higgs boson in the origin of mass.\nSection \\ref{Discovery} reviews the discovery and early\nmeasurements \nof the Higgs boson's properties.\nRecent measurements of the Higgs coupling to fermions are discussed in Section \n\\ref{fermions}.\nSection \\ref{properties} summarises the status of measurement of the Higgs boson's properties and \ninteractions\nin comparison to the predictions for the Higgs boson\ndescribed by the\nStandard Model.\nIn Section \\ref{lambda} \nwe discuss\nthe Higgs self-coupling.\nSection \\ref{extrahiggses} \nfocuses on \nsearches for any extra Higgs states or possible new CP violation in the Higgs sector.\n%\nIn Sections \\ref{sec:vac} and \\ref{sec:cosmo}\nwe describe open\ntheoretical issues connected to the Higgs boson in particle physics and cosmology.\nWhat might the Higgs boson be telling us about (the need for) extra new physics beyond the Standard Model?\nFinally, in Section \\ref{conclusions} we give an outlook to future \nmeasurements\nthat might shed light on these questions and the role of the Higgs in understanding the deep structure of the Universe.", 'The world-wide particle physics community was excited by the announcement, and \nthe international press coverage of the event was huge.'],
        "sources":[{'source': {'section': 'Introduction', 'content': 'The European Particle Physics  Strategy recently identified precision studies of the Higgs boson as the main priority for the next high-energy collider with measurements\nfirst at the planned high luminosity upgrade of the LHC and, later, with a dedicated Higgs factory as a new facility.\nThis program involves essential interaction between experiment and theory.\nHow well does the discovered boson match the Standard Model Higgs and can we find hints for new physics beyond the Standard Model?', 'title': 'The Higgs boson -- its implications and prospects for future discoveries', 'id': '2104.06821'}}, {'source': {'section': 'Introduction', 'content': 'The long-sought Higgs boson(s) $h$ of electroweak symmetry breaking\nin particle physics may soon be observed at the CERN Large Hadron\nCollider (LHC) through the diphoton decay mode ($h\\rightarrow\\gamma\\gamma$).\nPurely hadronic standard model processes are a copious source of diphotons,\nand a narrow Higgs boson signal at relatively low masses will appear\nas a small peak above this considerable background. A precise theoretical\nunderstanding of the kinematic distributions for diphoton production\nin the standard model could provide valuable guidance in the search\nfor the Higgs boson signal and assist in the important measurement \nof Higgs boson coupling strengths.', 'title': 'Calculation of prompt diphoton production cross sections at Tevatron and LHC energies', 'id': '0704.0001'}}, {'source': {'section': 'Introduction', 'content': "This article surveys \nHiggs boson physics with an outlook to future experiments.\n%\nIn Section \\ref{sec:higssth}\nwe discuss the role of the Higgs boson in the origin of mass.\nSection \\ref{Discovery} reviews the discovery and early\nmeasurements \nof the Higgs boson's properties.\nRecent measurements of the Higgs coupling to fermions are discussed in Section \n\\ref{fermions}.\nSection \\ref{properties} summarises the status of measurement of the Higgs boson's properties and \ninteractions\nin comparison to the predictions for the Higgs boson\ndescribed by the\nStandard Model.\nIn Section \\ref{lambda} \nwe discuss\nthe Higgs self-coupling.\nSection \\ref{extrahiggses} \nfocuses on \nsearches for any extra Higgs states or possible new CP violation in the Higgs sector.\n%\nIn Sections \\ref{sec:vac} and \\ref{sec:cosmo}\nwe describe open\ntheoretical issues connected to the Higgs boson in particle physics and cosmology.\nWhat might the Higgs boson be telling us about (the need for) extra new physics beyond the Standard Model?\nFinally, in Section \\ref{conclusions} we give an outlook to future \nmeasurements\nthat might shed light on these questions and the role of the Higgs in understanding the deep structure of the Universe.", 'title': 'The Higgs boson -- its implications and prospects for future discoveries', 'id': '2104.06821'}}, {'source': {'section': 'The Higgs boson and massive gauge bosons', 'content': 'The world-wide particle physics community was excited by the announcement, and \nthe international press coverage of the event was huge.', 'title': 'The Higgs boson -- its implications and prospects for future discoveries', 'id': '2104.06821'}}]
    }
    snippet_web = {
        "results": [   'With $175.8\xa0million, Musk founded SpaceX in 2002, a '
                   'spaceflight services company. In 2004, he was an early '
                   'investor in the electric vehicle manufacturer Tesla '
                   'Motors, Inc. (now Tesla, Inc.). He became its chairman and '
                   'product architect, assuming the position of CEO in 2008. '
                   'In 2006, he helped create SolarCity, a solar energy '
                   'company that was later acquired by Tesla and became Tesla '
                   'Energy. In 2015, he co-founded OpenAI, a nonprofit '
                   'artificial intelligence research company. The following '
                   'year, he co-founded Neuralink—a neurotechnology company '
                   'developing brain–computer interfaces—and The Boring '
                   'Company, a tunnel construction company. Musk has also '
                   'proposed a hyperloop high-speed vactrain transportation '
                   'system. In 2022, his acquisition of Twitter for $44 '
                   'billion was completed.',
                   'Elon Musk co-founded and leads Tesla, SpaceX, Neuralink '
                   'and The Boring Company.\n'
                   '\n'
                   'As the co-founder and CEO of Tesla, Elon leads all product '
                   'design, engineering and global manufacturing of the '
                   "company's electric vehicles, battery products and solar "
                   'energy products.',
                   'Later in 1999, Musk co-founded X.com, an online financial '
                   'services and e-mail payment company.[59] X.com was one of '
                   'the first federally insured online banks, and over 200,000 '
                   'customers joined in its initial months of operation.[60] '
                   'Even though Musk founded the company, investors regarded '
                   'him as inexperienced and replaced him with Intuit CEO Bill '
                   'Harris by the end of the year.[61]',
                   'Pages for logged out editors learn more\n'
                   '\n'
                   'Elon Reeve Musk FRS (/ˈiːlɒn/ EE-lon; born June 28, 1971) '
                   'is a business magnate and investor. He is the founder, CEO '
                   'and chief engineer of SpaceX; angel investor, CEO and '
                   'product architect of Tesla, Inc.; owner and CEO of '
                   'Twitter, Inc.; founder of The Boring Company; co-founder '
                   'of Neuralink and OpenAI; and president of the '
                   'philanthropic Musk Foundation. With an estimated net worth '
                   'of around $139\xa0billion as of December 23, 2022, '
                   'primarily from his ownership stakes in Tesla and '
                   'SpaceX,[4][5] Musk is the second-wealthiest person in the '
                   'world, according to both the Bloomberg Billionaires Index '
                   "and Forbes's real-time billionaires list.[6][7]"],
        "sources":[   {   'content': 'With $175.8\xa0million, Musk founded SpaceX '
                                  'in 2002, a spaceflight services company. In '
                                  '2004, he was an early investor in the '
                                  'electric vehicle manufacturer Tesla Motors, '
                                  'Inc. (now Tesla, Inc.). He became its '
                                  'chairman and product architect, assuming '
                                  'the position of CEO in 2008. In 2006, he '
                                  'helped create SolarCity, a solar energy '
                                  'company that was later acquired by Tesla '
                                  'and became Tesla Energy. In 2015, he '
                                  'co-founded OpenAI, a nonprofit artificial '
                                  'intelligence research company. The '
                                  'following year, he co-founded Neuralink—a '
                                  'neurotechnology company developing '
                                  'brain–computer interfaces—and The Boring '
                                  'Company, a tunnel construction company. '
                                  'Musk has also proposed a hyperloop '
                                  'high-speed vactrain transportation system. '
                                  'In 2022, his acquisition of Twitter for $44 '
                                  'billion was completed.',
                       'source': 2,
                       'url': 'https://en.wikipedia.org/wiki/Elon_Musk'},
                   {   'content': 'Elon Musk co-founded and leads Tesla, '
                                  'SpaceX, Neuralink and The Boring Company.\n'
                                  '\n'
                                  'As the co-founder and CEO of Tesla, Elon '
                                  'leads all product design, engineering and '
                                  "global manufacturing of the company's "
                                  'electric vehicles, battery products and '
                                  'solar energy products.',
                       'source': 0,
                       'url': 'https://www.tesla.com/elon-musk'},
                   {   'content': 'Later in 1999, Musk co-founded X.com, an '
                                  'online financial services and e-mail '
                                  'payment company.[59] X.com was one of the '
                                  'first federally insured online banks, and '
                                  'over 200,000 customers joined in its '
                                  'initial months of operation.[60] Even '
                                  'though Musk founded the company, investors '
                                  'regarded him as inexperienced and replaced '
                                  'him with Intuit CEO Bill Harris by the end '
                                  'of the year.[61]',
                       'source': 10,
                       'url': 'https://en.wikipedia.org/wiki/Elon_Musk'},
                   {   'content': 'Pages for logged out editors learn more\n'
                                  '\n'
                                  'Elon Reeve Musk FRS (/ˈiːlɒn/ EE-lon; born '
                                  'June 28, 1971) is a business magnate and '
                                  'investor. He is the founder, CEO and chief '
                                  'engineer of SpaceX; angel investor, CEO and '
                                  'product architect of Tesla, Inc.; owner and '
                                  'CEO of Twitter, Inc.; founder of The Boring '
                                  'Company; co-founder of Neuralink and '
                                  'OpenAI; and president of the philanthropic '
                                  'Musk Foundation. With an estimated net '
                                  'worth of around $139\xa0billion as of '
                                  'December 23, 2022, primarily from his '
                                  'ownership stakes in Tesla and SpaceX,[4][5] '
                                  'Musk is the second-wealthiest person in the '
                                  'world, according to both the Bloomberg '
                                  "Billionaires Index and Forbes's real-time "
                                  'billionaires list.[6][7]',
                       'source': 0,
                       'url': 'https://en.wikipedia.org/wiki/Elon_Musk'}]
    }

    EVENT = {
        "snippets":{
            "arxiv":snippet_arxiv,
            "web":snippet_web
        },
        "query":"Where was Elon born?"
    }

    pp = PrettyPrinter(indent=4)

    resp = lambda_handler(EVENT, None)
    pp.pprint(resp)