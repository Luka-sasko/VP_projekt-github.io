import json

json_data = '''
[
    {
        "academic_name": "ADVENTISTIČKO TEOLOŠKO VISOKO UČILIŠTE, MARUŠEVEC*",
        "number_of_students": 21,
        "study_field": "Teologija",
        "region": "Zagrebačka županija"
    },
    {
        "academic_name": "AGRONOMSKI FAKULTET, ZAGREB",
        "number_of_students": 1665,
        "study_field": "Agronomija",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "AKADEMIJA DRAMSKE UMJETNOSTI, ZAGREB",
        "number_of_students": 380,
        "study_field": "Dramska umjetnost",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "AKADEMIJA LIKOVNIH UMJETNOSTI, ZAGREB",
        "number_of_students": 408,
        "study_field": "Likovne umjetnosti",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "AKADEMIJA PRIMIJENJENIH UMJETNOSTI, RIJEKA",
        "number_of_students": 297,
        "study_field": "Primijenjene umjetnosti",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "AKADEMIJA ZA UMJETNOST I KULTURU, OSIJEK",
        "number_of_students": 777,
        "study_field": "Umjetnost i kultura",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "ARHITEKTONSKI FAKULTET, ZAGREB",
        "number_of_students": 1101,
        "study_field": "Arhitektura",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "EDUKACIJSKO-REHABILITACIJSKI FAKULTET, ZAGREB",
        "number_of_students": 1063,
        "study_field": "Edukacijsko-rehabilitacijske znanosti",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "EFFECTUS VELEUČILIŠTE, ZAGREB",
        "number_of_students": 386,
        "study_field": "Računarstvo i informatika",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "EKONOMSKI FAKULTET, OSIJEK",
        "number_of_students": 1824,
        "study_field": "Ekonomija",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "EKONOMSKI FAKULTET, RIJEKA",
        "number_of_students": 2169,
        "study_field": "Ekonomija",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "EKONOMSKI FAKULTET, SPLIT",
        "number_of_students": 2356,
        "study_field": "Ekonomija",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "EKONOMSKI FAKULTET, ZAGREB",
        "number_of_students": 9821,
        "study_field": "Ekonomija",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "F. ELEKTROTEHNIKE, RAČUNARSTVA I INFORMACIJSKIH TEHNOLOG., OSIJEK",
        "number_of_students": 1757,
        "study_field": "Elektrotehnika, Računarstvo i Informacijske tehnologije",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "FAKULTET AGROBIOTEHNIČKIH ZNANOSTI, OSIJEK",
        "number_of_students": 1046,
        "study_field": "Agrobiotehničke znanosti",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "FAKULTET DENTALNE MEDICINE, RIJEKA",
        "number_of_students": 254,
        "study_field": "Dentalna medicina",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "FAKULTET ELEKTROTEHNIKE I RAČUNARSTVA, ZAGREB",
        "number_of_students": 4209,
        "study_field": "Elektrotehnika i Računarstvo",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "FAKULTET ELEKTROTEHNIKE, STROJARSTVA I BRODOGRADNJE, SPLIT",
        "number_of_students": 2165,
        "study_field": "Elektrotehnika, Strojarstvo i Brodogradnja",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "FAKULTET FILOZOFIJE I RELIGIJSKIH ZNANOSTI, ZAGREB",
        "number_of_students": 94,
        "study_field": "Filozofija i Religijske znanosti",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "FAKULTET GRAĐEVINARSTVA, ARHITEKTURE I GEODEZIJE, SPLIT",
        "number_of_students": 1055,
        "study_field": "Građevinarstvo, Arhitektura i Geodezija",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "FAKULTET INFORMATIKE I DIGITALNIH TEHNOLOGIJA, RIJEKA",
        "number_of_students": 444,
        "study_field": "Informatika i Digitalne tehnologije",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "FAKULTET KEMIJSKOG INŽENJERSTVA I TEHNOLOGIJE, ZAGREB",
        "number_of_students": 1170,
        "study_field": "Kemijsko inženjerstvo i tehnologija",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "FAKULTET ORGANIZACIJE I INFORMATIKE, VARAŽDIN",
        "number_of_students": 2488,
        "study_field": "Organizacija i Informatika",
        "region": "Varaždinska županija"
    },
    {
        "academic_name": "FAKULTET POLITIČKIH ZNANOSTI, ZAGREB",
        "number_of_students": 1392,
        "study_field": "Političke znanosti",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "FAKULTET PROMETNIH ZNANOSTI, ZAGREB",
        "number_of_students": 1584,
        "study_field": "Prometne znanosti",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "FAKULTET STROJARSTVA I BRODOGRADNJE, ZAGREB",
        "number_of_students": 2602,
        "study_field": "Strojarstvo i brodogradnja",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "FAKULTET ŠUMARSTVA I DRVNE TEHNOLOGIJE, ZAGREB",
        "number_of_students": 812,
        "study_field": "Šumarstvo i drvne tehnologije",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "FAKULTET TURIZMA I RURALNOG RAZVOJA U POŽEGI",
        "number_of_students": 620,
        "study_field": "Turizam i ruralni razvoj",
        "region": "Požeško-slavonska županija"
    },
    {
        "academic_name": "FAKULTET ZA DENTALNU MEDICINU I ZDRAVSTVO, OSIJEK",
        "number_of_students": 1103,
        "study_field": "Dentalna medicina i zdravstvo",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "FAKULTET ZA FIZIKU, RIJEKA",
        "number_of_students": 129,
        "study_field": "Fizika",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "FAKULTET ZA MATEMATIKU, RIJEKA",
        "number_of_students": 154,
        "study_field": "Matematika",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "FAKULTET ZA MENADŽMENT U TURIZMU I UGOSTITELJSTVU, OPATIJA",
        "number_of_students": 1964,
        "study_field": "Menadžment u turizmu i ugostiteljstvu",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "FAKULTET ZA ODGOJNE I OBRAZOVNE ZNANOSTI, OSIJEK",
        "number_of_students": 1036,
        "study_field": "Odgojne i obrazovne znanosti",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "FAKULTET ZDRAVSTVENIH STUDIJA, RIJEKA",
        "number_of_students": 854,
        "study_field": "Zdravstvene studije",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "FARMACEUTSKO-BIOKEMIJSKI FAKULTET, ZAGREB",
        "number_of_students": 1206,
        "study_field": "Farmacija i biokemija",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "FILOZOFSKI FAKULTET, OSIJEK",
        "number_of_students": 1282,
        "study_field": "Filozofija",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "FILOZOFSKI FAKULTET, RIJEKA",
        "number_of_students": 1277,
        "study_field": "Filozofija, religijske znanosti",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "FILOZOFSKI FAKULTET, SPLIT",
        "number_of_students": 1425,
        "study_field": "Filozofija, religijske znanosti",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "FILOZOFSKI FAKULTET, ZAGREB",
        "number_of_students": 6218,
        "study_field": "Filozofija, religijske znanosti",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "FILOZOFSKO-TEOLOŠKI INSTITUT D.I., ZAGREB*",
        "number_of_students": 54,
        "study_field": "Filozofija, religijske znanosti",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "GEODETSKI FAKULTET, ZAGREB",
        "number_of_students": 584,
        "study_field": "Geodezija, geoinformatika",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "GEOTEHNIČKI FAKULTET, VARAŽDIN",
        "number_of_students": 161,
        "study_field": "Geotehničko inženjerstvo",
        "region": "Varaždinska županija"
    },
    {
        "academic_name": "GRAĐEVINSKI FAKULTET, RIJEKA",
        "number_of_students": 797,
        "study_field": "Građevinarstvo, arhitektura",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "GRAĐEVINSKI FAKULTET, ZAGREB",
        "number_of_students": 1361,
        "study_field": "Građevinarstvo, arhitektura",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "GRAĐEVINSKI I ARHITEKTONSKI FAKULTET, OSIJEK",
        "number_of_students": 1151,
        "study_field": "Građevinarstvo, arhitektura",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "GRAFIČKI FAKULTET, ZAGREB",
        "number_of_students": 858,
        "study_field": "Grafičko inženjerstvo, dizajn",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "HRVATSKI STUDIJI, ZAGREB",
        "number_of_students": 1400,
        "study_field": "Interdisciplinarna područja",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "HRVATSKO KATOLIČKO SVEUČILIŠTE, ZAGREB",
        "number_of_students": 1467,
        "study_field": "Teologija, religijske znanosti",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "ISTARSKO VELEUČILIŠTE",
        "number_of_students": 74,
        "study_field": "Različita područja",
        "region": "Istarska županija"
    },
    {
        "academic_name": "KATOLIČKI BOGOSLOVNI FAKULTET, ĐAKOVO",
        "number_of_students": 65,
        "study_field": "Teologija",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "KATOLIČKI BOGOSLOVNI FAKULTET, SPLIT",
        "number_of_students": 145,
        "study_field": "Teologija",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "KATOLIČKI BOGOSLOVNI FAKULTET, ZAGREB",
        "number_of_students": 360,
        "study_field": "Teologija",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "KEMIJSKO-TEHNOLOŠKI FAKULTET, SPLIT",
        "number_of_students": 453,
        "study_field": "Kemija, tehnologija",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "KINEZIOLOŠKI FAKULTET, OSIJEK",
        "number_of_students": 365,
        "study_field": "Kineziologija, sportske znanosti",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "KINEZIOLOŠKI FAKULTET, SPLIT",
        "number_of_students": 784,
        "study_field": "Kineziologija, sportske znanosti",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "KINEZIOLOŠKI FAKULTET, ZAGREB",
        "number_of_students": 2541,
        "study_field": "Kineziologija, sportske znanosti",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "LIBERTAS MEĐUNARODNO SVEUČILIŠTE, ZAGREB",
        "number_of_students": 2249,
        "study_field": "Različita područja",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "MEDICINSKI FAKULTET, OSIJEK",
        "number_of_students": 735,
        "study_field": "Medicina",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "MEDICINSKI FAKULTET, RIJEKA",
        "number_of_students": 1381,
        "study_field": "Medicina",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "MEDICINSKI FAKULTET, SPLIT",
        "number_of_students": 1335,
        "study_field": "Medicina",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "MEDICINSKI FAKULTET, ZAGREB",
        "number_of_students": 2937,
        "study_field": "Medicina",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "MEĐIMURSKO VELEUČILIŠTE U ČAKOVCU",
        "number_of_students": 542,
        "study_field": "Različita područja",
        "region": "Međimurska županija"
    },
    {
        "academic_name": "METALURŠKI FAKULTET, SISAK",
        "number_of_students": 142,
        "study_field": "Metalurgija",
        "region": "Sisačko-moslavačka županija"
    },
    {
        "academic_name": "MUZIČKA AKADEMIJA, ZAGREB",
        "number_of_students": 556,
        "study_field": "Glazba, muzička umjetnost",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "ODJEL ZA BIOLOGIJU, OSIJEK",
        "number_of_students": 255,
        "study_field": "Biologija",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "ODJEL ZA BIOTEHNOLOGIJU, RIJEKA",
        "number_of_students": 311,
        "study_field": "Biotehnologija",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "ODJEL ZA FIZIKU, OSIJEK",
        "number_of_students": 82,
        "study_field": "Fizika",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "ODJEL ZA KEMIJU, OSIJEK",
        "number_of_students": 156,
        "study_field": "Kemija",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "ODJEL ZA MATEMATIKU, OSIJEK",
        "number_of_students": 482,
        "study_field": "Matematika",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "POMORSKI FAKULTET, RIJEKA",
        "number_of_students": 1519,
        "study_field": "Pomorstvo, nautika",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "POMORSKI FAKULTET, SPLIT",
        "number_of_students": 1290,
        "study_field": "Pomorstvo, nautika",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "POSLOVNO VELEUČILIŠTE ZAGREB",
        "number_of_students": 231,
        "study_field": "Poslovno upravljanje, ekonomija",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "PRAVNI FAKULTET, OSIJEK",
        "number_of_students": 1871,
        "study_field": "Pravo",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "PRAVNI FAKULTET, RIJEKA",
        "number_of_students": 1286,
        "study_field": "Pravo",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "PRAVNI FAKULTET, SPLIT",
        "number_of_students": 1916,
        "study_field": "Pravo",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "PRAVNI FAKULTET, ZAGREB",
        "number_of_students": 6059,
        "study_field": "Pravo",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "PREHRAMBENO-BIOTEHNOLOŠKI FAKULTET, ZAGREB",
        "number_of_students": 1063,
        "study_field": "Prehrambena tehnologija, biotehnologija",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "PREHRAMBENO-TEHNOLOŠKI FAKULTET, OSIJEK",
        "number_of_students": 644,
        "study_field": "Prehrambena tehnologija",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "PRIRODOSLOVNO-MATEMATIČKI FAKULTET, SPLIT",
        "number_of_students": 1078,
        "study_field": "Prirodne znanosti, matematika",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "PRIRODOSLOVNO-MATEMATIČKI FAKULTET, ZAGREB",
        "number_of_students": 4006,
        "study_field": "Prirodne znanosti, matematika",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "R.I.T. CROATIA, DUBROVNIK",
        "number_of_students": 790,
        "study_field": "Različita područja",
        "region": "Dubrovačko-neretvanska županija"
    },
    {
        "academic_name": "RUDARSKO-GEOLOŠKO-NAFTNI FAKULTET, ZAGREB",
        "number_of_students": 588,
        "study_field": "Rudarstvo, geologija, nafta",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "STOMATOLOŠKI FAKULTET, ZAGREB",
        "number_of_students": 862,
        "study_field": "Stomatologija",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "SVEUČILIŠNI ODJEL ZA FORENZIČNE ZNANOSTI, SPLIT",
        "number_of_students": 338,
        "study_field": "Forenzične znanosti",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "SVEUČILIŠNI ODJEL ZA STUDIJE MORA, SPLIT",
        "number_of_students": 165,
        "study_field": "Morske studije",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "SVEUČILIŠNI ODJEL ZDRAVSTVENIH STUDIJA, SPLIT",
        "number_of_students": 735,
        "study_field": "Zdravstvene znanosti",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "SVEUČILIŠNI STUDIJSKI ODJEL ZA STRUČNE STUDIJE, SPLIT",
        "number_of_students": 2141,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "SVEUČILIŠTE VERN, ZAGREB",
        "number_of_students": 1317,
        "study_field": "Poslovne i ekonomske znanosti, komunikacijske i medijske znanosti, informatičke znanosti, turizam, religijske znanosti",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "SVEUČILIŠTE SJEVER",
        "number_of_students": 4421,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Međimurska županija"
    },
    {
        "academic_name": "SVEUČILIŠTE U DUBROVNIKU",
        "number_of_students": 1313,
        "study_field": "Različita studijska područja, uključujući društvene, prirodne ili tehničke znanosti",
        "region": "Dubrovačko-neretvanska županija"
    },
    {
        "academic_name": "SVEUČILIŠTE U OSIJEKU***",
        "number_of_students": 74,
        "study_field": "Različita studijska područja, uključujući društvene, prirodne ili tehničke znanosti",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "SVEUČILIŠTE U PULI",
        "number_of_students": 3180,
        "study_field": "Različita studijska područja, uključujući društvene, prirodne ili tehničke znanosti",
        "region": "Istarska županija"
    },
    {
        "academic_name": "SVEUČILIŠTE U RIJECI***",
        "number_of_students": 183,
        "study_field": "Različita studijska područja, uključujući društvene, prirodne ili tehničke znanosti",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "SVEUČILIŠTE U SLAVONSKOM BRODU",
        "number_of_students": 2072,
        "study_field": "Različita studijska područja, uključujući društvene, prirodne ili tehničke znanosti",
        "region": "Brodsko-posavska županija"
    },
    {
        "academic_name": "SVEUČILIŠTE U SPLITU***",
        "number_of_students": 249,
        "study_field": "Različita studijska područja, uključujući društvene, prirodne ili tehničke znanosti",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "SVEUČILIŠTE U ZADRU",
        "number_of_students": 4807,
        "study_field": "Različita studijska područja, uključujući društvene, prirodne ili tehničke znanosti",
        "region": "Zadarska županija"
    },
    {
        "academic_name": "SVEUČILIŠTE U ZAGREBU***",
        "number_of_students": 489,
        "study_field": "Različita studijska područja, uključujući društvene, prirodne ili tehničke znanosti",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "TEHNIČKI FAKULTET, RIJEKA",
        "number_of_students": 1626,
        "study_field": "Tehničke znanosti",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "TEHNIČKO VELEUČILIŠTE, ZAGREB",
        "number_of_students": 4394,
        "study_field": "Tehničke znanosti",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "TEKSTILNO-TEHNOLOŠKI FAKULTET, ZAGREB",
        "number_of_students": 493,
        "study_field": "Tehničke znanosti",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "TEOLOŠKI FAKULTET 'MATIJA VLAČIĆ-ILIRIK', ZAGREB - EVANGELIČKI**",
        "number_of_students": 25,
        "study_field": "Teološke znanosti",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "UČITELJSKI FAKULTET, RIJEKA",
        "number_of_students": 566,
        "study_field": "Različita studijska područja, uključujući pedagoške, psihološke ili didaktičke discipline",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "UČITELJSKI FAKULTET, ZAGREB",
        "number_of_students": 2890,
        "study_field": "Različita studijska područja, uključujući pedagoške, psihološke ili didaktičke discipline",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "UMJETNIČKA AKADEMIJA, SPLIT",
        "number_of_students": 401,
        "study_field": "Umjetničke znanosti",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "VELEUČILIŠTE 'HRVATSKO ZAGORJE', KRAPINA",
        "number_of_students": 314,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Krapinsko-zagorska županija"
    },
    {
        "academic_name": "VELEUČILIŠTE 'LAVOSLAV RUŽIČKA' U VUKOVARU",
        "number_of_students": 921,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Vukovarsko-srijemska županija"
    },
    {
        "academic_name": "VELEUČILIŠTE 'MARKO MARULIĆ' U KNINU",
        "number_of_students": 273,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Šibensko-kninska županija"
    },
    {
        "academic_name": "VELEUČILIŠTE 'NIKOLA TESLA' U GOSPIĆU",
        "number_of_students": 198,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Ličko-senjska županija"
    },
    {
        "academic_name": "VELEUČILIŠTE ARCA, SPLIT",
        "number_of_students": 52,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "VELEUČILIŠTE ASPIRA, SPLIT",
        "number_of_students": 727,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Splitsko-dalmatinska županija"
    },
    {
        "academic_name": "VELEUČILIŠTE BALTAZAR, ZAPREŠIĆ",
        "number_of_students": 1432,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Zagrebačka županija"
    },
    {
        "academic_name": "VELEUČILIŠTE EDWARD BERNAYS, ZAGREB",
        "number_of_students": 335,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "VELEUČILIŠTE IVANIĆ-GRAD",
        "number_of_students": 166,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Zagrebačka županija"
    },
    {
        "academic_name": "VELEUČILIŠTE KRIMINALISTIKE I JAVNE SIGURNOSTI, ZAGREB",
        "number_of_students": 368,
        "study_field": "Kriminalistika i javna sigurnost",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "VELEUČILIŠTE PAR, RIJEKA",
        "number_of_students": 123,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "VELEUČILIŠTE RRIF, ZAGREB",
        "number_of_students": 120,
        "study_field": "Različita studijska područja, uključujući ekonomiju, financije i informatiku",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "VELEUČILIŠTE SUVREMENIH INFORMACIJSKIH TEHNOLOGIJA, ZAGREB",
        "number_of_students": 428,
        "study_field": "Informatičke znanosti",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "VELEUČILIŠTE U BJELOVARU",
        "number_of_students": 749,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Bjelovarsko-bilogorska županija"
    },
    {
        "academic_name": "VELEUČILIŠTE U KARLOVCU",
        "number_of_students": 1434,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Karlovačka županija"
    },
    {
        "academic_name": "VELEUČILIŠTE U KRIŽEVCIMA, KRIŽEVCI",
        "number_of_students": 337,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Koprivničko-križevačka županija"
    },
    {
        "academic_name": "VELEUČILIŠTE U RIJECI",
        "number_of_students": 1368,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Primorsko-goranska županija"
    },
    {
        "academic_name": "VELEUČILIŠTE U ŠIBENIKU",
        "number_of_students": 568,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Šibensko-kninska županija"
    },
    {
        "academic_name": "VELEUČILIŠTE U VELIKOJ GORICI",
        "number_of_students": 1159,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Zagrebačka županija" 
    },
    {
        "academic_name": "VELEUČILIŠTE U VIROVITICI",
        "number_of_students": 328,
        "study_field": "Različita studijska područja, uključujući tehničke, društvene ili humanističke discipline",
        "region": "Virovitičko-podravska županija"
    },
    {
        "academic_name": "VETERINARSKI FAKULTET, ZAGREB",
        "number_of_students": 1081,
        "study_field": "Veterinarska medicina",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "VISOKO EVANĐEOSKO TEOLOŠKO UČILIŠTE, OSIJEK",
        "number_of_students": 34,
        "study_field": "Teologija",
        "region": "Osječko-baranjska županija"
    },
    {
        "academic_name": "VISOKO UČILIŠTE ALGEBRA",
        "number_of_students": 1831,
        "study_field": "Računarstvo, informatika, matematika, ekonomija, financije i druge srodne discipline",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "ZAGREBAČKA ŠKOLA EKONOMIJE I MANAGEMENTA, ZAGREB",
        "number_of_students": 742,
        "study_field": "Ekonomija, menadžment i srodne discipline",
        "region": "Grad Zagreb"
    },
    {
        "academic_name": "ZDRAVSTVENO VELEUČILIŠTE, ZAGREB",
        "number_of_students": 4193,
        "study_field": "Zdravstvene znanosti i srodna područja",
        "region": "Grad Zagreb"
    }
]
'''

data = json.loads(json_data)

academic_fields = set()
total_students = 0
total_fields = 0
regions = set()

for academic_data in data:
    academic_fields.add(academic_data["study_field"])
    total_students += academic_data["number_of_students"]
    regions.add(academic_data["region"])

print("Academic Fields:")
for field in academic_fields:
    print(field)

print("\nRegions:")
for region in regions:
    print(region)

total_fields = len(academic_fields)
print("\nTotal number of academic fields:", total_fields)

print("\nTotal Students:", total_students)

print("\nTotal regions:", len(regions))
