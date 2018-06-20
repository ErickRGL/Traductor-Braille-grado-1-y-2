#!/usr/bin/env python3

"""Modulo para manejar braille"""

# Tabla general de signos generadores.
# Es un diccionario, diseñado para ser buscad
# en el formato específico de "números en orden,
# sólo los que aparecen", e.g., "123".
tabla_signos = {
    "0" : "⠀",
    "1": "⠁",
    "2" : "⠂",
    "3" : "⠄",
    "4" : "⠈",
    "5" : "⠐",
    "6" : "⠠",
    "56" : "⠰",
    "15" : "⠑",
    "16" : "⠡",
    "156" : "⠱",
    "25" : "⠒",
    "26" : "⠢",
    "256" : "⠲",
    "12" : "⠃",
    "125" : "⠓",
    "126" : "⠣",
    "1256" : "⠳",
    "35" : "⠔",
    "36" : "⠤",
    "356" : "⠴",
    "13" : "⠅",
    "135" : "⠕",
    "136" : "⠥",
    "1356" : "⠵",
    "23" : "⠆",
    "235" : "⠖",
    "236" : "⠦",
    "2356" : "⠶",
    "123" : "⠇",
    "1235" : "⠗",
    "1236" : "⠧",
    "12356" : "⠷",
    "45" : "⠘",
    "46" : "⠨",
    "456" : "⠸",
    "14" : "⠉",
    "145" : "⠙",
    "146" : "⠩",
    "1456" : "⠹",
    "24" : "⠊",
    "245" : "⠚",
    "246" : "⠪",
    "2456" : "⠺",
    "124" : "⠋",
    "1245" : "⠛",
    "1246" : "⠫",
    "12456" : "⠻",
    "34" : "⠌",
    "345" : "⠜",
    "346" : "⠬",
    "3456" : "⠼",
    "134" : "⠍",
    "1345" : "⠝",
    "1346" : "⠭",
    "13456" : "⠽",
    "234" : "⠎",
    "2345" : "⠞",
    "2346" : "⠮",
    "23456" : "⠾",
    "1234" : "⠏",
    "12345" : "⠟",
    "12346" : "⠯",
    "123456" : "⠿",
}

def getPuntos(n):
    """Obtiene un signo generador con puntos
    específicos buscados en la tabla de signos general."""

    if not (isinstance(n, str)):
        n = str(n)
    
    if not (n in tabla_signos):
        raise LookupError("Signo generador buscado no en la tabla")
    else: 
        return tabla_signos[n]

# Tabla de traducción
tabla_trans = {
    ' ' : tabla_signos["0"],
    'a' : tabla_signos["1"],
    'b' : tabla_signos["12"],
    'c' : tabla_signos["14"],
    'd' : tabla_signos["145"],
    'e' : tabla_signos["15"],
    'f' : tabla_signos["124"],
    'g' : tabla_signos["1245"],
    'h' : tabla_signos["125"],
    'i' : tabla_signos["24"],
    'j' : tabla_signos["245"],
    'k' : tabla_signos["13"],
    'l' : tabla_signos["123"],
    'm' : tabla_signos["134"],
    'n' : tabla_signos["1345"],
    'ñ' : tabla_signos["12456"],
    'o' : tabla_signos["135"],
    'p' : tabla_signos["1234"],
    'q' : tabla_signos["12345"],
    'r' : tabla_signos["1235"],
    's' : tabla_signos["234"],
    't' : tabla_signos["2345"],
    'u' : tabla_signos["136"],
    'v' : tabla_signos["1236"],
    'w' : tabla_signos["2456"],
    'x' : tabla_signos["1346"],
    'y' : tabla_signos["12456"],
    'z' : tabla_signos["1356"],
    'á' : tabla_signos["12356"],
    'é' : tabla_signos["2346"],
    'í' : tabla_signos["34"],
    'ó' : tabla_signos["346"],
    'ú' : tabla_signos["23456"],
    'ü' : tabla_signos["1256"],

    'A' : tabla_signos["46"] + tabla_signos["1"],
    'B' : tabla_signos["46"] + tabla_signos["12"],
    'C' : tabla_signos["46"] + tabla_signos["14"],
    'D' : tabla_signos["46"] + tabla_signos["145"],
    'E' : tabla_signos["46"] + tabla_signos["15"],
    'F' : tabla_signos["46"] + tabla_signos["124"],
    'G' : tabla_signos["46"] + tabla_signos["1245"],
    'H' : tabla_signos["46"] + tabla_signos["125"],
    'I' : tabla_signos["46"] + tabla_signos["24"],
    'J' : tabla_signos["46"] + tabla_signos["245"],
    'K' : tabla_signos["46"] + tabla_signos["13"],
    'L' : tabla_signos["46"] + tabla_signos["123"],
    'M' : tabla_signos["46"] + tabla_signos["134"],
    'N' : tabla_signos["46"] + tabla_signos["1345"],
    'Ñ' : tabla_signos["46"] + tabla_signos["12456"],
    'O' : tabla_signos["46"] + tabla_signos["135"],
    'P' : tabla_signos["46"] + tabla_signos["1234"],
    'Q' : tabla_signos["46"] + tabla_signos["12345"],
    'R' : tabla_signos["46"] + tabla_signos["1235"],
    'S' : tabla_signos["46"] + tabla_signos["234"],
    'T' : tabla_signos["46"] + tabla_signos["2345"],
    'U' : tabla_signos["46"] + tabla_signos["136"],
    'V' : tabla_signos["46"] + tabla_signos["1236"],
    'W' : tabla_signos["46"] + tabla_signos["2456"],
    'X' : tabla_signos["46"] + tabla_signos["1346"],
    'Y' : tabla_signos["46"] + tabla_signos["12456"],
    'Z' : tabla_signos["46"] + tabla_signos["1356"],
    'Á' : tabla_signos["46"] + tabla_signos["12356"],
    'É' : tabla_signos["46"] + tabla_signos["2346"],
    'Í' : tabla_signos["46"] + tabla_signos["34"],
    'Ó' : tabla_signos["46"] + tabla_signos["346"],
    'Ú' : tabla_signos["46"] + tabla_signos["23456"],
    'Ü' : tabla_signos["46"] + tabla_signos["1256"],

    '1' : tabla_signos["3456"] + tabla_signos["1"],
    '2' : tabla_signos["3456"] + tabla_signos["12"],
    '3' : tabla_signos["3456"] + tabla_signos["14"],
    '4' : tabla_signos["3456"] + tabla_signos["145"],
    '5' : tabla_signos["3456"] + tabla_signos["15"],
    '6' : tabla_signos["3456"] + tabla_signos["124"],
    '7' : tabla_signos["3456"] + tabla_signos["1245"],
    '8' : tabla_signos["3456"] + tabla_signos["125"],
    '9' : tabla_signos["3456"] + tabla_signos["24"],
    '0' : tabla_signos["3456"] + tabla_signos["245"],

    '.' : tabla_signos["3"],
    ',' : tabla_signos["2"],
    ':' : tabla_signos["25"],
    ';' : tabla_signos["23"],
    '€' : tabla_signos["456"] + tabla_signos["15"],
    '$' : tabla_signos["456"] + tabla_signos["234"], # Dolar, no peso
    #'$' : tabla_signos["456"] + tabla_signos["1234"] + tabla_signos["234"], # Peso Mexicano
    '#' : tabla_signos["3456"],
    '=' : tabla_signos["2356"],
    '÷' : tabla_signos["256"],
    '<' : tabla_signos["246"],
    #'>' : tabla_signos["135"], #es igual a la o
    '¿' : tabla_signos["26"],
    '?' : tabla_signos["26"],
    "¡" : tabla_signos["235"],
    "!" : tabla_signos["235"],
    '-' : tabla_signos["36"],
    '&' : tabla_signos["12346"],
    '*' : tabla_signos["35"],
    '(' : tabla_signos["126"],
    ')' : tabla_signos["345"],
    '"' : tabla_signos["236"],
    '+' : tabla_signos["235"],
    '÷' : tabla_signos["256"],
}

# Tabla de traducción
tabla_trans_grado2 = {
    ' ' : tabla_signos["0"],
    'a' : tabla_signos["1"],
    'b' : tabla_signos["12"],
    'c' : tabla_signos["14"],
    'd' : tabla_signos["145"],
    'e' : tabla_signos["15"],
    'f' : tabla_signos["124"],
    'g' : tabla_signos["1245"],
    'h' : tabla_signos["125"],
    'i' : tabla_signos["24"],
    'j' : tabla_signos["245"],
    'k' : tabla_signos["13"],
    'l' : tabla_signos["123"],
    'm' : tabla_signos["134"],
    'n' : tabla_signos["1345"],
    'ñ' : tabla_signos["12456"],
    'o' : tabla_signos["135"],
    'p' : tabla_signos["1234"],
    'q' : tabla_signos["12345"],
    'r' : tabla_signos["1235"],
    's' : tabla_signos["234"],
    't' : tabla_signos["2345"],
    'u' : tabla_signos["136"],
    'v' : tabla_signos["1236"],
    'w' : tabla_signos["2456"],
    'x' : tabla_signos["1346"],
    'y' : tabla_signos["12456"],
    'z' : tabla_signos["1356"],
    'á' : tabla_signos["12356"],
    'é' : tabla_signos["2346"],
    'í' : tabla_signos["34"],
    'ó' : tabla_signos["346"],
    'ú' : tabla_signos["23456"],
    'ü' : tabla_signos["1256"],

    '1' : tabla_signos["3456"] + tabla_signos["1"],
    '2' : tabla_signos["3456"] + tabla_signos["12"],
    '3' : tabla_signos["3456"] + tabla_signos["14"],
    '4' : tabla_signos["3456"] + tabla_signos["145"],
    '5' : tabla_signos["3456"] + tabla_signos["15"],
    '6' : tabla_signos["3456"] + tabla_signos["124"],
    '7' : tabla_signos["3456"] + tabla_signos["1245"],
    '8' : tabla_signos["3456"] + tabla_signos["125"],
    '9' : tabla_signos["3456"] + tabla_signos["24"],
    '0' : tabla_signos["3456"] + tabla_signos["245"],

    '.' : tabla_signos["3"],
    ',' : tabla_signos["2"],
    ':' : tabla_signos["25"],
    ';' : tabla_signos["23"],
    '€' : tabla_signos["456"] + tabla_signos["15"],
    '$' : tabla_signos["456"] + tabla_signos["234"], # Dolar, no peso
    '#' : tabla_signos["3456"],
    '=' : tabla_signos["2356"],
    '÷' : tabla_signos["256"],
    '<' : tabla_signos["246"],
    #'>' : tabla_signos["135"], #es igual a la o
    '¿' : tabla_signos["26"],
    '?' : tabla_signos["26"],
    "¡" : tabla_signos["235"],
    "!" : tabla_signos["235"],
    '-' : tabla_signos["36"],
    '&' : tabla_signos["12346"],
    '*' : tabla_signos["35"],
    '(' : tabla_signos["126"],
    ')' : tabla_signos["345"],
    '"' : tabla_signos["236"],
    '+' : tabla_signos["235"],
    '÷' : tabla_signos["256"],

    'â' : tabla_signos["16"],#caracter especial
    'ê' : tabla_signos["126"],#caracter especial
    'î' : tabla_signos["146"],#caracter especial
    'ô' : tabla_signos["1456"],#caracter especial
    'û' : tabla_signos["156"],#caracter especial

    'ë' : tabla_signos["1246"],#caracter especial
    'ï' : tabla_signos["12456"],#caracter especial
    'ü' : tabla_signos["1256"],#caracter especial

    '»' : tabla_signos["356"],#caracter especial
    'ψ' : tabla_signos["13456"],#caracter especial
}

# Tabla de traducción grado 2
tabla_trans2 = {

    " abajo " : " aj ",
    " absoluto " : " {a}{b} ",
    " acaso " : " ac ",
    " acción " : " a# ",
    " acerca " : " acc ",
    " adelante " : " adl ",
    " además " : " adm ",
    " ahora " : " ah ",
    " algo " : " alg ",
    " alguien " : " algn ",
    " algún " : " aln ",
    " alguno " : " alno ",
    " alguna " : " alna ",
    " alrededor " : " alr ",
    " anterior " : " {a}{n}{t}{e}r ",
    " anterioridad " : " {a}{n}{t}{e}rad ",
    " antes " : " ans ",
    " apenas " : " ap ",
    #aunque au
    #" arriba " : "",
    " atrás " : " atrj ",
    " aunque " : " au ",
    " bajo " : " bj ",
    " bastante " : " bt ",
    " bondad " : " bad ",
    " breve " : " brv ",
    " brevedad " : " brvad",
    " bueno " : " bn ",
    " buena " : " ba ",
    " bueno " : "bo",
    " buenamente " : " bm ",
    " casi " : " cs ",
    " cerca " : " cc ",
    " ciego " : " cg ",
    " ciega " : " cga ",
    " cierto " : " ct ",
    " conmigo " : " {c}{o}{n}m ",
    " condición " : " {c}{o}{n}mión ", #revisar
    " consecuencia " : " {c}{o}{n}sc ",
    " consecuente " : " {c}{o}{n}st ",
    " consigo " : " {c}{o}{n}s ",
    " contigo " : " {c}{o}{n}t ",
    " contra " : " {c}{o}{n}tr ",
    " contrario " : " {c}{o}{n}trr ",
    " contrariedad " : " {c}{o}{n}trrad ",
    " cual " : " cl ",
    " cualquier " : " cq ",
    " cualquiera " : " cqa ",
    " cuando " : " cd ",
    " cuanto " : " cu ",
    " cuyo " : " cy ",
    " debajo " : " dbj ",
    " dice " : " dc ",
    " delante " : " dl ",
    " demás " : " dm ",
    " demasiado " : " dmd ",
    " desde " : " ds ",
    " después " : " dp ",
    " detrás " : " dtr ",
    " diferente " : " dft ",
    " dificil " : " df ",
    " dijo " : " dj ",
    " donde " : " dd ",
    " dondequier " : " ddq ",
    " dondequiera " : " ddqa ",
    " durante " : " du ",
    " efectivo " : " efw ",
    " efectividad " : " efwad ",
    " efecto " : " ef ",
    " ejemplar " : " ejr ",
    " ejemplo " : " ej ",
    " encima " : " enc ",
    " entonces " : " ent ",
    " entretanto " : " entret ",
    #" este " : " est ", #revisar: este es z
    " esta " : " esta ",
    " estaba " : " esb ",
    " estaban " : " esbn ",
    " estado " : " esd ",
    " están " : " esn ",
    " estando " : " esnd ",
    " estar " : " esr ",
    " estuvo " : " esv ",
    " exterior " : " xr ",
    " fácil " : " fá ",
    " facilidad " : " fad ",
    " favor " : " fv ",
    " general " : " gn ",
    " generalidad " : " gad ",
    " grande " : " gd ",
    " había " : " hb ",
    " habían " : " hbn ",
    " habido " : " hbd ",
    " hacer " : " hr ",
    " hacia " : " hc ",
    " hasta " : " hs ",
    " haya " : " hy ",
    " hayan " : " hyn ",
    " hermano " : " hm ",
    " hermana " : " hma ",
    " hijo " : " hj ",
    " hija " : " hja ",
    " historia " : " ht ",
    " hambre " : " hw ",
    " igual " : " ig ",
    " igualdad " : " igad ",
    " importancia " : " impc ",
    " importante " : " impt ",
    " inferior " : " inf ",#revisar in
    " inferioridad " : " infad ",#revisar in
    " inmediato " : " inm ",#revisar in
    " interés " : " {i}{n} ",
    " interesante " : " intert ",
    " interior " : " interr ", #revisar
    " interioridad " : " interrad ",
    " joven " : " jv ",
    " juventud " : " jvt ",
    " junto " : " jt ",
    " lejos " : " lj ",
    " luego " : " lü ",
    " lugar " : " lu ",
    " madre " : " ma ",
    " manera " : " mn ",
    " mayor " : " my ",
    " mayoría " : " myr ",
    " mediante " : " mdt ",
    " medio " : " md ",
    " mejor " : " mj ",
    " menos " : " ms ",
    " mientras " : " mtr ",
    " mismo " : " mmo ",
    " mujer " : " mu ",
    " nada " : " nad ",
    " nadie " : " nd ",
    " natural " : " nt ",
    " naturaleza " : " ntz ",
    " naturalidad " : " ntad ",
    " necesario " : " n{c}{r} ", #revisar cr
    " necesidad " : " ncad ",
    " ningún " : " ng ",
    " ninguna " : " nga ",
    " ninguno " : " ngo ",
    " niño " : " nñ ",
    " nuevo " : " nv ",
    " nuestro " : " nü ",
    " novedad " : " nvad ",
    " números " : " #s ",
    " nunca " : " nc ",
    " ocasión " : " oión ",
    " oficio " : " of ",
    " oficial " : " ofl ",
    " oportuno " : " op ",
    " oportunidad " : " opad ",
    " otro " : " otr ",
    " padre " : " pa ",
    " pequeño " : " pñ ",
    " persona " : " pn ",
    " personal " : " pnl ",
    " personalidad " : " pnla ", #revisar ad
    " poco " : " pc ",
    " poder " : " {p}{r} ",
    " podía " : " pd ",
    " porque " : " pq ",
    " principal " : " precl ",#revisar
    " principio " : " prec ",#revisar
    " pronto " : " {p}{r}{t} ",
    " propio " : " prep ", #revisar
    " propiedad " : " prepad ", #revisar
    " puede " : " pü ",
    " quién " : " qn ",
    " razón " : " rz ",
    " relación " : " rl ",
    " relatividad " : " rlvad ",
    " relativo " : " rlv ",
    " sido " : " sd ",
    " siguiente " : " sg ",
    " sino " : " sn ",
    " siquiera " : " sq ",
    " sitio " : " st ",
    " sitación " : " stión ",
    " solo " : " sl ",
    " superior " : " sp ",
    " superioridad " : " spad ",
    " suyo " : " sy ",
    " también " : " tb ",
    " tampoco " : " tpc ",
    " tanto " : " tt ",
    " temporal " : " tpl ",
    " tener " : " {t}{r} ",
    " tenían " : " tn ",
    " tenido " : " tnd ",
    " tiempo " : " tp ",
    " todavía " : " tv ",
    " todo " : " td ",
    " trabajo " : " trb ",
    " trabajador " : " trbor ",
    " trabajar " : " trbr ",
    " tuyo " : " ty ",
    " último " : " úl ",
    " único " : " úc ",
    " veces " : " vc ",
    " vida " : " vd ",
    " verdad " : " vad ",
    " vuestro " : " vü ",



    " a " : " a ",
    " bien " : " b ",
    " con " : " c ",
    " de " : " d ",
    " el " : " e ",
    " fue " : " f ",
    " gran " : " g ",
    " haber " : " h ",
    " si " : " i ",
    " jamas " : " j ",
    " al " : " k ",
    " le " : " l ",
    " me " : " m ",
    " no " : " n ",
    " o " : " o ",
    " por " : " p ",
    " que " : " q ",
    " ser " : " r ",
    " se " : " s ",
    " te " : " t ",
    " un " : " u ",
    " vez " : " v ",
    " son " : " x ",
    " y " : " y ",
    " este " : " z ",
    " año " : " ñ ",
    " como " : " w ",
    " pues " : " ü ",
    " ella " : " ll ",

    " más " : " á ",
    " él " : " é ",
    " sí " : " í ",
    " aquél " : " ó ",
    " según " : " ú ",

    " la " : " . ",
    " del " : " ÷ ",
    " sobre " : " ; ",
    " lo " : " - ",
    " grado " : " = ",
    " siempre " : " ( ",
    " su " : " ) ",
    " en " : " ? ",
    " pero " : " ! ",
    " sin " : " * ",
    " los " : " < ",
    " número " : " # ",
    " las " : " & ",

    " para " : " â ",#caracter especial
    " ante " : " î ",#caracter especial
    " cada " : " ô ",#caracter especial
    " es " : " ë ",#caracter especial

    " com" : " -",
    " con" : " :",
    " dis" : " ÷",
    " ex" : " x",
    " pre" : " !",
    " re" : " r",
    " sobre" : " ;",
    " entre" : " »",#caracter especial
    " inter" : " ψ",#caracter especial

    "mente " : "m ",
    "que " : "q ",
    "ión " : "# ",
    "ando " : "îd ",
    "endo " : "?d ",
    "iendo " : "÷d ",
    "accíon " : "a# ",
    "eccíon " : "e# ",
    "iccíon " : "i# ",
    "uccíon " : "u# ",

    "ab" : ",",
    "ad" : "ô",
    "al" : "k",
    "an" : "î",
    "ar" : "â",
    "as" : "&",
    "br" : ";",
    "cr" : ":",
    "dr" : "÷",
    "em" : "(",
    "en" : "?",
    "er" : '"',
    "es" : "ë",
    "grado" : "=",
    "im" : ")",
    "sin" : "*",
    "ión" : "#",
    "om" : "w",
    "on" : "x",
    "or" : "û",
    "os" : "<",
    "pr" : "j",
    "qu" : "q",
    "tr" : "»",
    "ue" : "ü",

    "{a}{n}{t}{e}" : "î",#adaptacion para palabra con 2 o mas signos
    "{c}{o}{n}" : ":",#adaptacion para palabra con 2 o mas signos
}

def getChar(c):
    """Traducir un simple charácter a su equivalente en Braille,
    de acuerdo a la tabla de traducción."""
    if not (isinstance(c, str)):
        c = str(c)
    if not (c in tabla_trans):
        raise LookupError("Signo generador buscado no en la tabla")
    else:
        return tabla_trans[c]


def traducir(st):
    """Traducir un string entero a braille."""
    if not (isinstance(st, str)):
        st = str(st)
    r = ""
    for i in st:
        try:
            r += getChar(i)
        except LookupError:
            r += i

    return r

def getCharGrado2(c):
    """Traducir un simple charácter a su equivalente en Braille,
    de acuerdo a la tabla de traducción."""
    if not (isinstance(c, str)):
        c = str(c)
    if not (c in tabla_trans_grado2):
        raise LookupError("Signo generador buscado no en la tabla")
    else:
        return tabla_trans_grado2[c]


def traducirGrado2(st):
    """Traducir un string entero a braille."""
    if not (isinstance(st, str)):
        st = str(st)
    r = ""
    for i in st:
        try:
            r += getCharGrado2(i)
        except LookupError:
            r += i

    return r

def reemplazargrado2(st):
    """reemplazar las palabras de grado 2."""
    r = st
    for i in tabla_trans2:
        r = r.replace(i,tabla_trans2[i])
    r = r.replace("{","")
    r = r.replace("}","")
    return "normal:\n " + r + " \nbraille:\n" + traducirGrado2(r)
