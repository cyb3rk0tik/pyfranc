# -*- coding': utf-8 -*
#!/usr/bin/env python3

code_to_name = {"aar":   "Afar",
"abk":   "Abkhazian",
"ace":   "Achinese",
"acu":   "Achuar-Shiwiar",
"ada":   "Adangme",
"ady":   "Adyghe",
"afr":   "Afrikaans",
"agr":   "Aguaruna",
"aii":   "Assyrian Neo-Aramaic",
"ajg":   "Aja (Benin)",
"als":   "Tosk Albanian",
"alt":   "Southern Altai",
"amc":   "Amahuaca",
"ame":   "Yanesha'",
"amh":   "Amharic",
"ami":   "Amis",
"amr":   "Amarakaeri",
"arb":   "Standard Arabic",
"arl":   "Arabela",
"arn":   "Mapudungun",
"ast":   "Asturian",
"auc":   "Waorani",
"ayr":   "Central Aymara",
"azj":   "North Azerbaijani",
"bam":   "Bambara",
"ban":   "Balinese",
"bax":   "Bamun",
"bba":   "Baatonum",
"bci":   "Baoulé",
"bcl":   "Central Bikol",
"bel":   "Belarusian",
"bem":   "Bemba (Zambia)",
"ben":   "Bengali",
"bfa":   "Bari",
"bho":   "Bhojpuri",
"bin":   "Bini",
"bis":   "Bislama",
"blt":   "Tai Dam",
"boa":   "Bora",
"bod":   "Tibetan",
"bos":   "Bosnian",
"bre":   "Breton",
"buc":   "Bushi",
"bug":   "Buginese",
"bul":   "Bulgarian",
"bum":   "Bulu (Cameroon)",
"cab":   "Garifuna",
"cak":   "Kaqchikel",
"cat":   "Catalan",
"cbi":   "Chachi",
"cbr":   "Cashibo-Cacataibo",
"cbs":   "Cashinahua",
"cbt":   "Chayahuita",
"cbu":   "Candoshi-Shapra",
"ceb":   "Cebuano",
"ces":   "Czech",
"cfm":   "Falam Chin",
"cha":   "Chamorro",
"chj":   "Ojitlán Chinantec",
"chk":   "Chuukese",
"chr":   "Cherokee",
"chv":   "Chuvash",
"cic":   "Chickasaw",
"cjk":   "Chokwe",
"cjs":   "Shor",
"ckb":   "Central Kurdish",
"cmn":   "Mandarin Chinese",
"cnh":   "Hakha Chin",
"cni":   "Asháninka",
"cnr":   "Montenegrin",
"cof":   "Colorado",
"cos":   "Corsican",
"cot":   "Caquinte",
"cpu":   "Pichis Ashéninka",
"crh":   "Crimean Tatar",
"cri":   "Sãotomense",
"crs":   "Seselwa Creole French",
"csa":   "Chiltepec Chinantec",
"csw":   "Swampy Cree",
"ctd":   "Tedim Chin",
"cym":   "Welsh",
"dag":   "Dagbani",
"dan":   "Danish",
"ddn":   "Dendi (Benin)",
"deu":   "German",
"dga":   "Southern Dagaare",
"dip":   "Northeastern Dinka",
"div":   "Dhivehi",
"duu":   "Drung",
"dyo":   "Jola-Fonyi",
"dyu":   "Dyula",
"dzo":   "Dzongkha",
"ekk":   "Standard Estonian",
"ell":   "Modern Greek (1453-)",
"emk":   "Eastern Maninkakan",
"eng":   "English",
"epo":   "Esperanto",
"ese":   "Ese Ejja",
"eus":   "Basque",
"eve":   "Even",
"evn":   "Evenki",
"ewe":   "Ewe",
"fao":   "Faroese",
"fat":   "Fanti",
"fij":   "Fijian",
"fin":   "Finnish",
"fkv":   "Kven Finnish",
"fon":   "Fon",
"fra":   "French",
"fry":   "Western Frisian",
"fuf":   "Pular",
"fur":   "Friulian",
"fuv":   "Nigerian Fulfulde",
"fvr":   "Fur",
"gaa":   "Ga",
"gag":   "Gagauz",
"gaz":   "West Central Oromo",
"gjn":   "Gonja",
"gkp":   "Guinea Kpelle",
"gla":   "Scottish Gaelic",
"gld":   "Nanai",
"gle":   "Irish",
"glg":   "Galician",
"glv":   "Manx",
"gsw":   "Swiss German",
"guc":   "Wayuu",
"gug":   "Paraguayan Guaraní",
"guj":   "Gujarati",
"guu":   "Yanomamö",
"gyr":   "Guarayu",
"hat":   "Haitian",
"hau":   "Hausa",
"haw":   "Hawaiian",
"hea":   "Northern Qiandong Miao",
"heb":   "Hebrew",
"hil":   "Hiligaynon",
"hin":   "Hindi",
"hlt":   "Matu Chin",
"hms":   "Southern Qiandong Miao",
"hna":   "Mina (Cameroon)",
"hni":   "Hani",
"hnj":   "Hmong Njua",
"hns":   "Caribbean Hindustani",
"hrv":   "Croatian",
"hsb":   "Upper Sorbian",
"hun":   "Hungarian",
"hus":   "Huastec",
"huu":   "Murui Huitoto",
"hye":   "Armenian",
"ibb":   "Ibibio",
"ibo":   "Igbo",
"ido":   "Ido",
"idu":   "Idoma",
"iii":   "Sichuan Yi",
"ijs":   "Southeast Ijo",
"ike":   "Eastern Canadian Inuktitut",
"ilo":   "Iloko",
"ina":   "Interlingua (International Auxiliary Language Association)",
"ind":   "Indonesian",
"isl":   "Icelandic",
"ita":   "Italian",
"jav":   "Javanese",
"jiv":   "Shuar",
"jpn":   "Japanese",
"kaa":   "Kara-Kalpak",
"kal":   "Kalaallisut",
"kan":   "Kannada",
"kat":   "Georgian",
"kaz":   "Kazakh",
"kbd":   "Kabardian",
"kbp":   "Kabiyè",
"kde":   "Makonde",
"kdh":   "Tem",
"kea":   "Kabuverdianu",
"kek":   "Kekchí",
"kha":   "Khasi",
"khk":   "Halh Mongolian",
"khm":   "Khmer",
"kin":   "Kinyarwanda",
"kir":   "Kirghiz",
"kjh":   "Khakas",
"kkh":   "Khün",
"kmb":   "Kimbundu",
"knc":   "Central Kanuri",
"kng":   "Koongo",
"koi":   "Komi-Permyak",
"koo":   "Konzo",
"kor":   "Korean",
"kqn":   "Kaonde",
"kqs":   "Northern Kissi",
"kri":   "Krio",
"krl":   "Karelian",
"ktu":   "Kituba (Democratic Republic of Congo)",
"kwi":   "Awa-Cuaiquer",
"lad":   "Ladino",
"lao":   "Lao",
"lat":   "Latin",
"lia":   "West-Central Limba",
"lij":   "Ligurian",
"lin":   "Lingala",
"lit":   "Lithuanian",
"lld":   "Ladin",
"lns":   "Lamnso'",
"lob":   "Lobi",
"lot":   "Otuho",
"loz":   "Lozi",
"ltz":   "Luxembourgish",
"lua":   "Luba-Lulua",
"lue":   "Luvale",
"lug":   "Ganda",
"lun":   "Lunda",
"lus":   "Lushai",
"lvs":   "Standard Latvian",
"mad":   "Madurese",
"mag":   "Magahi",
"mah":   "Marshallese",
"mai":   "Maithili",
"mal":   "Malayalam",
"mam":   "Mam",
"mar":   "Marathi",
"maz":   "Central Mazahua",
"mcd":   "Sharanahua",
"mcf":   "Matsés",
"men":   "Mende (Sierra Leone)",
"mfq":   "Moba",
"mic":   "Mi'kmaq",
"min":   "Minangkabau",
"miq":   "Mískito",
"mkd":   "Macedonian",
"mlt":   "Maltese",
"mnw":   "Mon",
"mor":   "Moro",
"mos":   "Mossi",
"mri":   "Maori",
"mto":   "Totontepec Mixe",
"mxi":   "Mozarabic",
"mxv":   "Metlatónoc Mixtec",
"mya":   "Burmese",
"mzi":   "Ixcatlán Mazatec",
"nav":   "Navajo",
"nba":   "Nyemba",
"nbl":   "South Ndebele",
"ndo":   "Ndonga",
"nds":   "Low German",
"nhn":   "Central Nahuatl",
"nio":   "Nganasan",
"niu":   "Niuean",
"niv":   "Gilyak",
"njo":   "Ao Naga",
"nku":   "Bouna Kulango",
"nld":   "Dutch",
"nno":   "Norwegian Nynorsk",
"nob":   "Norwegian Bokmål",
"not":   "Nomatsiguenga",
"npi":   "Nepali (individual language)",
"nso":   "Pedi",
"nya":   "Nyanja",
"nym":   "Nyamwezi",
"nyn":   "Nyankole",
"nzi":   "Nzima",
"oaa":   "Orok",
"oci":   "Occitan (post 1500)",
"ojb":   "Northwestern Ojibwa",
"oki":   "Okiek",
"orh":   "Oroqen",
"oss":   "Ossetian",
"ote":   "Mezquital Otomi",
"pam":   "Pampanga",
"pan":   "Panjabi",
"pap":   "Papiamento",
"pau":   "Palauan",
"pbb":   "Páez",
"pbu":   "Northern Pashto",
"pcd":   "Picard",
"pcm":   "Nigerian Pidgin",
"pes":   "Iranian Persian",
"pis":   "Pijin",
"piu":   "Pintupi-Luritja",
"plt":   "Plateau Malagasy",
"pnb":   "Western Panjabi",
"pol":   "Polish",
"pon":   "Pohnpeian",
"por":   "Portuguese",
"pov":   "Upper Guinea Crioulo",
"ppl":   "Pipil",
"prs":   "Dari",
"quc":   "K'iche'",
"que":   "Quechua",
"qug":   "Chimborazo Highland Quichua",
"quh":   "South Bolivian Quechua",
"quy":   "Ayacucho Quechua",
"quz":   "Cusco Quechua",
"qva":   "Ambo-Pasco Quechua",
"qvc":   "Cajamarca Quechua",
"qvh":   "Huamalíes-Dos de Mayo Huánuco Quechua",
"qvm":   "Margos-Yarowilca-Lauricocha Quechua",
"qvn":   "North Junín Quechua",
"qwh":   "Huaylas Ancash Quechua",
"qxn":   "Northern Conchucos Ancash Quechua",
"qxu":   "Arequipa-La Unión Quechua",
"rar":   "Rarotongan",
"rgn":   "Romagnol",
"rmn":   "Balkan Romani",
"roh":   "Romansh",
"ron":   "Romanian",
"run":   "Rundi",
"rup":   "Macedo-Romanian",
"rus":   "Russian",
"sag":   "Sango",
"sah":   "Yakut",
"san":   "Sanskrit",
"sat":   "Santali",
"sco":   "Scots",
"sey":   "Secoya",
"shk":   "Shilluk",
"shn":   "Shan",
"shp":   "Shipibo-Conibo",
"sin":   "Sinhala",
"skr":   "Saraiki",
"slk":   "Slovak",
"slr":   "Salar",
"slv":   "Slovenian",
"sme":   "Northern Sami",
"smo":   "Samoan",
"sna":   "Shona",
"snk":   "Soninke",
"snn":   "Siona",
"som":   "Somali",
"sot":   "Southern Sotho",
"spa":   "Spanish",
"src":   "Logudorese Sardinian",
"srp":   "Serbian",
"srr":   "Serer",
"ssw":   "Swati",
"suk":   "Sukuma",
"sun":   "Sundanese",
"sus":   "Susu",
"swb":   "Maore Comorian",
"swe":   "Swedish",
"swh":   "Swahili (individual language)",
"tah":   "Tahitian",
"tam":   "Tamil",
"tat":   "Tatar",
"tbz":   "Ditammari",
"tca":   "Ticuna",
"tdt":   "Tetun Dili",
"tel":   "Telugu",
"tem":   "Timne",
"tet":   "Tetum",
"tgk":   "Tajik",
"tgl":   "Tagalog",
"tha":   "Thai",
"tir":   "Tigrinya",
"tiv":   "Tiv",
"tly":   "Talysh",
"tob":   "Toba",
"toi":   "Tonga (Zambia)",
"toj":   "Tojolabal",
"ton":   "Tonga (Tonga Islands)",
"top":   "Papantla Totonac",
"tpi":   "Tok Pisin",
"tsn":   "Tswana",
"tso":   "Tsonga",
"tsz":   "Purepecha",
"tuk":   "Turkmen",
"tur":   "Turkish",
"twi":   "Twi",
"tyv":   "Tuvinian",
"tzh":   "Tzeltal",
"tzm":   "Central Atlas Tamazight",
"tzo":   "Tzotzil",
"udu":   "Uduk",
"uig":   "Uighur",
"ukr":   "Ukrainian",
"umb":   "Umbundu",
"ura":   "Urarina",
"urd":   "Urdu",
"uzn":   "Northern Uzbek ",
"vai":   "Vai",
"vec":   "Venetian",
"ven":   "Venda",
"vep":   "Veps",
"vie":   "Vietnamese",
"vmw":   "Makhuwa",
"war":   "Waray (Philippines)",
"wln":   "Walloon",
"wol":   "Wolof",
"wwa":   "Waama",
"xho":   "Xhosa",
"xsm":   "Kasem",
"yad":   "Yagua",
"yao":   "Yao",
"yap":   "Yapese",
"ydd":   "Eastern Yiddish",
"ykg":   "Northern Yukaghir",
"yor":   "Yoruba",
"yrk":   "Nenets",
"yua":   "Yucateco",
"zam":   "Miahuatlán Zapotec",
"zdj":   "Ngazidja Comorian",
"zgh":   "Standard Moroccan Tamazight",
"zlm":   "Malay (individual language)",
"zro":   "Záparo",
"ztu":   "Güilá Zapotec",
"zul":   "Zulu",
"zyb":   "Yongbei Zhuang"}