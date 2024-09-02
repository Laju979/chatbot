import streamlit as st
import difflib

st.image('pexels-emmages-8445454.jpg')
def user_input(info):
    phrase = ['chappal waddi is the highest mountain of nigeria. what state is it located in?',
              'where is the highest mountain in nigeria?',
              'what is the capital of nigeria?', 'what is nigerias capital?',
              'nigeria is situated in western africa and has a coastal border on which body of water?',
              'what was the previous nigerian national anthem?',
              'what is the nigerian national anthem?'
              'what is the capital of abia state', 'what is the capital of abia'
              'what is the capital of adamawa state', 'what is the capital of adamawa'
              'what is the capital of akwa ibom state',
              'what is the capital of akwa ibom',
              'what is the capital of anambra state', 'what is the capital of anambra'
              'what is the capital of bauchi state',
              'what is the capital of bayelsa state',
              'what is the capital of benue state',
              'what is the capital of borno state',
              'what is the capital of cross river state',
              'what is the capital of delta state',
              'what is the capital of ebonyi state',
              'what is the capital of edo state',
              'what is the capital of ekiti state',
              'what is the capital of enugu state',
              'what is the capital of gombe state',
              'what is the capital of imo state',
              'what is the capital of jigawa state',
              'what is the capital of kaduna state',
              'what is the capital of kano state',
              'what is the capital of kano',
              'what is the capital of katsina state',
              'what is the capital of katsina',
              'what is the capital of kebbi state',
              'what is the capital of kebbi',
              'what is the capital of kogi state',
              'what is the capital of kogi',
              'what is the capital of kwara state',
              'what is the capital of kwara',
              'what is the capital of lagos state',
              'what is the capital of lagos',
              'what is the capital of nasarawa state',
              'what is the capital of nasarawa',
              'what is the capital of niger state',
              'what is the capital of niger',
              'what is the capital of ogun state',
              'what is the capital of ogun',
              'what is the capital of ondo state',
              'what is the capital of ondo',
              'what is the capital of osun state',
              'what is the capital of osun',
              'what is the capital of oyo state',
              'what is the capital of oyo',
              'what is the capital of plateau state',
              'what is the capital of plateau',
              'what is the capital of rivers state',
              'what is the capital of rivers',
              'what is the capital of sokoto state',
              'what is the capital of sokoto',
              'what is the capital of taraba state',
              'what is the capital of taraba',
              'what is the capital of yobe state',
              'what is the capital of yobe state',
              'what is the capital of zamfara state',
              'what is the capital of zamfara',
              'who was the first senate president of the fourth republic?',
              'most people in nigeria are from what religion?',
              'what is the most common religion in nigeria',
              'who were the first Sub-Saharan people to make intricate and life-size terracotta statues?',
              'what was General Babangidas position before becoming president?',
              'which is the largest state in nigeria',
              'how many states are there in nigeria',
              'what is the currency in nigeria',
              'when did nigeria adopt the use of the naira',
              'who was the captain of the super eagles when they won the afcon in 1994?',
              'who captained the Olympic gold medal winning team of 1996?',
              'what year did nigeria win an olympic gold medal',
              'what is the most popular sport in nigeria',
              'what is the most popular crime in nigeria',
              'what are the two colours on the nigerian flag',
              'when did nigeria gain her independence',
              'when is nigerias independence day',
              'what country colonised nigeria',
              'who was the first civilian Governor of Plateau State?',
              'who was the chief security officer under Gen. abacha?',
              'who is popularly referred to as maradona in nigeria?',
              '1 naira is divided into what',
              'nigerians wole soyinka, ben okri and chinua achebe have all achieved renown in which field?',
              'what is nigerias main resource',
              'zuma rock is located in what city',
              'who is nigerias first female author?',
              'who is the first nigerian female vice-chancellor?',
              'who founded nigerias first political party',
              'federal capital territory, abuja is in what geopolitical zone?',
              'which is the nigerian state with the largest land mass?',
              'which is the nigerian state with the greatest number of local government areas?',
              'which is the nigerian state with the highest population?',
              'which nigerian state has "light of the nation" as her slogan?',
              'what is the slogan of lagos state?',
              'what is the slogan of rivers state?',
              'what is the capital of osun state?',
              'what is the slogan of kano state?',
              'what is the capital of yobe state?',
              'what is the capital of zamfara state?',
              'What is the capital of Niger State?',
              'who is the first nigerian nationalist to move the motion of self government?',
              'what is the highest mountain in the world?',
              'what is the highest mountain in africa?',
              'who is the first governor of the defunct eastern region?',
              'which african country has the highest mountain in africa?',
              'what is the name of south african currency?',
              'what is the name of ghanaian currency?',
              'what is the name of nigerian currency?',
              'ibibio ethnic group is predominantly found in which state?',
              'nupe ethic group is predominantly found in which state?',
              'what is the minority group in anambra state?',
              'which state in nigeria is famous for blacksmith works?',
              'government of the people by the people and for the people is called?',
              'where is the headquarters of ecowas?',
              'how many states are in northern nigeria?',
              'how many states are in southern nigeria?',
              'who is the african slave boy that later became a bishop?',
              'when was naira and kobo introduced in nigeria?',
              'ajaokuta is famous for?',
              'what are the three arms of government in nigeria?',
              'which university is the oldest in nigeria?',
              'who is the first inspector-general of police?',
              'who is the current president of nigeria',
              'who wass the first military head of state to die in office?',
              'which state in nigeria has the least number of local government areas?',
              'which state in nigeria has food basket of the nation as her slogan?',
              'how many states are in nigeria?',
              'which political party is the ruling party in nigeria?',
              'which country won the hosting rights of the 2019 african cup Of nations?',
              'what is the first political party in nigeria?',
              'when was the nigerian first political party formed?',
              'nigeria was first visited by the white men from which country?',
              'who is the first executive president of nigeria?',
              'who is the first president of nigeria?',
              'who is the first military head Of state of nigeria?',
              'what is the ruling political party in delta state?',
              'which year did nigeria gain her independence?',
              'which year did nigeria become a republic?',
              'who amalgamated the northern and southern protectorates of nigeria?',
              'who gave named nigeria?',
              'when was nigeria amalgamated?',
              'when was nigerias second republic?',
              'who moved the first historic motion for nigerias independence?',
              'when was the first unsuccessful motion for nigerias independence moved?',
              'nigeria is intersected by which two major rivers?',
              'what are the colours of the nigerian flag?',
              'where is the name nigeria derived from?',
              'how many local government areas sre in nigeria'
              ]

    mp4 = difflib.get_close_matches(info.lower(), phrase, n=1, cutoff=0.5)

    if mp4:
        close_matches = mp4[0]
        if close_matches in ['chappal waddi is the highest mountain of nigeria. what state is it located in?']:
            return "Taraba State"
        elif close_matches in ['where is the highest mountain in nigeria?']:
            return "Taraba State"
        elif close_matches in ['what is the capital of nigeria?', 'what is nigerias capital?']:
            return "Abuja"
        elif close_matches in ['nigeria is situated in western africa and has a coastal border on which body of water?']:
            return "Gulf of Guinea"
        elif close_matches in ['what was the previous nigerian national anthem?']:
            return "Arise, O Compatriots which came about in 1978 and was changed in 2024"
        elif close_matches in ['what is the nigerian national anthem?']:
            return "Nigeria We Hail Thee"
        elif close_matches in ['what is the capital of abia state', 'what is the capital of abia']:
            return "Umuahia"
        elif close_matches in ['what is the capital of adamawa state', 'what is the capital of adamawa']:
            return "Yola"
        elif close_matches in ['what is the capital of akwa ibom state', 'what is the capital of akwa ibom']:
            return "Uyo"
        elif close_matches in ['what is the capital of anambra state', 'what is the capital of anambra']:
            return "Awka"
        elif close_matches in ['what is the capital of bauchi state', 'what is the capital of bauchi']:
            return "Bauchi"
        elif close_matches in ['what is the capital of bayelsa state', 'what is the capital of bayelsa']:
            return "Yenagoa "
        elif close_matches in ['what is the capital of benue state', 'what is the capital of benue']:
            return "Makurdi"
        elif close_matches in ['what is the capital of borno state', 'what is the capital of borno']:
            return "Maiduguri "
        elif close_matches in ['what is the capital of cross river state', 'what is the capital of cross river']:
            return "Calabar"
        elif close_matches in ['what is the capital of delta state', 'what is the capital of delta']:
            return "Asaba"
        elif close_matches in ['what is the capital of ebonyi state', 'what is the capital of ebonyi']:
            return "Abakaliki"
        elif close_matches in ['what is the capital of edo state', 'what is the capital of edo']:
            return "Benin City"
        elif close_matches in ['what is the capital of ekiti state', 'what is the capital of ekiti']:
            return "Ekiti"
        elif close_matches in ['what is the capital of enugu state', 'what is the capital of enugu']:
            return "Enugu"
        elif close_matches in ['what is the capital of gombe state', 'what is the capital of gombe']:
            return "Gombe"
        elif close_matches in ['what is the capital of imo state', 'what is the capital of imo']:
            return "Owerri"
        elif close_matches in ['what is the capital of jigawa state', 'what is the capital of jigawa']:
            return "Dutse "
        elif close_matches in ['what is the capital of kaduna state', 'what is the capital of kaduna']:
            return "Kaduna"
        elif close_matches in ['what is the capital of kano state', 'what is the capital of kano']:
            return "Kano"
        elif close_matches in ['what is the capital of katsina state', 'what is the capital of katsina']:
            return "Katsina"
        elif close_matches in ['what is the capital of kebbi state', 'what is the capital of kebbi']:
            return "Birnin Kebbi"
        elif close_matches in ['what is the capital of kogi state', 'what is the capital of kogi']:
            return "Lokoja"
        elif close_matches in ['what is the capital of kwara state', 'what is the capital of kwara']:
            return "Ilorin"
        elif close_matches in ['what is the capital of lagos state', 'what is the capital of lagos']:
            return "Ikeja"
        elif close_matches in ['what is the capital of nasarawa state', 'what is the capital of nasarawa']:
            return "Lafia"
        elif close_matches in ['what is the capital of niger state', 'what is the capital of niger']:
            return "Minna"
        elif close_matches in ['what is the capital of ogun state', 'what is the capital of ogun']:
            return "Abeokuta"
        elif close_matches in ['what is the capital of ondo state', 'what is the capital of ondo']:
            return "Akure"
        elif close_matches in ['what is the capital of osun state', 'what is the capital of osun']:
            return "Oshogbo"
        elif close_matches in ['what is the capital of oyo state', 'what is the capital of oyo']:
            return "Ibadan"
        elif close_matches in ['what is the capital of plateau state', 'what is the capital of plateau']:
            return "Jos"
        elif close_matches in ['what is the capital of rivers state', 'what is the capital of rivers']:
            return "Port Harcourt"
        elif close_matches in ['what is the capital of sokoto state', 'what is the capital of sokoto']:
            return "Sokoto"
        elif close_matches in ['what is the capital of taraba state', 'what is the capital of taraba']:
            return "Jalingo"
        elif close_matches in ['what is the capital of yobe state', 'what is the capital of yobe state']:
            return "Damaturu"
        elif close_matches in ['what is the capital of zamfara state', 'what is the capital of zamfara']:
            return "Gusau"
        elif close_matches in ['who was the first senate president of the fourth republic?']:
            return "Evan Enwerem"
        elif close_matches in ['most people in nigeria are from what religion?']:
            return "islam"
        elif close_matches in ['what is the most common religion in nigeria']:
            return "islam"
        elif close_matches in ['who were the first Sub-Saharan people to make intricate and life-size terracotta statues?']:
            return "Nok"
        elif close_matches in ['what was General Babangidas position before becoming president?']:
            return "Chief of Army Staff"
        elif close_matches in ['which is the largest state in nigeria']:
            return "Niger State"
        elif close_matches in ['how many states are there in nigeria']:
            return "36"
        elif close_matches in ['what is the currency in nigeria']:
            return "Naira"
        elif close_matches in ['when did nigeria adopt the use of the naira']:
            return "1973"
        elif close_matches in ['who was the captain of the super eagles when they won the afcon in 1994?']:
            return "Stephen Keshi"
        elif close_matches in ['who captained the Olympic gold medal winning team of 1996?']:
            return "Nwankwo Kanu"
        elif close_matches in ['what year did nigeria win an olympic gold medal']:
            return "1996"
        elif close_matches in ['what is the most popular sport in nigeria']:
            return "Football"
        elif close_matches in ['what is the most popular crime in nigeria']:
            return "Fraud"
        elif close_matches in ['what are the two colours on the nigerian flag']:
            return "Green & White"
        elif close_matches in ['when did nigeria gain her independence']:
            return "1960"
        elif close_matches in ['when is nigerias independence day']:
            return "1st Oct every year"
        elif close_matches in ['what country colonised nigeria']:
            return "The United Kingdom"
        elif close_matches in ['who was the first civilian Governor of Plateau State?']:
            return "Solomon Lar"
        elif close_matches in ['who was the chief security officer under Gen. abacha?']:
            return "Major Hamza Al-Mustapha"
        elif close_matches in ['who is popularly referred to as maradona in nigeria?']:
            return "Ibrahim Babangida"
        elif close_matches in ['who is the current president of nigeria']:
            return "Bola Ahmed Tinubu (B.A.T)"
        elif close_matches in ['1 naira is divided into what']:
            return "100 kobo"
        elif close_matches in ['nigerians wole soyinka, ben okri and chinua achebe have all achieved renown in which field?']:
            return "Literature"
        elif close_matches in ['what is nigerias main resource']:
            return "Oil"
        elif close_matches in ['zuma rock is located in what city']:
            return "Abuja"
        elif close_matches in ['who is nigerias first female author?']:
            return "Flora Nwapa"
        elif close_matches in ['who is the first nigerian female vice-chancellor?']:
            return "Prof. Grace Alele Williams"
        elif close_matches in ['who founded nigerias first political party']:
            return "Herbert Macaulay"
        elif close_matches in ['federal capital territory, abuja is in what geopolitical zone?']:
            return "North Central"
        elif close_matches in ['which is the nigerian state with the largest land mass?']:
            return "Niger"
        elif close_matches in ['which is the nigerian state with the greatest number of local government areas?']:
            return "Kano(44 LGAs)"
        elif close_matches in ['which is the nigerian state with the highest population?']:
            return "Kano State"
        elif close_matches in ['which nigerian state has "light of the nation" as her slogan?']:
            return "Anambra State"
        elif close_matches in ['what is the slogan of lagos state?']:
            return "Centre of Excellence"
        elif close_matches in ['what is the slogan of rivers state?']:
            return "Treasure Base of the Nation"
        elif close_matches in ['what is the capital of osun state?']:
            return "Osogbo"
        elif close_matches in ['what is the slogan of kano state?']:
            return "Centre of Commerce"
        elif close_matches in ['what is the capital of yobe state?']:
            return "Damaturu"
        elif close_matches in ['what is the capital of zamfara state?']:
            return "Gusau"
        elif close_matches in ['What is the capital of Niger State?']:
            return "Minna"
        elif close_matches in ['who is the first nigerian nationalist to move the motion of self government?']:
            return "Pa Anthony Enahoro"
        elif close_matches in ['what is the highest mountain in the world?']:
            return "Mount Everest"
        elif close_matches in ['what is the highest mountain in africa?']:
            return "Mount Kilimanjaro"
        elif close_matches in ['who is the first governor of the defunct eastern region?']:
            return "Francis Akanu Ibiam"
        elif close_matches in ['which african country has the highest mountain in africa?']:
            return "Tanzania"
        elif close_matches in ['what is the name of south african currency?']:
            return "Rand"
        elif close_matches in ['what is the name of ghanaian currency?']:
            return "Cedi"
        elif close_matches in ['what is the name of nigerian currency?']:
            return "Naira"
        elif close_matches in ['ibibio ethnic group is predominantly found in which state?']:
            return "Akwa Ibom State"
        elif close_matches in ['nupe ethic group is predominantly found in which state?']:
            return "Niger State"
        elif close_matches in ['what is the minority group in anambra state?']:
            return "Igala"
        elif close_matches in ['which state in nigeria is famous for blacksmith works?']:
            return "Anambra state"
        elif close_matches in ['government of the people by the people and for the people is called?']:
            return "Democracy"
        elif close_matches in ['where is the headquarters of ecowas?']:
            return "Abuja, Nigeria"
        elif close_matches in ['what town in nigeria is famous for plywood production?']:
            return "Sapele"
        elif close_matches in ['how many states are in northern nigeria?']:
            return "19"
        elif close_matches in ['how many states are in southern nigeria?']:
            return "17"
        elif close_matches in ['who is the african slave boy that later became a bishop?']:
            return "Samuel Ajayi Crowther"
        elif close_matches in ['when was naira and kobo introduced in nigeria?']:
            return "1973"
        elif close_matches in ['ajaokuta is famous for?']:
            return "Iron and Steel"
        elif close_matches in ['what are the three arms of government in nigeria?']:
            return "Executive, Judiciary and Legislative"
        elif close_matches in ['which university is the oldest in nigeria?']:
            return "University of Ibadan( founded in 1948)"
        elif close_matches in ['who is the first inspector-general of police?']:
            return "Louis Edet"
        elif close_matches in ['who is the current president of nigeria']:
            return "Bola Ahmed Tinubu (B.A.T)"
        elif close_matches in ['who wass the first military head of state to die in office?']:
            return "General J.T.U Aguiyi Ironsi"
        elif close_matches in ['which state in nigeria has the least number of local government areas?']:
            return " Bayelsa state( 8 LGAs)"
        elif close_matches in ['which state in nigeria has food basket of the nation as her slogan?']:
            return "Benue State"
        elif close_matches in ['how many states are in nigeria?']:
            return "36"
        elif close_matches in ['which political party is the ruling party in nigeria?']:
            return " All Progressive Congress (APC)"
        elif close_matches in ['which country won the hosting rights of the 2019 african cup Of nations?']:
            return "Egypt"
        elif close_matches in ['what is the first political party in nigeria?']:
            return " Nigerian National Democratic Party"
        elif close_matches in ['when was the nigerian first political party formed?']:
            return "1923"
        elif close_matches in ['nigeria was first visited by the white men from which country?']:
            return "Portugal"
        elif close_matches in ['who is the first executive president of nigeria?']:
            return "Alhaji Shehu Shagari"
        elif close_matches in ['who is the first president of nigeria?']:
            return " Dr. Nnamdi Azikwe"
        elif close_matches in ['who is the first military head Of state of nigeria?']:
            return "Aguiyi Ironsi"
        elif close_matches in ['what is the ruling political party in delta state?']:
            return " Peoples Democratic Party (PDP)"
        elif close_matches in ['which year did nigeria gain her independence?']:
            return "1960"
        elif close_matches in ['which year did nigeria become a republic?']:
            return "1963"
        elif close_matches in ['who amalgamated the northern and southern protectorates of nigeria?']:
            return "Sir Lord Lugard"
        elif close_matches in ['who gave named nigeria?']:
            return "Ms Flora Shaw"
        elif close_matches in ['when was nigeria amalgamated?']:
            return "1914"
        elif close_matches in ['when was nigerias second republic?']:
            return "1979-1983"
        elif close_matches in ['who moved the first historic motion for nigerias independence?']:
            return "Pa Anthony Enahoro"
        elif close_matches in ['when was the first unsuccessful motion for nigerias independence moved?']:
            return "1953"
        elif close_matches in ['nigeria is intersected by which two major rivers?']:
            return "River Niger and River Benue"
        elif close_matches in ['what are the colours of the nigerian flag?']:
            return "Green and white"
        elif close_matches in ['where is the name nigeria derived from?']:
            return "River Niger"
        elif close_matches in ['how many local government areas sre in nigeria']:
            return "774"
        elif close_matches in ['minister of art, culture and the creative economy']:
            return "HON. HANNATU MUSAWA"
        elif close_matches in ['minister of defence']:
            return "HON. MOHAMMED BADARU"
        elif close_matches in ['minister of state, defence']:
            return " HON. BELLO MATAWALLE"
        elif close_matches in ['minister of education']:
            return "HON. TAHIR MAMAN"
        elif close_matches in ['minister of state, education']:
            return "HON. YUSUF T. SUNUNU"
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""
        elif close_matches in ['']:
            return ""



st.header('ASK ABOUT NIGERIA')
poop = st.text_input('Laju')

if poop:
    response = user_input(poop)
    st.write(f'Laju: {response}')
