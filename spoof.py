import random

def random_string(arr):
    return random.choice(arr)

acnemedications =['doxycycline', 'spironolactone', 'minocycline', 'Accutane',
       'clindamycin', 'Aldactone', 'tretinoin', 'isotretinoin', 'Bactrim',
       'Retin-A', 'Aczone', 'benzoyl peroxide', 'Differin', 'Epiduo',
       'adapalene', 'cephalexin', 'Doryx', 'tetracycline', 'Septra',
       'Solodyn', 'Tazorac', 'Vibramycin', 'Acticlate',
       'benzoyl peroxide / clindamycin', 'Doxy 100', 'Keflex',
       'sulfamethoxazole / trimethoprim', 'Benzaclin', 'Monodox',
       'Targadox', 'Adoxa', 'Adoxa CK', 'Adoxa Pak', 'Adoxa TT',
       'Avidoxy', 'Bactrim DS', 'Cleocin T', 'Clindagel', 'Doryx MPC',
       'erythromycin', 'Morgidox', 'Oraxyl', 'Claravis', 'Clinda-Derm',
       'Evoclin', 'Minocin', 'Yaz', 'adapalene / benzoyl peroxide',
       'Clindacin ETZ', 'Clindacin P', 'Clindacin PAC',
       'ClindaReach Pledget', 'Clindets', 'Milk of Magnesia', 'Septra DS',
       'Yasmin', 'Ziana', 'Absorica', 'Acanya', 'Amnesteem',
       'azelaic acid', 'Co-trimoxazole', 'dapsone', 'Duac', 'Emcin Clear',
       'Epiduo Forte', 'Erygel', 'Ery Pads', 'Myorisan', 'Onexton',
       "Phillips' Milk of Magnesia", 'salicylic acid', 'Spotex',
       'Theramycin Z', 'Absorica LD', 'Achromycin V', 'Acne Treatment',
       'Acnex', 'Ala-Tet', 'Amzeeq', 'Atralin', 'Avita', 'Azelex',
       'Benzamycin', 'benzoyl peroxide / erythromycin',
       'benzoyl peroxide / sulfur', 'Beyaz', 'Brodspec', 'Cleeravue-M',
       'clindamycin / tretinoin', 'drospirenone / ethinyl estradiol',
       'Dynacin', 'Estarylla', 'ethinyl estradiol / norgestimate',
       'Gianvi', 'Loryna', 'magnesium hydroxide', 'Minolira', 'Ocella',
       'PanOxyl', 'PanOxyl 10% Acne Foaming Wash', 'Seysara', 'Sotret',
       'sulfacetamide sodium/sulfur', 'tazarotene', 'Tri-Previfem',
       'Tri-Sprintec', 'Veltin', 'Ximino', 'Zenatane', 'Acetoxyl',
       'Acne-10', 'Acne-Clear', 'Acnevir', 'Acnomel', 'Acnomel Acne Mask',
       'Acnomel BP 5', 'Aklief', 'Aktipak', 'Akurza', 'Aliclen',
       'Alquam-X Acne Therapy Gel', 'Altabax', 'Altreno', 'Arazlo',
       'Avar', 'Avar-E', 'Avar-E Green', 'Avar-E LS', 'Avar Cleanser',
       'Avar LS', 'Avar LS Cleanser', 'Benzac', 'Benzac AC',
       'Benzac AC Wash', 'Benzac W', 'Benzagel', 'Benzagel Wash',
       'Benzamycin Pak', 'Benzashave', 'BenzEFoam Ultra', 'BenzePro',
       'Benziq', 'benzoyl peroxide / hydrocortisone',
       'benzoyl peroxide / salicylic acid',
       'benzoyl peroxide / tretinoin', 'Binora', 'BP 10-Wash',
       'BPO 6 Foaming Cloths', 'BPO Gel', 'BP Wash', 'Brevoxyl',
       'Brevoxyl Acne Wash Kit', 'CeraVe SA Renewing', 'Clarifoam EF',
       'clascoterone', 'Cleanse & Treat', 'Cleanse & Treat Plus',
       'Clearskin', 'Compound W', 'DermalZone', 'DHS Salicylic Acid 3%',
       'drospirenone / ethinyl estradiol / levomefolate calcium',
       'Dulcolax Milk of Magnesia', 'Durasal', 'Enzoclear Foam',
       'ethinyl estradiol / norethindrone', 'Ex-Lax Milk of Magnesia',
       'Fabior', 'Fostex', 'Fostex Medicated',
       'Fostex Medicated Cleansing Cream', 'Fostex Wash 10%',
       'Hydrisalic', 'Inova', 'Inova 4/1', 'Inova 8/2', 'Jasmiel',
       'Liquimat Light', 'Liquimat Medium', 'Lo-Zumandimine', 'Meted',
       'Mono-Linyah', 'Neuac', 'Neutrogena Clear Pore Cleanser/Mask',
       'Neutrogena Rapid Clear Stubborn Acne', 'Nikki', 'Oscion',
       'Oxy-10', 'Oxy Daily Wash', 'P & S', 'PanOxyl 4% Acne Creamy Wash',
       'Pernox', 'Persa-Gel', 'Plexion', 'Propa pH Acne Med Cleansing',
       'R A Acne', 'Resinol', 'resorcinol / sulfur', 'resorcinol',
       'retapamulin', 'Riax', 'Sal-Plant Gel', 'Salactic Film', 'Salex',
       'salicylic acid/sulfur', 'Salvax', 'sarecycline', 'SAStid',
       'Scalpicin Scalp Relief', 'Sebulex', 'SoluCLENZ Rx', 'SSS 10-4',
       'SSS 10-5', 'SSS Cleanser', 'Stri-Dex', 'Stridex Body Focus',
       'Stridex Maximum Strength', 'Sulfacleanse 8/4', 'Sulfoam',
       'sulfur', 'Sulpho-Lac Soap', 'Sumadan', 'Sumaxin', 'Suphera',
       'Syeda', 'Tinamed Plantar', 'Tri-Estarylla', 'Tri-Linyah',
       'Tri-Lo-Marzia', 'trifarotene', 'Twyneo', 'Vanoxide-HC', 'Winlevi',
       'Z-Clinz 10', 'Zarah', 'Zumandimine', 'levothyroxine', 'Synthroid',
       'Armour Thyroid', 'Levoxyl', 'Cytomel', 'Tirosint', 'Euthyrox',
       'liothyronine', 'Nature-Throid', 'Unithroid', 'Westhroid',
       'Levo-T', 'Thyquidity', 'Tirosint-Sol', 'NP Thyroid', 'Triostat',
       'WP Thyroid', 'sumatriptan', 'Imitrex', 'Zomig', 'Cambia',
       'Nurtec ODT', 'zolmitriptan', 'rizatriptan', 'Maxalt', 'Reyvow',
       'Elyxyb', 'lasmiditan', 'rimegepant', 'Tosymra', 'Relpax',
       'Excedrin Migraine', 'Amerge', 'cyclobenzaprine', 'Fiorinal',
       'Treximet', 'Maxalt-MLT', 'diclofenac', 'Ubrelvy', 'naratriptan',
       'aspirin / butalbital / caffeine', 'Frova', 'eletriptan',
       'Excedrin', 'almotriptan', 'naproxen / sumatriptan',
       'acetaminophen / aspirin / caffeine', 'Imitrex Statdose',
       'Methergine', 'Migranal',
       'acetaminophen / aspirin / caffeine / salicylamide', 'Cafergot',
       'dihydroergotamine', 'frovatriptan', 'Migergot', 'orphenadrine',
       'Zembrace SymTouch', 'Zomig-ZMT', 'caffeine / ergotamine',
       'celecoxib', 'D.H.E. 45', 'Ergomar', 'ergotamine',
       'methylergonovine', 'Onzetra Xsail', 'Painaid', 'Vanquish',
       'Zomig Nasal Spray', 'Anacin Advanced Headache Formula',
       'Backaid Inflammatory Pain Formula', 'Fortabs', 'Genace',
       "Goody's Extra-Strength Headache Powders",
       "Goody's Extra Strength", "Goody's Headache Powders",
       'Migraine Relief', 'Trudhesa', 'ubrogepant', 'cefotaxime',
       'metronidazole', 'vancomycin', 'cefepime', 'ceftazidime', 'Flagyl',
       'amikacin', 'Ancef', 'Zyvox', 'Cleocin', 'Flagyl IV', 'linezolid',
       'piperacillin / tazobactam', 'Zosyn', 'cefazolin', 'Cleocin HCl',
       'Cleocin Pediatric', 'Cleocin Phosphate', 'Flagyl 375',
       'tobramycin', 'aztreonam', 'ertapenem', 'Garamycin', 'gentamicin',
       'Invanz', 'Maxipime', 'Penicillin VK', 'penicillin v potassium',
       'Teflaro', 'tigecycline', 'Tygacil', 'Vancocin', 'Vancocin HCl',
       'Vancocin HCl Pulvules', 'Amikin', 'Amikin Pediatric',
       'ampicillin / sulbactam', 'avibactam / ceftazidime', 'Avycaz',
       'Azactam', 'BACiiM', 'bacitracin', 'Baxdela', 'Bicillin C-R',
       'Bicillin C-R 900/300', 'Cefotan', 'cefotetan', 'cefoxitin',
       'ceftaroline', 'ceftolozane / tazobactam', 'Claforan',
       'delafloxacin', 'Fortaz', 'lefamulin', 'nafcillin', 'Nuzyra',
       'omadacycline', 'oxacillin',
       'penicillin g benzathine / procaine penicillin',
       'penicillin g potassium', 'penicillin g sodium', 'Pfizerpen',
       'piperacillin', 'procaine penicillin', 'Tazicef', 'telavancin',
       'Tobi', 'Unasyn', 'Vibativ', 'Xenleta', 'Zerbaxa', 'Humira',
       'Stelara', 'ustekinumab', 'adalimumab', 'Cosentyx', 'Taltz',
       'Skyrizi', 'Tremfya', 'Ilumya', 'Avsola', 'Duobrii', 'guselkumab',
       'halobetasol / tazarotene', 'Inflectra', 'ixekizumab', 'Renflexis',
       'risankizumab', 'secukinumab', 'tildrakizumab', 'calcipotriene',
       'Dovonex', 'acitretin', 'betamethasone', 'Soriatane', 'Taclonex',
       'betamethasone / calcipotriene', 'Neoral', 'Otrexup', 'Trexall',
       'Enstilar', 'Rasuvo', 'tacrolimus', 'calcitriol', 'coal tar',
       'prednisolone', 'RediTrex', 'Taclonex Scalp', 'Vectical',
       'Gengraf', 'Oxsoralen-Ultra', 'Psoriasin', 'Sernivo', 'Abrilada',
       'Amjevita', 'Analpram-HC', 'Analpram E', 'Anthraforte',
       'anthralin', 'Anthrascalp', 'Balnetar', 'Betatar Gel',
       'brodalumab', 'Bryhali', 'Calcitrene',
       'coal tar/salicylic acid/sulfur', 'coal tar/salicylic acid',
       'Cutar', 'Cyltezo', 'DHS Tar Shampoo', 'Doak Tar', 'Dritho-Scalp',
       'Drithocreme', 'Elta Tar', 'Epifoam', 'Estar', 'Fototar',
       'Hadlima', 'Hulio', 'hydrocortisone / pramoxine', 'hydroxyurea',
       'Hyrimoz', 'Impoyz', 'Ionil T', 'Ixifi', 'Kalosar', 'Medotar',
       'methoxsalen', 'MG217 Medicated Tar', 'Neutrogena T/Derm',
       'Neutrogena T/Gel', 'Novacort', 'Oxipor VHC', 'Pramosone',
       'Proctofoam HC', 'Scytera', 'Siliq', 'Sorilux', 'Tarsum',
       'Theraplex T', 'Wynzora', 'Yusimry', 'Zithranol', 'Zithranol-RR']

random_value = random.choice(acnemedications)
print(random_value)